import os
from PyPDF2 import PdfReader
from pdf_email.exceptions import EmailException, PDFException
from pdf_email.services.smtp import SMTPService


def send_file(file, email: str) -> None:
    text = read_pdf(file)
    try:
        service = SMTPService()
        service.send_email(receiver_email=email, subject=str(file.filename), content=text)
    except Exception as e:
        raise EmailException(e)


def read_pdf(file) -> str:
    try:
        tmp_file = f"/tmp/{file.filename}"
        with open(tmp_file, "wb") as f:
            f.write(file.file.read())
        reader = PdfReader(tmp_file)
        total_lines = 0
        content = ""
        for page in reader.pages:
            text = page.extract_text()
            lines = text.split("\n")
            for line in lines:
                total_lines += 1
                content += str(line) + "\n"
                if total_lines >= int(os.getenv("PDF_LINES")):
                    break
        os.remove(tmp_file)
        return content
    except Exception as e:
        raise PDFException(e)
