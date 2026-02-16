from agents.News_Fetch_Agents.newsapi_agent import fetch_newsapi
from agents.News_Fetch_Agents.gnews_agent import fetch_gnews
from agents.News_Fetch_Agents.rss_agent import fetch_rss
from agents.summarizer_agent import summarize_news

def run_agentic_pipeline(topic):
    all_articles = []

    # Fetch from multiple agents
    all_articles.extend(fetch_newsapi(topic))
    all_articles.extend(fetch_gnews(topic))
    all_articles.extend(fetch_rss(topic))

    results = []

    for article in all_articles:
        summary = summarize_news(article["content"])
        results.append({
            "title": article["title"],
            "summary": summary
        })

    return results


# Old version

# from agents.news_fetch_agent import fetch_news
# from agents.summarizer_agent import summarize_news

# def run_agentic_pipeline(topic):
#     news = fetch_news(topic)
#     final_output = []

#     for article in news:
#         summary = summarize_news(article["content"])
#         final_output.append({
#             "title": article["title"],
#             "summary": summary
#         })

#     return final_output