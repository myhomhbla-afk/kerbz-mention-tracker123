import re
from datetime import datetime, timedelta
from dateutil import tz

def is_excluded(text: str, exclude_phrases: list[str]) -> bool:
    t = (text or "").lower()
    for phrase in exclude_phrases:
        if phrase.lower() in t:
            return True
    return False

def has_kerbz_keyword(text: str) -> bool:
    return bool(re.search(r'\bkerbz\b', text or "", re.IGNORECASE)) or            '@kerbzadventures' in (text or "").lower() or            'kerbz adventures' in (text or "").lower()

def is_within_last_day(dt_utc: datetime, tz_name: str) -> bool:
    tzinfo = tz.gettz(tz_name)
    local = dt_utc.astimezone(tzinfo)
    now_local = datetime.now(tzinfo)
    delta = now_local - local
    return delta.total_seconds() <= 24*3600 + 60  # small buffer
