import requests
import os

def fetch_gnews(topic, limit=5):
    api_key = os.getenv("GNEWS_KEY")
    url = "https://gnews.io/api/v4/search"

    params = {
        "q": topic,
        "lang": "en",
        "max": limit,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if data.get("articles"):
        for item in data["articles"]:
            articles.append({
                "title": item["title"],
                "content": item["description"] or ""
            })

    return articles
