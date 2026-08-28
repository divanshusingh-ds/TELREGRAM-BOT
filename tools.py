from langchain.tools import tool

@tool
def get_cricket_score(country: str) -> str:
    """
    Use this tool when the user asks for a cricket
    score between India and another country.
    """
    return f"Score between India and {country} is 120-3"
