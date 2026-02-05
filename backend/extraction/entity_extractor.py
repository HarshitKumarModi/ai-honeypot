import re
from datetime import datetime

UPI_PATTERN = r"[a-zA-Z0-9._-]+@[a-zA-Z]+"
PHONE_PATTERN = r"\b[6-9]\d{9}\b"
URL_PATTERN = r"https?://\S+"

def extract_entities(message: str):
    return {
        "upi_ids": re.findall(UPI_PATTERN, message),
        "phone_numbers": re.findall(PHONE_PATTERN, message),
        "urls": re.findall(URL_PATTERN, message),
        "timestamp": datetime.now().isoformat()
    }
