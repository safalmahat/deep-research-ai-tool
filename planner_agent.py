from agents import Agent, WebSearchTool
from pydantic import BaseModel


NUMBER_OF_SEARCHES=2

INSTRUCTIONS=f"You are a helpful research assistant. Given a query, come up with a set of web searches \
    to perform to best answer the query. Output {NUMBER_OF_SEARCHES} terms to query for."

class WebSearchItem(BaseModel):
    reason:str
    "Your reason why this search is important to the query"

    query:str
    "The search term to use for web search" 

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searches to perform to best answer the query"""    

planner_agent= Agent(
    name="Planner Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan
)       