from agents.news_fetch_agent import fetch_news
from agents.summarizer_agent import summarize_news

def run_agentic_pipeline(topic):
    news = fetch_news(topic)
    final_output = []

    for article in news:
        summary = summarize_news(article["content"])
        final_output.append({
            "title": article["title"],
            "summary": summary
        })

    return final_output
