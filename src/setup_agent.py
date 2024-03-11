from operator import itemgetter

from dotenv import load_dotenv
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory

from src.agents.react import get_agent
from src.memory.setup import get_session_history
from src.models.hf_endpoint import get_llm_model
from src.settings.models import CFGHFOpenchat
from src.tools.setup import get_tools

load_dotenv()


def clean_output(output: str) -> str:
    output = output.replace("<|end_of_turn|>", "")
    for stop_sequence in CFGHFOpenchat.stop_sequences:
        output = output.replace(stop_sequence, "")
    return output


class AgentRunner:
    def __init__(self) -> None:
        llm = get_llm_model()
        tools = get_tools()
        agent = get_agent(llm, tools)
        self.__runnable = RunnableWithMessageHistory(
            agent,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        ) | {
            "output": itemgetter("output") | RunnableLambda(lambda x: clean_output(x)),
            "intermediate_steps": itemgetter("intermediate_steps"),
        }

    def get_answer(
        self,
        question: str,
        session_id: str = "",
        callbacks: list[BaseCallbackHandler] = None,
    ):
        return self.__runnable.invoke(
            {"input": question},
            config={"configurable": {"session_id": session_id, "callbacks": callbacks}},
        )
