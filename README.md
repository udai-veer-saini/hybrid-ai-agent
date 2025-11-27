Hybrid AI Agent

A combined Troubleshooting + Automation system designed as a college project.
This agent can analyze problems, run diagnostic checks, and trigger automated actions to assist users efficiently.

🔧 Features

<b>Troubleshooter Agent<b>
Identifies common issues, performs system checks, and returns suggestions or fixes.

<b>Automation Agent<b>
Executes background tasks, handles routine operations, and triggers actions based on user requests.

<b>FastAPI Backend<b>
Clean API endpoints for communication between frontend and agents.

<b>Modular Design<b>
Agents, routes, and tools organized in separate modules for easy extension.

🤖 AI Agent (Groq-powered)

Interprets user queries

Understands intent

Decides routing (Troubleshooting vs Automation)

Generates helpful responses

Acts as the cognitive layer of the system

📦 Project Includes

<b>backend/<b> – FastAPI application, agents, tools, routes

<b>frontend/<b> – Simple UI for interacting with the agent

<b>requirements.txt<b> – Python dependencies

🚀 Purpose

Created as a BCA college project to demonstrate a hybrid AI system combining problem-solving intelligence with automated task execution.

🔧 Installation and Setup
Backend Setup (FastAPI)

cd backend

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn app.main:app --reload

🧩 System Architecture (Diagram)
```txt           ┌────────────────────────┐
                 │        Frontend         │
                 │  (User Interaction UI)  │
                 └──────────┬─────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │      FastAPI Backend    │
                 │   (API Gateway Layer)   │
                 └──────────┬─────────────┘
                            │
                            ▼
                 ┌────────────────────────┐
                 │    Groq AI Agent        │
                 │  (LLM Decision Layer)   │
                 └──────────┬─────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
┌──────────────────┐                  ┌───────────────────┐
│ Troubleshooter    │                  │ Automation Agent  │
│ Agent             │                  │ (Task Execution)  │
│ - System checks   │                  │ - Scripts/Actions │
│ - Diagnostics     │                  │ - Background ops  │
└──────────────────┘                  └───────────────────┘
        └───────────────────┬───────────────────┘
                            ▼
                 ┌────────────────────────┐
                 │      Final Output       │
                 │  (Suggestions/Actions)  │
                 └────────────────────────┘
```

🔄 Data Flow 
```txt
User Input
    │
    ▼
AI Agent (Decision Layer)
    │
    ├──► Troubleshooter Module
    │         │
    │         └──► System checks, diagnostics, problem analysis
    │
    └──► Automation Module
              │
              └──► Executes tasks, triggers routines, performs actions

Final Output → structured results returned to frontend
```
🧠 How the Hybrid AI Agent Works (with Groq AI)

1. The user enters a query in natural language through the frontend.

2.The request is sent to the Groq-powered AI Agent, which interprets the intent using LLM intelligence.

3.Based on the intent, the AI decides whether the request belongs to:

4.Troubleshooting Module (system checks, diagnostics), or

5.Automation Module (run tasks, trigger tools).

6.The chosen module performs the required operations.

7.The final structured result is returned to the frontend with explanations.
