from app.utils.system_checks import run_system_diagnostics
from app.models.chat_models import ChatResponse

def system_agent_handler(user_input: str) -> ChatResponse:
    result = run_system_diagnostics()
    return ChatResponse(
        reply=f"🔍 Running system diagnostics...\n\n{result}"
    )
