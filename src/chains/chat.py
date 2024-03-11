from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import BaseChatPromptTemplate
from settings.models import HFChatModel, hf_chat_model_settings

from src.models.hf_endpoint import get_chat_model
from src.prompts.chat import qna_prompt


class QnAComponent:
    def __init__(
        self,
        prompt: BaseChatPromptTemplate,
        model_config: HFChatModel,
    ):
        self.chain = prompt | get_chat_model(model_config) | StrOutputParser()


class QnAModel(QnAComponent):
    def __init__(self):
        super().__init__(prompt=qna_prompt, model_config=hf_chat_model_settings)
