import asyncio
from agents.News_Fetch_Agents.newsapi_agent import fetch_newsapi
from agents.News_Fetch_Agents.gnews_agent import fetch_gnews
from agents.News_Fetch_Agents.rss_agent import fetch_rss
from scrapers.scout import run_scout
from agents.summarizer_agent import summarize_news

def run_agentic_pipeline(topic):
    all_articles = []

    # 1. Keep Existing Features: Fetch from traditional APIs and RSS
    all_articles.extend(fetch_newsapi(topic))
    all_articles.extend(fetch_gnews(topic))
    all_articles.extend(fetch_rss(topic))

    # 2. Add New Feature: Fetch from Autonomous Scout
    try:
        scout_data = asyncio.run(run_scout(topic))
        # Add scout findings to the processing list
        all_articles.append({
            "title": f"Scout Verification for {topic}",
            "content": str(scout_data)
        })
    except Exception as e:
        print(f"Scout failed but continuing with APIs: {e}")

    results = []
    for article in all_articles:
        # 3. Enhanced Feature: Audit the content instead of just summarizing
        summary = summarize_news(article["content"])
        results.append({
            "title": article["title"],
            "summary": summary
        })

    return results
