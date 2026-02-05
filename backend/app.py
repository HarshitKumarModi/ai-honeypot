from backend.agents.persona_agent import generate_reply
from backend.extraction.entity_extractor import extract_entities
from backend.extraction.logger import save_log

from backend.scam_detector import is_scam



from backend.extraction.risk_scorer import calculate_risk




def activate_honeypot():
    print("\n🧠 AI Honeypot Activated")
    print("Type 'exit' to stop the conversation.\n")

    conversation_history = []

    current_risk_level = None


    while True:
        scammer_message = input("Scammer: ")
        if scammer_message.lower() == "exit":
            break

        # Store conversation
        conversation_history.append(
            {"role": "user", "content": scammer_message}
        )

        # 🔍 Extract entities
        extracted = extract_entities(scammer_message)
        print("DEBUG extracted =", extracted)

        # ✅ Save ONLY if something is detected
        if extracted["upi_ids"] or extracted["phone_numbers"] or extracted["urls"]:
            score, level = calculate_risk(extracted)

            current_risk_level = level

            print("DEBUG save_log CALLED")

            save_log({
                "message": scammer_message,
                "extracted_data": extracted,
                "risk_score": score,
                "risk_level": level
            })

            print(f"⚠️ Scam intelligence captured | Risk: {level}")

        # 🤖 AI reply (fallback or LLM)
        ai_reply = generate_reply(conversation_history)
        print(f"AI: {ai_reply}\n")

        conversation_history.append(
            {"role": "assistant", "content": ai_reply}
        )



if __name__ == "__main__":
    user_message = input("Paste suspicious message: ")

    if is_scam(user_message):
        print("\n⚠️ Scam detected!")
        choice = input("Type 'handover' to hand over to AI: ")

        if choice.lower() == "handover":
            activate_honeypot()
    else:
        print("Message seems safe.")
