from fastapi import HTTPException


class PDFException(HTTPException):
    """Exception raised when PDF file could not be read"""

    def __init__(self, error: str):
        return super().__init__(
            status_code=500, detail={"message": "Error trying to read PDF file.", "error": str(error)}
        )


class EmailException(HTTPException):
    """Exception raised when email could not be sent"""

    def __init__(self, error: str):
        return super().__init__(status_code=500, detail={"message": "Error trying to sent email.", "error": str(error)})
