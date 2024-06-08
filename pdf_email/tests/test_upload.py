from fastapi.testclient import TestClient
from pdf_email.main import app
from unittest.mock import patch
from pdf_email.services.smtp import SMTPService

client = TestClient(app)


def test_upload_success():
    url = "/upload"
    file = open("pdf_email/tests/test.pdf", "rb")
    email = "test@mail.com"
    with patch.object(SMTPService, "send_email", return_value=None) as mock:
        response = client.post(
            url=url, data={"email": email}, files={"file": file}, headers={"contentType": "multipart/form-data"}
        )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "The email has been successfully sent to test@mail.com"
    assert mock.called is True


def test_upload_invalid_email():
    url = "/upload"
    file = open("pdf_email/tests/test.pdf", "rb")
    email = "invalid_email"
    response = client.post(
        url=url, data={"email": email}, files={"file": file}, headers={"contentType": "multipart/form-data"}
    )
    assert response.status_code == 500
    assert response.json()["detail"]["message"] == "Error trying to sent email."
    assert response.json()["detail"]["error"] == "Invalid email."


def test_upload_invalid_file():
    url = "/upload"
    file = open("pdf_email/tests/test.jpg", "rb")
    email = "test@mail.com"
    response = client.post(
        url=url, data={"email": email}, files={"file": file}, headers={"contentType": "multipart/form-data"}
    )
    assert response.status_code == 500
    assert response.json()["detail"]["message"] == "Error trying to read PDF file."
    assert response.json()["detail"]["error"] == "Invalid file. Only PDF format is valid."
