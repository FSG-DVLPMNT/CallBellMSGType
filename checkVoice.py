from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.post("/callbell/webhook")
async def callbell_webhook(request: Request):
    try:
        body = await request.body()
        
        if not body:
            return JSONResponse({"result": "UNKNOWN"})
        
        payload = json.loads(body)
        message = payload.get("message")

        if not message:
            return JSONResponse({"result": "UNKNOWN"})

        msg_type = message.get("type", "").lower()

        if msg_type == "text":
            return JSONResponse({"result": "TEXT"})

        if msg_type in ["audio", "voice", "voice_message", "audio_message"]:
            return JSONResponse({"result": "VOICE"})

        return JSONResponse({"result": "OTHER"})

    except Exception as e:
        return JSONResponse({"result": "ERROR"})