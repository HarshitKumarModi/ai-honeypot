import json
from pathlib import Path

# ALWAYS resolve path relative to THIS file
LOG_FILE = Path(__file__).resolve().parent.parent / "data" / "logs.json"

def save_log(entry):
    if not LOG_FILE.exists():
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        LOG_FILE.write_text("[]")

    data = json.loads(LOG_FILE.read_text())
    data.append(entry)
    LOG_FILE.write_text(json.dumps(data, indent=2))
