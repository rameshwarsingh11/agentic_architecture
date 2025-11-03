# Disable LangChain tracing
import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"

# Set your Google API key or pass at run time using this command: export GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE" 
# os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY_HERE"

from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub

# Define your tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# Wrap the tool
tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="Get the weather for a given city name"
    )
]

# Load reasoning prompt (from LangChain Hub)
prompt = hub.pull("hwchase17/react")

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # You can also use gemini-1.5-flash for cheaper/faster responses

# Create the ReAct agent
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# Create executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run it
response = agent_executor.invoke({"input": "what is the weather in SF?"})
print(response)