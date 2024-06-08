from fastapi import FastAPI
from pdf_email.router import router


app = FastAPI()


app.include_router(router)
