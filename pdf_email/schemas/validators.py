import re
import mimetypes
from fastapi import UploadFile, Form
from pydantic import BaseModel, Field, model_validator

from pdf_email.exceptions import EmailException, PDFException


class UploadValidator(BaseModel):
    email: str = Field(..., description="Email address to send mail")
    file: UploadFile = Form(..., description="Email address to send mail")

    @model_validator(mode="before")
    def validate_fields(cls, values) -> dict:
        email = values.get("email")
        file = values.get("file")
        validated_email = _validate_email(email)
        if not validated_email:
            raise EmailException("Invalid email.")
        validated_file = _validate_file(file)
        if not validated_file:
            raise PDFException("Invalid file. Only PDF format is valid.")
        return values


def _validate_email(email) -> bool:
    EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    match = re.fullmatch(EMAIL_REGEX, email)
    return match is not None


def _validate_file(file) -> bool:
    EXTENSIONS = [".pdf"]
    mimetype = mimetypes.guess_extension(file.content_type)
    return mimetype in EXTENSIONS
