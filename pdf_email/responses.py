UPLOAD_RESPONSE = {
    200: {"success": True, "message": "The email has been successfully sent to example@example.com"},
    400: {"detail": {"message": "", "error": ""}},
    500: {"detail": {"message": "", "error": ""}},
}

upload_responses = {200: UPLOAD_RESPONSE[200], 400: UPLOAD_RESPONSE[400], 500: UPLOAD_RESPONSE[500]}
