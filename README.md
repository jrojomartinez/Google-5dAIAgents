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
- **5-Step Problem-Solving Process**: Get the Mission → Scan the Scene → Think It Through → Take Action → Observe and Iterate. This is the clasical 'Think, Act, Observe' loops we see mentioned in the industry.
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

### Day 2: Agent Tools & Interoperability with Model Context Protocol (MCP)

📄 **[View White Paper](White_Papers/Day%202%20-%20Agent%20Tools%20%26%20Interoperability%20with%20Model%20Context%20Protocol%20(MCP).pdf)**

**Summary:**
This white paper focuses on Agent Tools—the mechanism that allows Language Models to interact with the external world beyond their training data. It covers three main areas: (1) best practices for tool design, emphasizing that tools should be task-oriented, well-documented, and produce concise outputs; (2) the Model Context Protocol (MCP), an open standard that solves the N×M integration problem by providing a unified interface between AI models and external services; and (3) critical security challenges that arise when deploying MCP in enterprise environments.

**Key Points:**
- **Agent Tools Fundamentals**: Tools allow LLMs to retrieve data (know something) or perform actions (do something). Three types exist: Function Tools (developer-defined), Built-in Tools (model service provided, like Google Search), and Agent Tools (specialized agents invoked as tools).
- **Tool Design Best Practices**: Tools must encapsulate granular **tasks** (not just mirror APIs), use clear/descriptive names, provide comprehensive parameter documentation, design for concise output to avoid context window bloat, and include instructive error messages that guide the LLM on resolution.
- **Model Context Protocol (MCP)**: Open standard introduced in 2024 to solve the N×M integration explosion problem. Uses client-server architecture (Host, Client, Server) with JSON-RPC 2.0 communication over stdio or Streamable HTTP.
- **MCP Core Primitives**:
  - **Capabilities offered by the Server to the Client**:
    - **Tools** (most widely adopted): Standardized JSON schema for describing available functions—servers advertise their capabilities (e.g., `get_current_weather`) with parameter details and return types.
    - **Resources**: Server-side contextual data provision—servers expose background information like file contents, configurations, or database schemas that agents can read for context.
    - **Prompts**: Server provides reusable prompt templates related to its Tools and Resources—gives clients higher-level examples of how to use the server's capabilities with an LLM (security concerns exist around third-party instruction injection).
  - **Capabilities offered by the Client to the Server**:
    - **Sampling**: Server can request LLM completions from client (reversed control flow)—the server asks the client's LLM to generate content, flipping the typical request direction.
    - **Elicitation**: Server can request additional user input via client UI—the server asks the client to prompt the user for more information (e.g., confirmation before a transaction).
    - **Roots**: Client defines filesystem boundaries where servers can operate—URIs (currently file: only) that scope server operations to specific directories (servers should respect these boundaries, but no strict enforcement exists).
- **Enterprise Security Challenges**: MCP introduces new risks including Tool Shadowing (malicious tool descriptions hijacking agent decisions), Dynamic Capability Injection (unexpected tool set changes), and Confused Deputy Problem (unprivileged users tricking agents into unauthorized actions via privileged servers).
- **Security Mitigations**: Multi-layered defense required: explicit allowlists of approved tools/servers, API Gateways (like Apigee) for centralized policy enforcement, input/output sanitization (e.g., Model Armor), and scoped credentials following least privilege principles.
- **Performance Considerations**: MCP suffers from Context Window Bloat as all tool definitions load into prompts, increasing cost/latency. Dynamic tool retrieval (RAG-based tool discovery) proposed as future mitigation.
- **Enterprise Readiness Gaps**: Base MCP protocol lacks robust authentication/authorization standards, clear identity management, and native observability primitives (logging, tracing, metrics). MCP must therefore be wrapped with existing enterprise authentication and security protocols, as the protocol itself focuses solely on the Agent-Tools communication layer.

### Day 3: Context Engineering: Sessions & Memory

📄 **[View White Paper](White_Papers/Day%203%20-%20Context%20Engineering_%20Sessions%20%26%20Memory.pdf)**

**Summary:**
Context Engineering is the discipline that converts stateless LLM models into stateful, intelligent AI agents. This is achieved through the continuous management of both the information available and the information provided to the LLM. Context Engineering is essential for avoiding "context rot"—when the context window grows too large, the LLM loses focus on critical information, leading to rambling, confused responses, and degraded performance. By dynamically managing what information is provided, Context Engineering ensures responses remain focused, relevant, and high-quality. It focuses on two core architectural components: (1) Sessions, which serve as the "short-term memory" or temporary "workbench" for a single conversation, holding dialogue history and working state while managing context window bloat through compaction strategies; and (2) Memory, the "filing cabinet" that provides long-term persistence, storing extracted, curated knowledge across sessions to personalize future interactions and make the agent an expert on the user.

**Key Points:**
- **Context Engineering (CE)**: Dynamic management of the LLM's context window to provide the most relevant information. Unlike prompt engineering (static instructions), CE constructs state-aware prompts from user, history, and external data. As context grows, cost, latency, and context rot degrade performance.
- **Context Payload Components**: Includes guidance (System Instructions, Tool Definitions, Few-Shot Examples), evidential data (Memory, RAG, Tool Outputs), and immediate conversation (History, Scratchpad, User Prompt).
- **Sessions**: Container of a single, immediate conversation (the agent's temporary "workbench"). Contains Events (chronological log of inputs, responses, tool calls/outputs) and State (scratchpad for temporary data). Production requires persistent storage with strict isolation and PII redaction.
- **Session Compaction Strategies**: Token-Based Truncation (cutting old messages beyond limit) and Recursive Summarization (replacing older conversation with AI-generated summaries persisted in memory).
- **Multi-Agent Sessions**: Managed via Shared, Unified History (all agents write to one log) or Separate, Individual Histories (agents communicate via explicit messages through Agent-as-a-Tool or A2A).
- **Memory**: Long-term memory across sessions of the user and its preferences (the agent's "filing cabinet").
- **Memory vs. RAG**: RAG handles static, shared factual knowledge ("research librarian"), while Memory handles dynamic, user-specific context ("personal assistant"). Memory makes the agent an expert on the user.
- **Memory Types**: Declarative Memory ("knowing what"—facts, preferences) and Procedural Memory ("knowing how"—skills, workflows like tool call sequences).
- **Memory Organization**: Collections (self-contained natural language memories) or Structured User Profile (continuously updated core facts). Storage uses Vector Databases (semantic retrieval) and/or Knowledge Graphs (relational queries).
- **Memory Generation Pipeline**: LLM-driven ETL process with Extraction (filtering signal from noise), Transformation (Consolidation—resolving conflicts, merging duplicates, pruning stale data), and Load (storing in database).
- **Memory Retrieval: Proactive vs Reactive**: Proactive Retrieval automatically fetches memories at every turn (always-on, introduces latency but cacheable). Reactive Retrieval (Memory-as-a-Tool) exposes memory as a callable function, letting the agent decide when to retrieve context—more sophisticated and cost-efficient.
- **Memory Trust and Provenance**: Provenance tracks a memory's origin and history to establish trustworthiness. Source type (Bootstrapped Data, User Input, Tool Output) determines trust level. Confidence scores injected into prompts let the LLM assess reliability. Confidence increases through corroboration and decreases over time.
- **Memory Retrieval Dimensions**: Advanced memory systems use blended scoring across three dimensions: (1) Relevance (semantic similarity to current context), (2) Recency (how recently created/updated, with decay), and (3) Importance (overall significance, defined during generation). Relying solely on semantic similarity is a common pitfall.
- **Memory Generation: Blocking vs Background**: Memory generation is computationally expensive. Blocking (synchronous) operations force users to wait (discouraged for production). Background (asynchronous) operations send the response first while memory generation runs in parallel—essential for fast, responsive agents.
- **Memory Security**: Memory poisoning (malicious users corrupting persistent knowledge) requires validation tools like Model Armor for sanitization before committing to long-term storage.

### Day 4: Agent Quality

📄 **[View White Paper](White_Papers/Day%204%20-%20Agent%20Quality.pdf)**

**Summary:**
Agent Quality is a continuous discipline that must be integrated from the design phase to build trustworthy AI agents in production. Traditional Quality Assurance fails for non-deterministic agents because failures manifest as subtle degradations (hallucination, bias, concept drift) rather than explicit crashes. The fundamental evaluation unit is the entire system trajectory (Thought → Action → Observation), not just model output. This whitepaper establishes a holistic evaluation framework built on four pillars—Effectiveness (goal achievement), Efficiency (cost and latency), Robustness (handling adversity), and Safety & Alignment (trustworthiness). The foundation is Observability, which provides visibility into the agent's "thought process" through Logs (event diary), Traces (causal narrative), and Metrics (aggregated health scores). Evaluation follows an "Outside-In" hierarchy, starting with Black Box (end-to-end task completion) before Glass Box (full reasoning analysis), judged through a hybrid system of LLM-as-a-Judge automation and Human-in-the-Loop expertise. These practices form the Agent Quality Flywheel, where observed data fuels continuous evaluation, converting every failure into a permanent regression test.

**Key Points:**
- **Four Pillars of Agent Quality**:
  - Effectiveness: black-box measure of successful goal achievement.
  - Efficiency: resources consumed (tokens/cost, latency, trajectory complexity).
  - Robustness: handling real-world adversity (exceptions, ambiguous prompts, API timeouts, retries).
  - Safety & Alignment: operating within ethical boundaries (security against prompt injection, data leakage).
- **Observability Foundation**: Visibility into the agent's "thought process" through three pillars:
  - Logs: timestamped structured entries of events, reasoning steps, tool calls (tells what happened).
  - Traces: narrative thread connecting logs to reveal causal relationships (explains why failures occurred, uses OpenTelemetry).
  - Metrics: quantitative aggregated scores applied to the 4 pillars of Agent Quality:
    - System Metrics: Task Completion Rate, Tool usage frequency, P99 Latency, Error Rate, Tokens per Task, API cost per run.
    - Quality Metrics: Factual Correctness Score, Trajectory Adherence, Helpfulness Ratings, Hallucination Rate.
- **Outside-In Evaluation Hierarchy**: Sampling strategies avoid system overload by logging 100% of failures in Black Box evaluation (which triggers Glass Box analysis), while only sampling a few successful cases.
  - End-to-End (Black Box): assesses final output quality and task success against business KPIs.
  - Trajectory (Glass Box): diagnoses failures by analyzing execution path including LLM planning, tool selection/parameterization, and response interpretation.
- **Evaluation Judges**: LLM-as-a-Judge (powerful model scoring against rubric, uses pairwise comparison for reliable improvement measurement at scale), Agent-as-a-Judge (specialized Critic Agent evaluating full execution trace for plan quality and tool use), and Human-in-the-Loop (HITL—captures qualitative signals, judges nuance, provides domain expertise, creates "Golden Set" evaluation cases).
- **Agent Quality Flywheel**: Self-reinforcing system for continuous improvement where operational data is gathered (Observability), fuels evaluation (LLM/Human Judges), and feedback is converted into permanent regression tests. Core principle: design agents to be "evaluatable-by-design," programmed to emit data for judgment from the start.

### Day 5: Prototype to Production

📄 **[View White Paper](White_Papers/Day%205%20-%20Prototype%20to%20Production.pdf)**

**Summary:**
This white paper tackles the "last mile" production gap—moving agent prototypes into trustworthy, enterprise-grade systems. It introduces AgentOps, a new operational discipline extending DevOps and MLOps for non-deterministic, stateful, autonomous agents. Production relies on three pillars: Automated Evaluation, Automated Deployment (CI/CD), and Comprehensive Observability. Pre-production uses Evaluation-Gated Deployment (automated quality gates block unvalidated versions). In production, a continuous loop (Observe → Act → Evolve) identifies emergent behavior, enables real-time intervention, and converts failures into permanent test cases. Scaling to enterprise fleets requires the Agent2Agent (A2A) protocol for complex, stateful collaboration between agents.

**Key Points:**
- **AgentOps Discipline**: Operational paradigm evolved from DevOps/MLOps for agentic system challenges: dynamic tool orchestration (on-the-fly trajectory assembly), scalable state management (secure session/memory persistence), unpredictable cost/latency. Prototypes take minutes. Production takes 80% of total effort.
- **People and Process**: Production requires coordinated teams. Traditional MLOps needs: Cloud Platform (infrastructure, security), Data Engineering (pipelines, quality), Data Science/MLOps (training, automation), ML Governance (oversight, compliance). GenAI adds: Prompt Engineers (instructions, expected outputs, domain expertise), AI Engineers (production scaling, evaluation, guardrails, RAG/tools). Small companies have generalists. Mature organizations have specialists. Coordination is essential.
- **Evaluation-Gated Deployment**: No agent reaches users without passing quality and safety checks. Mature teams integrate evaluation into CI/CD, automatically blocking deployment when metrics (tool success rate, helpfulness) fall below thresholds.
- **CI/CD Pipeline Structure**: Three-phase funnel catches errors early.
  - Pre-Merge Integration (CI): Fast checks (unit tests, linting, agent evaluation) for immediate feedback.
  - Post-Merge Validation in Staging (CD): Comprehensive tests in staging (load testing, internal dogfooding).
  - Gated Production Deployment: Human sign-off (HITL) required before promotion.
  - Infrastructure as Code (IaC): Terraform for repeatable environments. Secret Manager for runtime secrets.
- **Safe Rollout Strategies**: Gradual deployment minimizes risk: Canary (small user percentage), Blue-Green (instant environment switching), A/B Testing, Feature Flags. Requires rigorous versioning of all artifacts (prompts, code, models, tools, datasets) for instant rollback.
- **Security Defense Layers**: Three-layer defense against agent risks (Prompt Injection, Data Leakage, Memory Poisoning).
  - Policy Definition: System Instructions as core "constitution".
  - Enforcement (Guardrails): Input Filtering (blocks malicious prompts). Output Filtering (checks harmful content/PII).
  - Continuous Assurance: Systematic Red Teaming and RAI testing.
- **Operational Loop: Observe, Act, Evolve**:
  - Observe: Logs (event diary), Traces (causal narrative), Metrics (performance/cost scores).
  - Act: Two categories. System Health: horizontal scaling, async processing, auto-retries, cost/speed/reliability balance. Risk Management: contain (circuit breakers disable tools), triage (HITL investigation), resolve (deploy patch via CI/CD).
  - Evolve: Convert production insights into improvements. Production failures become permanent test cases.
- **Agent2Agent (A2A) Protocol**: Open standard for agent collaboration. JSON Agent Cards advertise capabilities, security, endpoints for discovery. Higher abstraction than MCP. A2A handles complex agent conversations. MCP handles structured tool operations.
- **Interoperability at Scale**: Central Tool Registries (MCP) and Agent Registries (A2A) enable discovery, governance, auditability. Build when managing thousands of tools/agents across teams, not by default. Benefits: developers avoid duplicates, security teams audit access, product owners understand capabilities.

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
