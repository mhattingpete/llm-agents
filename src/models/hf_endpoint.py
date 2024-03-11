import os

from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

from src.settings.models import CFGHFOpenchat, HFBaseSettings


def get_llm_model(model_config: HFBaseSettings = CFGHFOpenchat) -> HuggingFaceEndpoint:
    llm: HuggingFaceEndpoint = HuggingFaceEndpoint(
        endpoint_url=model_config.endpoint_url,
        huggingfacehub_api_token=os.getenv("API_TOKEN"),
        task=model_config.task,
        max_new_tokens=model_config.max_tokens,
        top_k=model_config.top_k,
        temperature=model_config.temperature,
        repetition_penalty=model_config.repetition_penalty,
        streaming=model_config.streaming,
        stop_sequences=model_config.stop_sequences,
    )
    return llm


def get_chat_model(model_config: HFBaseSettings = CFGHFOpenchat) -> ChatHuggingFace:
    llm: HuggingFaceEndpoint = get_llm_model(model_config)
    return ChatHuggingFace(llm=llm, model_id=model_config.name)
