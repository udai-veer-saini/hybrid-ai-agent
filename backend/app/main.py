# backend/app/main.py
from app.agents.groq_agent import groq_agent_handler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.chat_models import ChatRequest, ChatResponse
from app.agents.system_agent import system_agent_handler
from app.agents.automation_agent import automation_agent_handler
from app.routes.automation import router as automation_router

app = FastAPI(title="Hybrid AI Agent Backend")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include automation router
app.include_router(automation_router)

@app.get("/")
def home():
    return {"status": "Backend Running", "agent": "Hybrid AI Agent"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    original = payload.message
    text = original.lower()

    # System diagnostics routing
    if any(k in text for k in ["diagnose", "system", "cpu", "ram", "performance"]):
        return system_agent_handler(original)

    # Automation routing
    if any(k in text for k in ["rename", "delete", "move", "folder", "file", "directory"]):
        return automation_agent_handler(original)

    # Fallback: Groq LLM
    return groq_agent_handler(original)

    message = payload.message.lower()

    if "network" in message or "slow" in message or "diagnose" in message:
        return system_agent_handler(message)

    if "rename" in message or "folder" in message or "automation" in message:
        return automation_agent_handler(message)

    return ChatResponse(
        reply="I am not sure which mode to use. You can say things like:\n"
              "- Diagnose my system\n"
              "- Fix network issues\n"
              "- Rename files\n"
    )
