from fastapi import APIRouter, File, Form, UploadFile, Response
from pdf_email.schemas.serializers import UploadSerializer
from pdf_email.schemas.validators import UploadValidator
from pdf_email.responses import upload_responses
from pdf_email.utils import send_file

router = APIRouter()


@router.post("/upload", tags=["upload"], responses=upload_responses)
async def upload_file(email: str = Form(...), file: UploadFile = File(...)) -> UploadSerializer:
    body = {"email": email, "file": file}
    validated_fields = UploadValidator(**body).model_dump()
    email = validated_fields["email"]
    file = validated_fields["file"]
    send_file(file, email)
    response = {"success": True, "message": f"The email has been successfully sent to {email}"}
    validated_response = UploadSerializer.model_validate(response)
    return validated_response
