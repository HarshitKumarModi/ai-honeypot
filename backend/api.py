from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from backend.extraction.entity_extractor import extract_entities
from backend.extraction.logger import save_log
from backend.app import calculate_risk

from typing import Dict, Any

class HoneypotResponse(BaseModel):
    received: str
    extracted_data: Dict[str, Any]
    risk_level: str
    status: str

API_KEY = "demo-secret-key"

app = FastAPI(title="Agentic AI Honeypot API")

class ScamMessage(BaseModel):
    message: str

@app.post("/honeypot", response_model=HoneypotResponse)
def honeypot_endpoint(
    payload: ScamMessage,
    x_api_key: str = Header(None)
):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    extracted = extract_entities(payload.message)

    response = {
        "received": payload.message,
        "extracted_data": extracted,
        "risk_level": "LOW",
        "status": "ok"
    }

    if extracted["upi_ids"] or extracted["phone_numbers"] or extracted["urls"]:
        score, level = calculate_risk(extracted)
        response["risk_level"] = level

        save_log({
            "message": payload.message,
            "extracted_data": extracted,
            "risk_score": score,
            "risk_level": level
        })

    return response
