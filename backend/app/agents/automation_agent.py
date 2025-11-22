from app.utils.automation_tools import rename_files_in_folder
from app.models.chat_models import ChatResponse

def automation_agent_handler(user_input: str) -> ChatResponse:
    # Demo logic – detects rename task
    if "rename" in user_input:
        output = rename_files_in_folder()
        return ChatResponse(reply=output)

    return ChatResponse(reply="Automation tool ready! Say:\n- Rename files\n- Organize folders\n")
