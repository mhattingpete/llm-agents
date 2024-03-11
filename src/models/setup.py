from langchain_core.language_models import BaseChatModel, BaseLanguageModel

from src.models.hf_endpoint import get_chat_model as get_hf_chat_model
from src.models.hf_endpoint import get_llm_model as get_hf_llm_model
from src.models.openai import get_chat_model as get_openai_chat_model
from src.models.openai import get_llm_model as get_openai_llm_model
from src.settings.general import CFGModelType


def get_llm_model() -> BaseLanguageModel:
    if CFGModelType.type == "hf":
        llm = get_hf_llm_model()
    else:
        llm = get_openai_llm_model()
    return llm


def get_chat_model() -> BaseChatModel:
    if CFGModelType.type == "hf":
        llm = get_hf_chat_model()
    else:
        llm = get_openai_chat_model()
    return llm
