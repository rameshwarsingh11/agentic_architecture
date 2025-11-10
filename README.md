from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import Tool
from langchain import hub
from langgraph.prebuilt import create_react_agent
from langgraph.graph import AgentExecutor

# Define your tool

def get_weather(city: str) -> str:
"""Get weather for a given city."""
return f"It's always sunny in {city}!"

tools = [
Tool(
name="get_weather",
func=get_weather,
description="Get the weather for a given city name"
)
]

# Load ReAct prompt

prompt = hub.pull("hwchase17/react")

# Initialize Gemini model

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Create ReAct agent

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# Execute agent

executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = executor.invoke({"input": "what is the weather in Toronto?"})
print(response)
