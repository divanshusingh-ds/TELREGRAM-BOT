from langchain.tools import tool

@tool
def get_cricket_score(country: str) -> str:
    """
    Use this tool when the user asks for a cricket
    score between India and another country.
    """
    return f"Score between India and {country} is 120-3"

@tool
def get_football_score(home_team: str, away_team: str) -> str:
    """
    Use this tool when the user asks for a football
    score between two teams.
    """
    return f"Score between {home_team} and {away_team} is 2-1"



