import os
from datetime import datetime


def format_digest(articles):

    header = f"Daily News Updates - {datetime.now().strftime('%Y%m%d')}"

    entries = []

    for article in articles:

        entry = f"""## {article.get("title")}
        *{article.get("source", {}).get("name")}*
        {article.get("description")}
        [Read more]({article.get("url")})

        ---"""

        entries.append(entry)


    full = "\n\n".join(entries)

    return header + "\n\n" + full






def save_digest(formated_articles, output_dir ="data"):

    file_name = f"digest_{datetime.now().strftime('%Y%m%d')}.md"


    os.makedirs(output_dir, exist_ok=True)

    p = os.path.join(output_dir, file_name)


    with open(p, "w", encoding="utf-8") as f:
        f.write(formated_articles)

    return p







def format_digest_html(articles):


    header = f"Daily News Updates - {datetime.now().strftime('%Y%m%d')}"


    # group articles by their matched topic
    grouped = {}
    for article in articles:
        topic = article.get("matched_topic", "Other")
        grouped.setdefault(topic, []).append(article)


    sections = []
    for topic, topic_articles in grouped.items():
        cards = []
        for article in topic_articles:
            title = article.get("title")
            description = article.get("description") or ""
            url = article.get("url")
            source_name = article.get("source", {}).get("name")
            cards.append(f"""
            <div class="card">
              <h3>{title}</h3>
              <p class="source">{source_name}</p>
              <p class="desc">{description}</p>
              <a class="link" href="{url}">Read more →</a>
            </div>""")


        sections.append(
            f"""
        <section>
          <h2 class="topic-header">{topic.title()}</h2>
          <div class="card-grid">
            {''.join(cards)}
          </div>
        </section>"""
        )



    style = """
    <style>
      :root {
        --bg: #f5f5f7; --card-bg: #ffffff; --text: #1a1a1a;
        --muted: #666666; --accent: #2563eb; --border: #e0e0e0;
      }
      @media (prefers-color-scheme: dark) {
        :root {
          --bg: #121212; --card-bg: #1e1e1e; --text: #eaeaea;
          --muted: #999999; --accent: #6ea8fe; --border: #333333;
        }
      }
      body {
        background: var(--bg); color: var(--text);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        max-width: 900px; margin: 0 auto; padding: 30px 20px;
      }
      h1 { font-size: 1.8em; margin-bottom: 30px; }
      .topic-header {
        font-size: 1.3em; margin: 40px 0 15px;
        border-bottom: 2px solid var(--accent); padding-bottom: 6px;
      }
      .card-grid {
        display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
        gap: 16px;
      }
      .card {
        background: var(--card-bg); border: 1px solid var(--border);
        border-radius: 10px; padding: 16px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
      }
      .card h3 { font-size: 1.05em; margin: 0 0 8px; line-height: 1.3; }
      .card .source { color: var(--muted); font-size: 0.85em; margin: 0 0 8px; }
      .card .desc { font-size: 0.9em; line-height: 1.4; margin: 0 0 10px; }
      .card .link { color: var(--accent); text-decoration: none; font-size: 0.9em; font-weight: 600; }
      .card .link:hover { text-decoration: underline; }
    </style>
    """



    full_page = f"""<!DOCTYPE html>
<html>
<head>
<title>Daily News Digest</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
{style}
</head>
<body>
<h1>{header}</h1>
{''.join(sections)}
</body>
</html>"""

    return full_page






def save_digest_html(formated_articles, output_dir ="site"):

    file_name = "index.html"


    os.makedirs(output_dir, exist_ok=True)

    p = os.path.join(output_dir, file_name)


    with open(p, "w", encoding="utf-8") as f:
        f.write(formated_articles)

    return p
