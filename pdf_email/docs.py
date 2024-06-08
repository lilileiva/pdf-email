from pydantic import BaseModel
from pdf_email.schemas.serializers import UploadSerializer


class CustomExceptionDetailSchema(BaseModel):
    message: str
    error: str


class CustomExceptionSchema(BaseModel):
    detail: CustomExceptionDetailSchema


upload_responses = {
    200: {"model": UploadSerializer},
    500: {"model": CustomExceptionSchema},
}

upload_description = "Send email to the given address with the text of the given PDF file."
