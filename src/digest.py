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