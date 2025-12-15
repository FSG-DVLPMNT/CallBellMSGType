from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Message(BaseModel):
    type: str
    text: Optional[str] = None

class WebhookPayload(BaseModel):
    message: Optional[Message] = None

@app.post("/callbell/webhook")
async def callbell_webhook(payload: WebhookPayload):
    try:
        if not payload.message:
            return {"result": "UNKNOWN"}

        result = "OTHER"

        if payload.message.type == "text":
            result = "TEXT"

        if payload.message.type == "audio":
            result = "VOICE"

        return {"result": result}

    except Exception:
        return {"result": "ERROR"}
