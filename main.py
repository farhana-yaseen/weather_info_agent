from agents import Runner, set_tracing_disabled
from my_agents.weather_agent import weather_agent

set_tracing_disabled(True)

# stip() remove white space title() (e.g., "karachi" → "Karachi")
user_input = input("Enter your city name: ").strip().title()

query = f"What’s the weather in {user_input}?"

result = Runner.run_sync(starting_agent=weather_agent, input=query)

print(result.final_output)
