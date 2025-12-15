from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

@app.post("/callbell/webhook")
async def callbell_webhook(request: Request):
    try:
        payload = await request.json()
        
        # Callbell puede enviar diferentes estructuras
        # Intenta diferentes caminos
        message = (
            payload.get("message") or 
            payload.get("data", {}).get("message") or
            payload
        )

        msg_type = message.get("type", "").lower()

        if msg_type == "text":
            return {"result": "TEXT"}

        if msg_type in ["audio", "voice"]:
            return {"result": "VOICE"}

        return {"result": "OTHER"}

    except Exception as e:
        return {"result": "ERROR", "error": str(e)}