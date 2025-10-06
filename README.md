# Kerbz Mention Tracker123 (Daily)

Daily tracker for **Kerbz / @kerbzadventures** mentions across:
- **Google Search** (including `site:facebook.com` and `site:instagram.com`)
- **Reddit**

## Behavior
- Runs **once per day at 9:00 AM America/New_York**.
- Fetches results from the **last 24 hours**.
- Posts a **single summary** to your Discord channel.
- **Skips** anything already posted (tracked in `data/seen.json`).
- **Excludes** false positives containing: **Kerbal Space Program**, **Loyal beyond blood**, **Kerbz Xtatik**.

## Setup
1. Create a new GitHub repository named **kerbz-mention-tracker123**.
2. Add repository secrets (Settings → Secrets and variables → Actions):
   - `DISCORD_WEBHOOK` — Discord channel webhook URL
   - `SERPAPI_KEY` — from https://serpapi.com
   - `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USER_AGENT` — create an app at https://www.reddit.com/prefs/apps
3. Ensure GitHub Actions are enabled. The workflow will run daily or on **Run workflow**.

## Customize
- Edit `src/config.py` → `queries`, `exclude_phrases`, and `limit_per_source`.
