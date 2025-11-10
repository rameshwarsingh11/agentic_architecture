# weather_agent.py

import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = ""

# If you haven’t exported your Gemini key globally, you can set it here
# os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY_HERE"

from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub


# --- Define your custom tool ---
def get_weather(city: str) -> str:
    """Simple mock weather function."""
    return f"It's always sunny in {city}!"


# --- Register the tool ---
tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="Get the weather for a given city name"
    )
]

# --- Load the reasoning prompt from LangChain Hub ---
prompt = hub.pull("hwchase17/react")

# --- Initialize the Gemini LLM ---
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")


# --- Create the ReAct agent ---
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# --- Build an executor to run the agent ---
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Run a sample query ---
response = agent_executor.invoke({"input": "what is the weather in San Francisco?"})
print(response)
