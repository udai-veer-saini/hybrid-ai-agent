from app.models.chat_models import ChatResponse
import re

def extract_path(text):
    match = re.search(r"(?:in|at)\s+([A-Za-z0-9_:/\\.\-]+)", text)
    return match.group(1) if match else None


def extract_two_paths(text):
    matches = re.findall(r"(?:from|to)\s+([A-Za-z0-9_:/\\.\-]+)", text)
    return matches if len(matches) >= 2 else (None, None)


def automation_agent_handler(user_input: str) -> ChatResponse:
    text = user_input.lower()

    # ---------------- LIST FILES ----------------
    if "list" in text or "show files" in text:
        p = extract_path(user_input)
        if not p:
            return ChatResponse(
                reply=(
                    "List operation detected.\n"
                    "Please specify a path, for example:\n"
                    "list files in C:/Users/me"
                )
            )
        return ChatResponse(
            reply=(
                "Listing files:\n"
                f"Target path: {p}\n\n"
                f"[ACTION:list] path={p}"
            )
        )

    # ---------------- RENAME ----------------
    if "rename" in text:
        p = extract_path(user_input)
        m = re.search(r"rename\s+([^\s]+)\s+to\s+([^\s]+)", user_input)
        if not (p and m):
            return ChatResponse(
                reply=(
                    "Rename operation detected.\n"
                    "Correct usage:\n"
                    "rename old.txt to new.txt in C:/path"
                )
            )
        old_name, new_name = m.groups()
        return ChatResponse(
            reply=(
                "Rename operation:\n"
                f"- Old name: {old_name}\n"
                f"- New name: {new_name}\n"
                f"- Path: {p}\n\n"
                f"[ACTION:rename] path={p} old={old_name} new={new_name}"
            )
        )

    # ---------------- DELETE ----------------
    if "delete" in text or "remove" in text:
        p = extract_path(user_input)
        if not p:
            return ChatResponse(
                reply=(
                    "Delete operation detected.\n"
                    "Usage example:\n"
                    "delete in C:/path/to/item"
                )
            )
        return ChatResponse(
            reply=(
                "Delete operation:\n"
                f"- Target: {p}\n\n"
                f"[ACTION:delete] path={p}"
            )
        )

    # ---------------- CREATE FOLDER ----------------
    if "create folder" in text or "new folder" in text:
        p = extract_path(user_input)
        m = re.search(r"(?:folder|named)\s+([A-Za-z0-9_\-]+)", user_input)
        if not (p and m):
            return ChatResponse(
                reply=(
                    "Create-folder operation detected.\n"
                    "Usage:\n"
                    "create folder named logs in C:/path"
                )
            )
        folder_name = m.group(1)
        return ChatResponse(
            reply=(
                "Create folder operation:\n"
                f"- Folder name: {folder_name}\n"
                f"- Location: {p}\n\n"
                f"[ACTION:create] path={p} name={folder_name}"
            )
        )

    # ---------------- MOVE ----------------
    if "move" in text:
        src, dst = extract_two_paths(user_input)
        if not (src and dst):
            return ChatResponse(
                reply=(
                    "Move operation detected.\n"
                    "Correct usage:\n"
                    "move from C:/src/file to D:/dst/"
                )
            )
        return ChatResponse(
            reply=(
                "Move operation:\n"
                f"- Source: {src}\n"
                f"- Destination: {dst}\n\n"
                f"[ACTION:move] src={src} dst={dst}"
            )
        )

    # ---------------- DEFAULT HELP ----------------
    return ChatResponse(
        reply=(
            "Automation assistant ready.\n"
            "You can say:\n"
            "- list files in C:/path\n"
            "- rename old.txt to new.txt in C:/path\n"
            "- delete in C:/path\n"
            "- create folder named logs in C:/path\n"
            "- move from C:/source to D:/destination"
        )
    )
