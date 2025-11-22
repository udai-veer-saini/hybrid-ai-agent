import os

def rename_files_in_folder(path="demo_folder"):
    if not os.path.exists(path):
        return "Folder not found."

    files = os.listdir(path)

    for i, filename in enumerate(files):
        old = os.path.join(path, filename)
        new = os.path.join(path, f"renamed_{i}.txt")
        os.rename(old, new)

    return f"Renamed {len(files)} files in {path}"
