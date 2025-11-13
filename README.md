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
   git clone https://github.com/jrojomartinez/Google-5dAIAgents.git
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
├── .env                                # Environment variables (not tracked in git)
├── .gitignore                          # Git ignore rules
├── README.md                           # This file
├── CLAUDE.md                           # Claude Code development guidance (not tracked in git)
├── agent_template.py                   # Template for creating new agents
├── White_Papers/                       # Course white papers
│   ├── Day 1 - Introduction to Agents.pdf
│   ├── Day 2 - Agent Tools & Interoperability with Model Context Protocol (MCP).pdf
│   ├── Day 3 - Context Engineering: Sessions & Memory.pdf
│   └── Day 4 - Agent Quality.pdf
├── Day_1a/                             # Day 1a: Basic Agent with Google Search
│   ├── agent.py                        # Main agent with Google Search integration
│   ├── .gitignore                      # Local ignore rules
│   ├── __init__.py                     # Python package init
│   └── evalset*.json                   # Evaluation sets
├── Day_1b_Section2_orchestrator/       # Orchestrator pattern (manual coordination)
│   ├── agent.py                        # Research + Summarizer with root coordinator
│   └── __init__.py                     # Python package init
├── Day_1b_Section3_sequential/         # Sequential agent pattern (pipeline)
│   ├── agent.py                        # Blog pipeline: Outline -> Write -> Edit
│   └── __init__.py                     # Python package init
├── Day_1b_Section4_parallel/           # Parallel agent pattern (concurrent execution)
│   ├── agent.py                        # Multi-domain research with aggregation
│   └── __init__.py                     # Python package init
└── Day_1b_Section5_loop/               # Loop agent pattern (iterative refinement)
    ├── agent.py                        # Story writing with critic feedback loop
    └── __init__.py                     # Python package init
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

## White Papers

Each day of the course includes a comprehensive white paper covering theoretical foundations and best practices. These papers provide deep dives into agent architecture, design patterns, and implementation strategies.

### Day 1: Introduction to Agents

📄 **[View White Paper](White_Papers/Day%201%20-%20Introduction%20to%20Agents.pdf)**

**Summary:**
This white paper introduces AI agents as autonomous systems that think, act, and observe to accomplish goals (as the evolution from passive generative AI). It provides an architectural framework for building production-grade agents, covering core components (Model, Tools, Orchestration), a 5-level capability taxonomy, and practical guidance on deployment, security, and operations.

**Key Points:**
- **Core Architecture**: Agents consist of three essential components - the Model (brain for reasoning), Tools (hands for action), and Orchestration Layer (nervous system for coordination).
- **5-Step Problem-Solving Process**: Get the Mission → Scan the Scene → Think It Through → Take Action → Observe and Iterate.
- **Taxonomy of Agentic Systems**: 5 levels of capability progression.
  - Level 0: Core Reasoning System (LM without tools, relies on training data only).
  - Level 1: Connected Problem-Solver (adds external tools for real-time data and actions).
  - Level 2: Strategic Problem-Solver (context engineering and multi-step planning).
  - Level 3: Collaborative Multi-Agent System (team of specialized agents working together).
  - Level 4: Self-Evolving System (dynamically creates new tools/agents to fill capability gaps).
- **Agent Ops Discipline**: New operational paradigm for measuring, debugging, and deploying agents using metrics-driven development, LM judges, and OpenTelemetry traces.
- **Production Considerations**: Covers deployment strategies, security (identity management, policies, guardrails), and scaling from single agents to enterprise fleets.
- **Multi-Agent Design Patterns**: Coordinator, Sequential, Iterative Refinement, and Human-in-the-Loop patterns for complex workflows.
- **Interoperability Standards**: Agent2Agent (A2A) protocol, Model Context Protocol (MCP), and emerging payment protocols for the agentic economy.
- **Learning and Evolution**: Agents can adapt through enhanced context engineering, tool optimization, and human feedback loops.
- **Advanced Examples**: Google Co-Scientist (research collaboration) and AlphaEvolve (algorithm optimization).

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

### Day 1b: Multi Agent Systems (MAS)

**Description:**
Exploration of multi-agent system architectures using Google ADK. Demonstrates four key patterns for orchestrating multiple agents to work together: Orchestrator, Sequential, Parallel, and Loop patterns. Each pattern addresses different coordination needs and workflow requirements.

#### Section 2: Orchestrator Pattern

**Location:** `Day_1b_Section2_orchestrator/`

**Description:**
Implements a manual orchestration pattern where a root coordinator agent explicitly calls sub-agents as tools. The coordinator maintains full control over when and how each agent is invoked.

**Architecture:**
- **ResearchAgent**: Specialized agent with `google_search` tool to find and present research findings
- **SummarizerAgent**: Takes research findings and creates a concise bulleted summary
- **Root Coordinator**: Orchestrates the workflow by wrapping sub-agents in `AgentTool` and calling them sequentially based on its instructions

**Key Concepts:**
- Manual workflow orchestration
- Sub-agents wrapped as tools using `AgentTool`
- State management with `output_key` for passing data between agents
- Explicit control flow defined in coordinator's instructions

**Example Query:**
"What are the latest advancements in quantum computing and what do they mean for AI?"

**Run:**
```bash
python3 Day_1b_Section2_orchestrator/agent.py
# or
adk run Day_1b_Section2_orchestrator
```

#### Section 3: Sequential Agent Pattern

**Location:** `Day_1b_Section3_sequential/`

**Description:**
Uses `SequentialAgent` to create an automated pipeline where agents execute in a fixed order. Each agent's output automatically becomes available to the next agent in the sequence.

**Architecture:**
- **OutlineAgent**: Creates a structured blog post outline with headline, introduction, sections, and conclusion
- **WriterAgent**: Writes a 200-300 word blog post following the outline from the previous agent
- **EditorAgent**: Polishes the draft by fixing grammar, improving flow, and enhancing clarity
- **BlogPipeline**: `SequentialAgent` that automatically runs all three agents in order

**Key Concepts:**
- Automatic sequential execution
- State variables (`{blog_outline}`, `{blog_draft}`) passed between agents
- Pipeline pattern for multi-stage processing
- No manual orchestration needed

**Example Query:**
"Write a blog post about the benefits of multi-agent systems for software developers"

**Run:**
```bash
python3 Day_1b_Section3_sequential/agent.py
# or
adk run Day_1b_Section3_sequential
```

#### Section 4: Parallel Agent Pattern

**Location:** `Day_1b_Section4_parallel/`

**Description:**
Combines `ParallelAgent` and `SequentialAgent` to run multiple agents concurrently, then aggregate their results. Ideal for independent tasks that can be executed simultaneously to save time.

**Architecture:**
- **TechResearcher**: Researches latest AI/ML trends (runs in parallel)
- **HealthResearcher**: Researches medical breakthroughs (runs in parallel)
- **FinanceResearcher**: Researches fintech innovations (runs in parallel)
- **ParallelResearchTeam**: `ParallelAgent` that executes all three researchers simultaneously
- **AggregatorAgent**: Synthesizes findings from all three research streams into an executive summary
- **Root Agent**: `SequentialAgent` that runs parallel team first, then aggregator

**Key Concepts:**
- Concurrent execution with `ParallelAgent`
- Multiple output keys (`tech_research`, `health_research`, `finance_research`)
- Result aggregation from parallel streams
- Nested agent patterns (Parallel within Sequential)

**Example Query:**
"Run the daily executive briefing on Tech, Health, and Finance"

**Run:**
```bash
python3 Day_1b_Section4_parallel/agent.py
# or
adk run Day_1b_Section4_parallel
```

#### Section 5: Loop Agent Pattern

**Location:** `Day_1b_Section5_loop/`

**Description:**
Implements an iterative refinement loop using `LoopAgent`. Agents repeatedly execute until a condition is met or maximum iterations are reached. Demonstrates human-in-the-loop style workflows where outputs are refined through multiple iterations.

**Architecture:**
- **InitialWriterAgent**: Creates the first draft of a short story (runs once)
- **CriticAgent**: Reviews the story and provides feedback or approval
- **RefinerAgent**: Rewrites the story based on feedback OR calls `exit_loop()` function to break the loop
- **StoryRefinementLoop**: `LoopAgent` containing Critic and Refiner with max 2 iterations
- **Root Agent**: `SequentialAgent` that runs Initial Writer once, then enters the refinement loop

**Key Concepts:**
- Iterative refinement with `LoopAgent`
- Loop exit control with `FunctionTool(exit_loop)`
- State mutation (RefinerAgent overwrites `current_story`)
- Max iterations safety limit to prevent infinite loops
- Conditional workflow based on agent output

**Example Query:**
"Write a short story about a lighthouse keeper who discovers a mysterious, glowing map"

**Run:**
```bash
python3 Day_1b_Section5_loop/agent.py
# or
adk run Day_1b_Section5_loop
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
