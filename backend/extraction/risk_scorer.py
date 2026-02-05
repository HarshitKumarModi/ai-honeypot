# backend/extraction/risk_scorer.py

def calculate_risk(extracted_data):
    score = 0

    if extracted_data.get("upi_ids"):
        score += 3

    if extracted_data.get("phone_numbers"):
        score += 2

    if extracted_data.get("urls"):
        score += 3

    if score >= 6:
        return score, "HIGH"
    elif score >= 3:
        return score, "MEDIUM"
    else:
        return score, "LOW"
