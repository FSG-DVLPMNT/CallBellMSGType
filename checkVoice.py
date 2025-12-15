from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/callbell/webhook")
async def callbell_webhook(request: Request):
    try:
        payload = await request.json()
        message = payload.get("message")

        if not message:
            return {"result": "UNKNOWN"}

        msg_type = message.get("type")

        if msg_type == "text":
            return {"result": "TEXT"}

        if msg_type == "audio":
            return {"result": "VOICE"}

        return {"result": "OTHER"}

    except Exception:
        return {"result": "ERROR"}
