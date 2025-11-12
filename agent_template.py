# Dependencies
import asyncio
import os
from dotenv import load_dotenv

# Google ADK Dependencies:
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types

print("✅ ADK components imported successfully.")


# Import Google API key:
try:
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

# Define the Agent(s):





# Run the agent (debug for prototyping, no need to create and maintain sessions).
runner = InMemoryRunner(agent=root_agent)
print("✅ Runner created.")


async def main():
    try:
        # Queries to the Agent:
        response = await runner.run_debug(
                "Write a blog post about the benefits of multi-agent systems for software developers"
        )

    finally:
        # Clean up the runner and close any open HTTP sessions
        await runner.close()
        # Give async cleanup tasks time to complete
        await asyncio.sleep(1)


if __name__ == "__main__":
	asyncio.run(main())
