from fastapi import APIRouter
from pydantic import BaseModel
import os
import shutil

router = APIRouter(prefix="/automation", tags=["Automation Tools"])

# ---------------------- MODELS ----------------------
class ListRequest(BaseModel):
    path: str
    confirm: bool = False


class RenameRequest(BaseModel):
    path: str
    old_name: str
    new_name: str
    confirm: bool = False


class DeleteRequest(BaseModel):
    path: str
    confirm: bool = False


class CreateFolderRequest(BaseModel):
    path: str
    folder_name: str
    confirm: bool = False


class MoveRequest(BaseModel):
    source: str
    destination: str
    confirm: bool = False


# ---------------------- ENDPOINTS ----------------------
@router.post("/list")
def list_files(req: ListRequest):
    if not req.confirm:
        return {
            "warning": "This action can access sensitive folders.",
            "instruction": 'Add "confirm": true to proceed.'
        }

    if not os.path.exists(req.path):
        return {"error": "Path not found"}
    try:
        return {"files": os.listdir(req.path)}
    except Exception as e:
        return {"error": str(e)}


@router.post("/rename")
def rename_file(req: RenameRequest):
    if not req.confirm:
        return {
            "warning": "This action will rename a file.",
            "instruction": 'Add "confirm": true to proceed.'
        }

    old_path = os.path.join(req.path, req.old_name)
    new_path = os.path.join(req.path, req.new_name)

    if not os.path.exists(old_path):
        return {"error": "Original file does not exist"}

    try:
        os.rename(old_path, new_path)
        return {"message": "Rename successful"}
    except Exception as e:
        return {"error": str(e)}


@router.post("/delete")
def delete_item(req: DeleteRequest):
    if not req.confirm:
        return {
            "warning": "This action will DELETE files or folders permanently.",
            "instruction": 'Add "confirm": true to proceed.'
        }

    if not os.path.exists(req.path):
        return {"error": "File or folder not found"}

    try:
        if os.path.isfile(req.path):
            os.remove(req.path)
        else:
            shutil.rmtree(req.path)
        return {"message": "Deleted successfully"}
    except Exception as e:
        return {"error": str(e)}


@router.post("/create-folder")
def create_folder(req: CreateFolderRequest):
    if not req.confirm:
        return {
            "warning": "This action will create a new folder.",
            "instruction": 'Add "confirm": true to proceed.'
        }

    target = os.path.join(req.path, req.folder_name)
    try:
        if not os.path.exists(req.path):
            return {"error": "Base path not found"}
        if os.path.exists(target):
            return {"error": "Folder already exists"}
        os.makedirs(target, exist_ok=False)
        return {"message": f"Created folder: {target}"}
    except Exception as e:
        return {"error": str(e)}


@router.post("/move")
def move_item(req: MoveRequest):
    if not req.confirm:
        return {
            "warning": "This action will MOVE files and change structure.",
            "instruction": 'Add "confirm": true to proceed.'
        }

    if not os.path.exists(req.source):
        return {"error": "Source not found"}
    try:
        dest_dir = os.path.dirname(req.destination)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
        shutil.move(req.source, req.destination)
        return {"message": "Move successful"}
    except Exception as e:
        return {"error": str(e)}
