import requests
from datetime import datetime, timezone
from urllib.parse import urlencode

def search_serpapi(serp_key: str, queries: list[str], limit: int = 10):
    if not serp_key:
        return []
    results = []
    # Buckets: general, facebook.com, instagram.com
    sites = [None, "facebook.com", "instagram.com"]
    for q in queries:
        for site in sites:
            params = {
                "engine": "google",
                "q": f'{q} {"site:"+site if site else ""}'.strip(),
                "num": 10,
                "api_key": serp_key,
                "hl": "en",
                "tbs": "qdr:d",  # past day
            }
            url = "https://serpapi.com/search.json?" + urlencode(params)
            try:
                resp = requests.get(url, timeout=30)
                data = resp.json()
            except Exception:
                continue
            for item in (data.get("organic_results") or []):
                link = item.get("link")
                title = item.get("title") or link
                snippet = item.get("snippet") or ""
                created_utc = datetime.now(timezone.utc)  # qdr:d ensures last day
                results.append({
                    "id": f"google::{link}",
                    "title": title,
                    "url": link,
                    "text": f"{title} {snippet}",
                    "created_utc": created_utc,
                    "source": f"Google{'/' + site if site else ''}"
                })
                if len(results) >= limit:
                    break
            if len(results) >= limit:
                break
    return results
