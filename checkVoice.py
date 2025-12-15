from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/callbell/webhook")
async def callbell_webhook(request: Request):
    debug_info = {}
    
    try:
        body = await request.body()
        debug_info["raw_body"] = body.decode('utf-8')[:500]  # Primeros 500 chars
        
        payload = json.loads(body)
        debug_info["payload_keys"] = list(payload.keys())
        
        message = payload.get("message")
        debug_info["has_message"] = message is not None
        
        if message:
            debug_info["message_keys"] = list(message.keys()) if isinstance(message, dict) else "not_a_dict"
            debug_info["message_type"] = message.get("type") if isinstance(message, dict) else None

        if not message:
            return {"result": "UNKNOWN", "debug": debug_info}

        msg_type = message.get("type")

        if msg_type == "text":
            return {"result": "TEXT", "debug": debug_info}

        if msg_type == "audio":
            return {"result": "VOICE", "debug": debug_info}

        return {"result": "OTHER", "debug": debug_info}

    except Exception as e:
        debug_info["error"] = str(e)
        debug_info["error_type"] = type(e).__name__
        return {"result": "ERROR", "debug": debug_info}