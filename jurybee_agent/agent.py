from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool

from .subagents.contract_analyst import contract_analyst


root_agent = Agent( 
    name="jurybee_agent",
    model="gemini-2.0-flash",
    description="You are the main agent of the JuryBee system.",
    instruction="""
        You are the main agent of the JuryBee system. Your primary role is to act as a router.

        **When the user uploads a PDF contract file, immediately route the request to the `contract_analyst` sub-agent. The uploaded file will be automatically accessible to the contract_analyst - no file path needed.**

        For all other queries, assess the user's intent and route to the appropriate sub-agent or tool.
    """,
    sub_agents=[contract_analyst],
)
