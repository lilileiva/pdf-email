UPLOAD_RESPONSE = {
    200: {"success": True, "message": "The email has been successfully sent to example@example.com"},
    500: {"detail": {"message": "", "error": ""}},
}

upload_responses = {200: UPLOAD_RESPONSE[200], 500: UPLOAD_RESPONSE[500]}
