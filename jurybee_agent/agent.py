from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from .subagents.contract_analyst import contract_analyst


root_agent = Agent( 
    name="jurybee_agent",
    model="gemini-2.0-flash",
    description="You are the main agent of the JuryBee system.",
    instruction="""
        You are the main agent of the JuryBee system. Your primary role is to act as a router, directing user queries and inputs to the most appropriate sub-agent.

        **If the user provides a contract in PDF format, immediately route the request to the `contract_analyst` sub-agent for processing and analysis.**

        For all other queries, carefully assess the user's intent and determine which of your available tools or sub-agents can best fulfill their request.
    """, #this is the main router for our project it will decide what tools is necessery based on user query
    sub_agents=[contract_analyst],
)
