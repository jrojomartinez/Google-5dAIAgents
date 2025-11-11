# Dependencies
import asyncio
import os
from dotenv import load_dotenv

# Google ADK Dependencies:
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

print("✅ ADK components imported successfully.")


# Import Google API key:
import APIKeys
try:
	# GOOGLE_API_KEY = APIKeys.GOOGLE_API_KEY
	# os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
	load_dotenv(override=True)
	GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
	print("✅ Gemini API key setup complete.")
except Exception as e:
	print(
		f"🔑 Authentication Error: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}"
	)

# Retry Config:
retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

# Define the Agent:
root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)
print("✅ Root Agent defined.")


async def main():
    # Run the agent (debug for prototyping, no need to create and maintain sessions).
    runner = InMemoryRunner(agent=root_agent)
    print("✅ Runner created.")

    try:
        # Queries to the Agent:
        response = await runner.run_debug(
            "What is Agent Development Kit from Google? What languages is the SDK available in?"
        )

        response = await runner.run_debug("What's the weather in London?")
        response = await runner.run_debug("Who won the last soccer world cup?")
        response = await runner.run_debug("What new movies are showing in theaters now?")
    finally:
        # Clean up the runner and close any open HTTP sessions
        await runner.close()
        # Give async cleanup tasks time to complete
        await asyncio.sleep(1)



if __name__ == "__main__":
	asyncio.run(main())
