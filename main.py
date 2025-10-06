from datetime import datetime
from pathlib import Path
import sys
from dateutil import tz

# make src importable when run in GitHub Actions
sys.path.append(str(Path(__file__).resolve().parent))

from config import CONFIG
from state import load_seen, save_seen
from filters import is_excluded, has_kerbz_keyword, is_within_last_day
from discord_client import post_daily_summary
from providers.google_serpapi import search_serpapi
from providers.reddit_praw import search_reddit

def run():
    seen = load_seen()

    # Collect from providers
    items = []
    items += search_serpapi(CONFIG["serpapi_key"], CONFIG["queries"], limit=CONFIG["limit_per_source"])
    items += search_reddit(CONFIG["reddit"], CONFIG["queries"], limit=CONFIG["limit_per_source"])

    # Filter + dedupe
    dedup = {}
    for it in items:
        if it["id"] in dedup or it["id"] in seen:
            continue
        text_blob = (it.get("title","") + " " + it.get("text","")).strip()
        if not has_kerbz_keyword(text_blob):
            continue
        if is_excluded(text_blob, CONFIG["exclude_phrases"]):
            continue
        if not is_within_last_day(it["created_utc"], CONFIG["timezone"]):
            continue
        dedup[it["id"]] = it

    final_items = list(dedup.values())
    final_items.sort(key=lambda x: x.get("created_utc"))

    # Post a single daily summary (this workflow runs once a day)
    tzinfo = tz.gettz(CONFIG["timezone"])
    today_str = datetime.now(tzinfo).strftime("%Y-%m-%d")
    header = f"**Daily Kerbz Mentions — {today_str}**"
    post_daily_summary(CONFIG["discord_webhook"], final_items, header)

    # Mark seen
    seen.update([it["id"] for it in final_items])
    save_seen(seen)

if __name__ == "__main__":
    run()
