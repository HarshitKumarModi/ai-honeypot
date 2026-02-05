# scam_detector.py

SCAM_KEYWORDS = [
    "urgent",
    "kyc",
    "otp",
    "account blocked",
    "verify now",
    "refund",
    "suspended",
    "bank update"
]

def is_scam(message: str) -> bool:
    message = message.lower()
    for keyword in SCAM_KEYWORDS:
        if keyword in message:
            return True
    return False
