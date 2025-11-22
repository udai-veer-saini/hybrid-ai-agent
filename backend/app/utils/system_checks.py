import platform
import psutil

def run_system_diagnostics():
    os_info = platform.platform()
    cpu_usage = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    return (
        f"🖥 OS: {os_info}\n"
        f"⚙ CPU Usage: {cpu_usage}%\n"
        f"💾 RAM Usage: {ram}%\n"
        f"Diagnostics complete."
    )
