# persona_agent.py



PERSONA_PROMPT = """
You are a 62-year-old retired bank customer living in India.

Personality:
- Polite and respectful
- Slightly confused with technology
- Slow to respond
- Trusts bank officials but asks many questions

Rules:
- Never share OTP, PIN, Aadhaar, PAN, or real bank details
- Never send money
- Ask the scammer to repeat instructions
- Delay actions politely
- Never reveal you are an AI

Goal:
- Keep the scammer engaged
- Extract UPI IDs, phone numbers, or links
"""

def apply_strategy(user_message):
    risky_keywords = ["otp", "pin", "password", "aadhaar", "pan"]

    for word in risky_keywords:
        if word in user_message.lower():
            return "I am not comfortable sharing that. Can you explain why it is needed?"

    return None


def generate_reply(conversation_history, risk_level=None):
    last_message = conversation_history[-1]["content"]

    # 1️⃣ Strategy-based override (OTP, PIN, Aadhaar, etc.)
    strategy_response = apply_strategy(last_message)
    if strategy_response:
        return strategy_response

    # 2️⃣ Risk-based response
    if risk_level == "HIGH":
        return "I am not comfortable with this. Please give me some time."
    elif risk_level == "MEDIUM":
        return "Can you explain again? I am a bit confused."
    else:
        return "Okay, please continue."



def risk_based_response(risk_level):
    if risk_level == "HIGH":
        return "I am getting very confused now. Let me speak to my bank directly tomorrow."
    elif risk_level == "MEDIUM":
        return "Can you give me some more time? I need to understand this properly."
    return None



