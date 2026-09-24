from config import TOPICS
from fetch_news import fetch_all_articles
from filter_news import process_articles
from digest import save_digest, format_digest, format_digest_html, save_digest_html
from llm_summary import summarize_articles, save_llm_summary
if __name__ == "__main__":
    raw = fetch_all_articles(TOPICS)
    filtered = process_articles(raw)
    formated = format_digest(filtered)
    path = save_digest(formated)
    

    print(f"Digest saved to {path}")

    summary = summarize_articles(filtered)
    save_llm_summary(summary)

    html_content = format_digest_html(filtered)
    html_path = save_digest_html(html_content)
    print(f"HTML saved to {html_path}")