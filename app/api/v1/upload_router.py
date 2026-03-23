from fastapi import APIRouter, UploadFile, File
from app.services.storage_service import upload_file

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()

    upload_file(file.filename, data)

    return {"message": "uploaded"}
