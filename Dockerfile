FROM python:3.11-alpine

RUN apk update

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8080

CMD [ "fastapi", "run", "./pdf_email/main.py", "--port", "8080"]