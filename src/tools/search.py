from langchain.tools.ddg_search.tool import DuckDuckGoSearchResults


def get_search_tool() -> DuckDuckGoSearchResults:
    return DuckDuckGoSearchResults()
