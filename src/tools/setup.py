from langchain_core.tools import BaseTool

from src.tools.search import get_search_tool


def get_tools() -> list[BaseTool]:
    tools = []
    tools.append(get_search_tool())
    return tools
