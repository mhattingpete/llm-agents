from src.settings.models import BaseSettings


def get_llm_model(model_config: BaseSettings = None):
    raise NotImplementedError


def get_chat_model(model_config: BaseSettings = None):
    raise NotImplementedError
