
from agents import Agent
from configuration.config import MODEL
from my_tools.weather_tool import get_weather


weather_agent = Agent(
    name = "Weather Info Agent",
    instructions="You are a helpful assistant. If a user asks about the weather in any city, use the weather tool to provide the current weather information.",
    model = MODEL,
    tools = [get_weather], 
)
