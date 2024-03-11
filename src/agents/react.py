from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool

from src.models.setup import get_llm_model
from src.prompts.agent import react_prompt


def get_agent(llm: BaseLanguageModel, tools: list[BaseTool]) -> AgentExecutor:
    llm = get_llm_model()
    agent = create_react_agent(llm, tools, react_prompt)
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
    )
