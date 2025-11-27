# backend/app/utils/automation_tools.py
import os

def rename_files_in_folder(path="demo_folder"):
    if not os.path.exists(path):
        return "Folder not found."

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if not files:
        return "No files to rename."

    renamed = 0
    for i, filename in enumerate(files):
        old = os.path.join(path, filename)
        # keep original extension
        name, ext = os.path.splitext(filename)
        new = os.path.join(path, f"renamed_{i}{ext}")
        try:
            os.rename(old, new)
            renamed += 1
        except Exception:
            continue

    return f"Renamed {renamed} files in {path}"
