from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.post("/callbell/webhook")
async def callbell_webhook(request: Request):
    try:
        body = await request.body()
        payload = json.loads(body) if body else {}
        
        return JSONResponse({
            "result": "DEBUG",
            "payload_received": payload,
            "body_string": body.decode('utf-8') if body else "empty"
        })

    except Exception as e:
        return JSONResponse({
            "result": "ERROR",
            "error": str(e)
        })