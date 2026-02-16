import feedparser

RSS_SOURCES = [
    "https://rss.cnn.com/rss/edition.rss",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.theguardian.com/world/rss"
]

def fetch_rss(topic, limit=5):
    articles = []

    for source in RSS_SOURCES:
        feed = feedparser.parse(source)

        for entry in feed.entries:
            if topic.lower() in entry.title.lower():
                articles.append({
                    "title": entry.title,
                    "content": entry.get("summary", "")
                })

            if len(articles) >= limit:
                break

    return articles
