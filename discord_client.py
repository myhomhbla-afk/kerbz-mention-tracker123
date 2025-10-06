import requests

def post_to_discord(webhook_url: str, title: str, url: str, source: str):
    if not webhook_url:
        return
    content = f"**Kerbz mention** ({source})\n**{title}**\n<{url}>"
    requests.post(webhook_url, json={"content": content}, timeout=20)

def post_daily_summary(webhook_url: str, items: list, header: str):
    if not webhook_url or not items:
        return
    lines = [header]
    for it in items:
        lines.append(f"- ({it['source']}) **{it['title']}**\n  <{it['url']}>")
    body = "\n".join(lines)
    # keep message size reasonable
    requests.post(webhook_url, json={"content": body[:1900]}, timeout=20)
