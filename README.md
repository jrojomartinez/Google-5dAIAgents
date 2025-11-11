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

## Usage

Run the agent:
```bash
python3 Day_1a.py
```

For interactive async usage:
```bash
python3 -m asyncio
```

The agent will execute several example queries including:
- Information about the Agent Development Kit
- Real-time weather information
- Recent world events
- Current movie releases

## Project Structure

- `Day_1a.py` - Main agent implementation with Google Search integration (Day 1 of the course)
- `.env` - Environment variables configuration (not tracked in git)
- `CLAUDE.md` - Development guidance for Claude Code
- `.gitignore` - Excludes sensitive files from version control

## Security Note

⚠️ **Important**: Never commit your `.env` file to version control. This file contains your API key and is excluded via `.gitignore`. Always keep your API keys secret and secure.

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

## License

This project is for educational and experimental purposes.

## Acknowledgments

Built as part of the Google AI Agents Intensive Course on Kaggle.
