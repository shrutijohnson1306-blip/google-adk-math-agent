from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from math_agent.tools import add, subtract, multiply, divide
from math_agent.prompts import MATH_AGENT_INSTRUCTION

root_agent = Agent(
    name="calculator_agent",
    model="gemini-2.5-flash",  # use any model your ADK supports
    description="A simple math calculator agent.",
    instruction=MATH_AGENT_INSTRUCTION,
    tools=[
        FunctionTool(add),
        FunctionTool(subtract),
        FunctionTool(multiply),
        FunctionTool(divide),
    ],
)
