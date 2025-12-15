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
        
        # Lee directamente del payload
        msg_type = payload.get("type", "").lower()
        
        # También intenta leer de message.type por si acaso
        if not msg_type:
            message = payload.get("message", {})
            msg_type = message.get("type", "").lower()

        print(f"Tipo recibido: '{msg_type}'")

        if msg_type == "text":
            return JSONResponse({"result": "TEXT"})

        if msg_type in ["audio", "voice", "voice_message", "ptt"]:
            return JSONResponse({"result": "VOICE"})

        return JSONResponse({"result": "OTHER", "debug": {"received_type": msg_type}})

    except Exception as e:
        return JSONResponse({"result": "ERROR"})