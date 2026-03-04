import requests
import os

def fetch_newsapi(topic=None, category=None, limit=5):
    api_key = os.getenv("NEWSAPI_KEY")
    
    # Existing search feature + New Category/Genre feature
    if category:
        url = "https://newsapi.org/v2/top-headlines"
        params = {"category": category.lower(), "language": "en", "pageSize": limit, "apiKey": api_key}
    else:
        url = "https://newsapi.org/v2/everything"
        params = {"q": topic, "language": "en", "pageSize": limit, "apiKey": api_key}

    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    if data.get("articles"):
        for item in data["articles"]:
            articles.append({
                "title": item["title"],
                "content": item["description"] or "No description available."
            })
    return articles
