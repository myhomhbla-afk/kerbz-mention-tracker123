import os

CONFIG = {
    "discord_webhook": os.getenv("DISCORD_WEBHOOK", ""),
    "serpapi_key": os.getenv("SERPAPI_KEY", ""),
    "reddit": {
        "client_id": os.getenv("REDDIT_CLIENT_ID", ""),
        "client_secret": os.getenv("REDDIT_CLIENT_SECRET", ""),
        "user_agent": os.getenv("REDDIT_USER_AGENT", "kerbz-mention-tracker/0.2"),
    },
    "timezone": os.getenv("TIMEZONE", "America/New_York"),
    # Search terms
    "queries": [
        '"Kerbz"', '"Kerbz Adventures"', '"@kerbzadventures"'
    ],
    # Hard filters to exclude false positives
    "exclude_phrases": [
        "Kerbal Space Program", "Loyal beyond blood", "Kerbz Xtatik"
    ],
    # How many results per provider per run
    "limit_per_source": 20,
}
