import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="AI Honeypot Dashboard", layout="wide")

st.title("🕵️ Agentic AI Honeypot – Scam Intelligence Dashboard")

LOG_FILE = Path("backend/data/logs.json")


def load_logs():
    if LOG_FILE.exists():
        return json.loads(LOG_FILE.read_text())
    return []

logs = load_logs()

# 🔎 Risk level filter (ADD HERE)
risk_filter = st.selectbox(
    "Filter by Risk Level",
    ["ALL", "LOW", "MEDIUM", "HIGH"]
)


st.subheader("📊 Intelligence Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Scam Events", len(logs))

with col2:
    high_risk = sum(1 for log in logs if log.get("risk_level") == "HIGH")
    st.metric("High Risk Alerts", high_risk)

with col3:
    unique_upi = set()
    for log in logs:
        unique_upi.update(log["extracted_data"].get("upi_ids", []))
    st.metric("Unique UPI IDs", len(unique_upi))

st.subheader("📁 Extracted Scam Intelligence")

if logs:
    for i, log in enumerate(reversed(logs), start=1):

        # 🔍 APPLY FILTER HERE
        if risk_filter != "ALL" and log["risk_level"] != risk_filter:
            continue

        with st.expander(f"Scam Event {i} | Risk: {log['risk_level']}"):
            st.write("🕒 Timestamp:", log["extracted_data"]["timestamp"])
            st.write("💬 Scammer Message:", log["message"])

            st.write("📌 Extracted Data:")
            st.json(log["extracted_data"])

            st.write("⚠️ Risk Score:", log["risk_score"])
else:
    st.info("No scam intelligence captured yet.")


st.subheader("📤 Export Evidence")

st.download_button(
    label="Download Scam Intelligence Report (JSON)",
    data=json.dumps(logs, indent=2),
    file_name="scam_intelligence_report.json",
    mime="application/json"
)
