from fastapi import FastAPI
from routes.register import register

app = FastAPI()

app.include_router(register)