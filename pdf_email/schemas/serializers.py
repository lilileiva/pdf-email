from pydantic import BaseModel, Field


class UploadSerializer(BaseModel):
    success: bool = Field(..., description="Indicates if upload was successful or not")
    message: str = Field(..., description="Response message")
