from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

def fetch_news(topic="technology"):
    articles = newsapi.get_everything(
        q=topic,
        language='en',
        sort_by='publishedAt',
        page_size=5
    )

    news_list = []
    for article in articles['articles']:
        news_list.append({
            "title": article['title'],
            "content": article['description']
        })

    return news_list
