from app.models.chat_models import ChatResponse
import platform
import psutil
import shutil

def system_agent_handler(user_input: str) -> ChatResponse:
    try:
        os_name = platform.system()
        os_version = platform.release()

        cpu = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory().percent

        # disk usage
        total, used, free = shutil.disk_usage("/")

        total_gb = round(total / (1024**3), 2)
        used_gb = round(used / (1024**3), 2)
        free_gb = round(free / (1024**3), 2)

        report = (
            "System Diagnostics Report\n"
            "------------------------\n"
            f"Operating System: {os_name} {os_version}\n"
            f"CPU Usage: {cpu}%\n"
            f"RAM Usage: {ram}%\n"
            f"Disk Total: {total_gb} GB\n"
            f"Disk Used: {used_gb} GB\n"
            f"Disk Free: {free_gb} GB\n\n"
            "If you want a deeper analysis, specify what area you want to inspect."
        )

        return ChatResponse(reply=report)

    except Exception as e:
        return ChatResponse(reply=f"System agent error: {e}")
