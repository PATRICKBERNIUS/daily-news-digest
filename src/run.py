from config import TOPICS
from fetch_news import fetch_all_articles
from filter_news import process_articles
from digest import save_digest, format_digest

if __name__ == "__main__":
    raw = fetch_all_articles(TOPICS)
    filtered = process_articles(raw)
    formated = format_digest(filtered)
    path = save_digest(formated)

    print(f"Digest saved to {path}")