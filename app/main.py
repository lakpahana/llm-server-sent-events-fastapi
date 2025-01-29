from fastapi import FastAPI
from app.api.v1.endpoints.chat import chat_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()
app.include_router(chat_router, prefix="/chat", tags=["chat"])

@app.get("/")
def home():
    return {"message": "LLM SSE FastAPI server is running!"}


