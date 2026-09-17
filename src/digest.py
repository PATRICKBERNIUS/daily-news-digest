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

    entries = []

    for article in articles:

        title = article.get("title")
        description = article.get("description") or ""
        url = article.get("url")
        source = article.get("source", {}).get("name")


        lines = [
            '<div class="article">',
            f'<h2>{title}</h2>',
            f'<p><em>{source}</em></p>',
            f'<p>{description}</p>',
            f'<a href="{url}">Read more</a>',
            '</div>',
            '<hr>',
        ]

        entries.append("\n".join(lines))


    full = "\n\n".join(entries)


    full_page = f"""<!DOCTYPE html>
        <html>
        <head><title>Daily News Digest</title></head>
        <body>
        <h1>{header}</h1>
        {full}
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
