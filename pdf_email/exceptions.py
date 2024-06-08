from fastapi import HTTPException


class CustomException(HTTPException):
    """Custom exception"""

    def __init__(self, status_code: int, message: str, error: str):
        return super().__init__(status_code=status_code, detail={"message": message, "error": error})


class PDFException(CustomException):
    """Exception raised when PDF file could not be read"""

    def __init__(self, error: str | Exception):
        return super().__init__(status_code=500, message="Error trying to read PDF file.", error=str(error))


class EmailException(CustomException):
    """Exception raised when email could not be sent"""

    def __init__(self, error: str | Exception):
        return super().__init__(status_code=500, message="Error trying to sent email.", error=str(error))
