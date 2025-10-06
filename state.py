import json
from pathlib import Path

STATE_PATH = Path("data/seen.json")
STATE_PATH.parent.mkdir(parents=True, exist_ok=True)

def load_seen():
    if STATE_PATH.exists():
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            try:
                return set(json.load(f))
            except Exception:
                return set()
    return set()

def save_seen(seen_ids: set):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(list(seen_ids)), f, ensure_ascii=False, indent=2)
