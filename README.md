# Google ADK Agents Project

A collection of AI agents built using Google's Agent Development Kit (ADK), powered by Gemini models.

## About This Project

This repository contains examples and experiments developed as part of the **Google AI Agents Intensive Course** - a 5-day hands-on program focused on building AI agents with the Agent Development Kit.

📚 **Course Link**: [5-Day AI Agents Course on Kaggle](https://www.kaggle.com/learn-guide/5-day-agents)

## Overview

This project demonstrates how to build AI agents with enhanced capabilities through tool integration, specifically leveraging Google Search for real-time information retrieval. The agents are powered by Google's Gemini models and implement modern async Python patterns.

## Features

- **Gemini Integration**: Powered by `gemini-2.5-flash-lite` model
- **Google Search Tool**: Agents can search the web for real-time information
- **Retry Logic**: Built-in exponential backoff for handling rate limits and transient errors
- **Async/Await Pattern**: Modern Python async implementation with proper resource cleanup
- **Environment-based Configuration**: Secure API key management using dotenv
- **ADK CLI Support**: Run agents using `adk run` and manage them via `adk web`

## Prerequisites

- Python 3.7+
- Google API Key (for Gemini and Google Search)
- Required packages: `google-adk` (v1.18.0), `google-genai` (v1.49.0), `python-dotenv`

## Setup

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd Google-5dAIAgents
   ```

2. **Install dependencies**
   ```bash
   pip install google-adk google-genai python-dotenv
   ```

3. **Configure your API key**

   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your-api-key-here
   ```

   The project uses the `python-dotenv` package to automatically load environment variables from this file.

## Project Structure

```
Google-5dAIAgents/
├── .env                    # Environment variables (not tracked in git)
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── CLAUDE.md               # Claude Code development guidance (not tracked in git)
├── Day_1a/                 # Day 1a implementation
│   ├── agent.py            # Main agent with Google Search integration
│   ├── .gitignore          # Local ignore rules
│   ├── __init__.py         # Python package init
│   └── evalset*.json       # Evaluation sets
└── Day_1b/                 # Day 1b implementation
    ├── agent.py            # Simple agent template
    ├── .env                # Local environment variables (not tracked)
    └── __init__.py         # Python package init
```

## Running Agents

### Method 1: Direct Python Execution

Navigate to a specific day's folder and run the agent:
```bash
cd Day_1a
python3 agent.py
```

### Method 2: ADK CLI

Run an agent using the ADK command-line interface:
```bash
adk run Day_1a
```

### Method 3: ADK Web UI

Launch the Google ADK Web UI for interactive agent management:
```bash
adk web --port 8000
```

Then open your browser and navigate to:
```
http://localhost:8000
```

The Web UI provides:
- Interactive agent execution
- Real-time monitoring and logging
- Evaluation creation and management
- Session tracking and debugging

## Day Implementations

### Day 1a: Basic Agent with Google Search

**Location:** `Day_1a/`

**Description:**
A foundational agent that demonstrates core ADK concepts including:
- Google Search tool integration for real-time information retrieval
- HTTP retry configuration with exponential backoff
- InMemoryRunner for session management
- Async/await patterns for non-blocking operations

**Features:**
- Model: `gemini-2.5-flash-lite`
- Tools: Google Search
- Retry Policy: 5 attempts with exponential backoff (base 7, initial 1s delay)
- Error Handling: Retries on HTTP errors [429, 500, 503, 504]

**Example Queries:**
- Information about the Agent Development Kit
- Real-time weather information
- Recent world events
- Current movie releases

**Run:**
```bash
python3 Day_1a/agent.py
# or
adk run Day_1a
```

### Day 1b: Coming Soon

**Location:** `Day_1b/`

**Description:**
A simple agent template for additional Day 1 exercises.

**Run:**
```bash
python3 Day_1b/agent.py
# or
adk run Day_1b
```

## Security Note

⚠️ **Important**: Never commit your `.env` files to version control. These files contain your API keys and are excluded via `.gitignore` at both the root and subfolder levels. Always keep your API keys secret and secure.

**Protected files (automatically excluded from git):**
- `.env` (root and all subdirectories)
- `APIKeys.py` (root and all subdirectories)
- `CLAUDE.md`
- `__pycache__/` directories
- `*.pyc` compiled Python files

## Technical Details

### Agent Configuration
- **Model**: `gemini-2.5-flash-lite`
- **Runner**: `InMemoryRunner` (designed for prototyping without session persistence)
- **Retry Configuration**: 5 attempts with exponential backoff (base 7, initial 1s delay) for HTTP errors [429, 500, 503, 504]

### Architecture
The project follows Google ADK's best practices:
- Agent definition with model, description, instructions, and tools
- Async execution pattern for non-blocking operations
- Proper resource cleanup with runner.close() and async sleep
- Modular structure with separate folders for each day's implementation

## Development Workflow

1. **Create a new agent**: Use `adk create Day_X` to scaffold a new agent
2. **Develop locally**: Edit the `agent.py` file in the day's folder
3. **Test with CLI**: Run `adk run Day_X` to test your agent
4. **Debug with Web UI**: Use `adk web` for interactive debugging
5. **Commit changes**: Stage and commit your work to git

## License

This project is for educational and experimental purposes.

## Acknowledgments

Built as part of the Google AI Agents Intensive Course on Kaggle.
