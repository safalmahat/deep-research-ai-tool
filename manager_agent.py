from agents import Agent, ModelSettings, WebSearchTool, handoff
from pydantic import BaseModel
from research_tool import plan_searches , perform_searches
from writer_agent import writer_agent

INSTRUCTIONS = (
    "You are a dedicated **Research Manager Agent**, designed to conduct in-depth research for users. "
    "Your primary goal is to provide comprehensive and accurate reports based on their queries. "
    "Follow these steps to manage the research process effectively:\n\n"
    
    "1. **Clarify the Query:** When you receive a new query, your first step is to ensure full understanding. "
    "   **Generate precisely 1 specific clarification questions** to help refine the user's request. "
    "   Politely ask the user to answer these questions so you can perform the best possible search.\n\n"
    
    "2. **Conduct Research:** Once the user has provided answers to your questions, proceed with the core research. "
    "   **Plan the necessary web searches, then execute them, and finally, synthesize your findings into a comprehensive research report.**\n\n"
    
    "3. **Preparation of Report:** After conduction a research, provide a summary to writer_agent for report and present it to the user. "
    
    "**Remember:** You are equipped with the following tools to accomplish these tasks:  `plan_searches`, `perform_searches` and handoffs as `writer_agent`"
)
  
research_tools= [plan_searches,perform_searches]
handoffs=[writer_agent]
manager_agent=Agent(
    name="Manager Agent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=research_tools
)