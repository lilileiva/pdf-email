import re
import mimetypes
from dataclasses import dataclass
from fastapi import UploadFile, Form
from pydantic import ValidationError, model_validator


@dataclass
class UploadValidator:
    email: str = Form(..., description="Email address to send mail")
    file: UploadFile = Form(..., description="Email address to send mail")

    @model_validator(mode="before")
    def validate_fields(cls, values):
        email = values.get("email")
        file = values.get("file")
        cls._validate_email(email)
        cls._validate_file(file)
        return values

    def _validate_email(cls, email):
        EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        match = re.fullmatch(EMAIL_REGEX, email)
        if not match:
            raise ValidationError("Invalid email.")

    def _validate_file(cls, file):
        EXTENSIONS = [".pdf"]
        mimetype = mimetypes.guess_extension(file.content_type)
        if mimetype not in EXTENSIONS:
            raise ValidationError("Invalid file. Only PDF format is valid.")
