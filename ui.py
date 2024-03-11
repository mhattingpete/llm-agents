import uuid

import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler

from src.setup_agent import AgentRunner

st.set_page_config(page_title="LangChain: Chat with search", page_icon="🦜")
st.title("🦜 LangChain: Chat with search")

executor = AgentRunner()
session_id = {"current": ""}


def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"}
    ]
    st.session_state.steps = {}
    # reset session id to trigger new chat history
    session_id["current"] = str(uuid.uuid4())


# Store LLM generated responses
if "messages" not in st.session_state.keys():
    clear_chat_history()


# Render chat history
for idx, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg.get("role")):
        # Render intermediate steps if any were saved
        for step in st.session_state.steps.get(str(idx), []):
            if step[0].tool == "_Exception":
                continue
            with st.status(
                f"**{step[0].tool}**: {step[0].tool_input}", state="complete"
            ):
                st.markdown(step[0].log)
                st.markdown(step[1])
        st.markdown(msg.get("content"))


st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Get new input
if question := st.chat_input(placeholder="Who won the Women's U.S. Open in 2018?"):
    st.chat_message("user").markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
        response = executor.get_answer(
            question,
            session_id["current"],
            callbacks=[st_cb],
        )
        output = response[
            "output"
        ]  # str(response["output"]).replace("<|end_of_turn|>", "")
        st.markdown(output)
        st.session_state.steps[str(len(st.session_state.messages) - 1)] = response[
            "intermediate_steps"
        ]
        st.session_state.messages.append({"role": "assistant", "content": output})
