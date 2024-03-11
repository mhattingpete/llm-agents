from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import (
    ChatMessageHistory,
    StreamlitChatMessageHistory,
)
from langchain_core.chat_history import BaseChatMessageHistory


def get_streamlit_memory_buffer() -> (
    tuple[StreamlitChatMessageHistory, ConversationBufferMemory]
):
    msgs = StreamlitChatMessageHistory()
    memory = ConversationBufferMemory(
        chat_memory=msgs,
        return_messages=True,
        memory_key="chat_history",
        output_key="output",
    )
    return msgs, memory


def get_buffer_memory() -> ConversationBufferMemory:
    return ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
    )


STORE = {}


def get_streamlit_memory() -> StreamlitChatMessageHistory:
    return StreamlitChatMessageHistory()


def get_memory() -> ChatMessageHistory:
    return ChatMessageHistory()


def get_session_history(
    session_id: str, get_chat_memory: callable = get_streamlit_memory
) -> BaseChatMessageHistory:
    if session_id not in STORE:
        STORE[session_id] = get_chat_memory()
    return STORE[session_id]
