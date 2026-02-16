import requests
import os

def fetch_newsapi(topic, limit=5):
    api_key = os.getenv("NEWSAPI_KEY")
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": topic,
        "language": "en",
        "pageSize": limit,
        "apiKey": api_key
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
