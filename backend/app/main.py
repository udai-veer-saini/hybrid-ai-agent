from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.chat_models import ChatRequest, ChatResponse
from app.agents.system_agent import system_agent_handler
from app.agents.automation_agent import automation_agent_handler

app = FastAPI(title="Hybrid AI Agent Backend")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Backend Running", "agent": "Hybrid AI Agent"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    """
    Route that decides whether to use system tools,
    automation tools, or forward to Flowise agent.
    """
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
