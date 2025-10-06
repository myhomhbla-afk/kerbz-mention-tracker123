from datetime import datetime, timezone
import praw

def search_reddit(creds: dict, queries: list[str], limit: int = 10):
    # If creds missing, skip reddit quietly
    if not creds.get("client_id") or not creds.get("client_secret") or not creds.get("user_agent"):
        return []

    try:
        reddit = praw.Reddit(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            user_agent=creds["user_agent"],
            check_for_async=False
        )
        reddit.read_only = True
    except Exception:
        # Auth/connect issue -> skip reddit so workflow still passes
        return []

    results = []
    for q in queries:
        try:
            for submission in reddit.subreddit("all").search(q, sort="new", time_filter="day", limit=limit):
                created_utc = datetime.fromtimestamp(submission.created_utc, tz=timezone.utc)
                text = (submission.title or "") + " " + (submission.selftext or "")
                results.append({
                    "id": f"reddit::{submission.id}",
                    "title": submission.title or "(untitled)",
                    "url": "https://www.reddit.com" + submission.permalink,
                    "text": text,
                    "created_utc": created_utc,
                    "source": "Reddit",
                })
        except Exception:
            continue
    return results
