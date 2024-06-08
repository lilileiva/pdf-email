from fastapi import APIRouter, Depends
from pdf_email.schemas.serializers import UploadSerializer
from pdf_email.schemas.validators import UploadValidator
from pdf_email.responses import upload_responses

from pdf_email.utils import send_file

router = APIRouter()


@router.post("/upload", tags=["upload"], responses=upload_responses)
async def upload_file(body: UploadValidator = Depends()):
    email = body.email
    file = body.file
    send_file(file, email)
    response = {"success": True, "message": f"The email has been successfully sent to {email}"}
    validated_response = UploadSerializer.model_validate(response)
    response = validated_response.model_dump()
    return response
