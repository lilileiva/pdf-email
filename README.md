# PDF Email

Send emails to the given address extracting text of a PDF file.

Github: https://github.com/lilileiva/pdf-email

## Steps to run app

### 1. Obtain Mailtrap credentials

- Register to Mailtrap
- Go to Sending Domains (https://mailtrap.io/sending/domains)
- Click to the desire domain (deafult: demomailtrap.com)
- Copy SMTP credentials: Host, Port, Username, Password

### 2. Set enviroment variables

- Create .env file in the root of the project
- Fill .env file as follow:

```

MAILTRAP_HOST=<Your Mailtrap host>
MAILTRAP_PORT=<Your Mailtrap port>
MAILTRAP_PASSWORD=<Your Mailtrap password>
MAILTRAP_USER=<Your Mailtrap username>
MAILTRAP_SENDER=<optional>@demomailtrap.com (if default domain is set)
PDF_LINES=<Number of lines to extract from PDF>

```

#### Notes:
- Mailtrap free trial only allows to sent emails to the address you registered with
- Default registered domain is "demomailtrap.com" (used in MAILTRAP_SENDER)

### 3. Install and run project

#### Using Docker

- docker-compose build
- docker-compose up

#### With virtual enviroment

- python -m venv venv
- cd venv/Scripts/activate
- pip install -r requirements.txt
- fastapi run pdf_email/main.py --port 8080

## Run tests

All tests:

```

python -m pytest

```

Specific test:

```

python -m pytest -k 'specific_test_name'

```

## Docs

- localhost:8080/docs
