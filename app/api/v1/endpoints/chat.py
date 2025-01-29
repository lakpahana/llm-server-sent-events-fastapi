from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.services.llm_service import openai_stream

chat_router = APIRouter()

@chat_router.get("/")
async def chat_stream(prompt: str):
    return StreamingResponse(openai_stream(prompt), media_type="text/event-stream")