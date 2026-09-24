from anthropic import Anthropic
import os


anthropic_api = os.getenv("CLAUDE_API")



def summarize_articles(articles):


    client = Anthropic(api_key=anthropic_api)


    full_articles = []
    for article in articles:
        title = article["title"]
        description = article.get("description", {}) or ""
        content = article.get("content", {}) or ""

        string = f"{title}: Short Description: {description}. Content Snapshot: {content}"

        full_articles.append(string)

    full_articles_text = "\n\n".join(full_articles)




    prompt = f"""You are writing a daily news briefing for one reader. Below is a list of today's articles.

    Write a cohesive briefing that synthesizes the most important developments across these articles — group related stories together naturally where it makes sense, rather than listing every article one by one. Make sure to identify the big points and updates in Artificial Intelligence, Biotechnology, technology, and health research. Use a natural, spoken tone, as if reading this aloud to someone who wants to stay informed without reading the news themselves. Do not use bullet points, headers, or markdown formatting — write in full paragraphs only.

    Today's articles:
    {full_articles_text}

    Briefing:"""

    try:

        message = client.messages.create(
            model = "claude-sonnet-5",
            max_tokens=1024,
            messages = [
                {"role": "user", "content": prompt}
            ]
        )

        full_summary = message.content[0].text


        return full_summary
    except Exception as e:
        print(f"Warning: LLM summary failed: {e}")
        return "No summmary today"



def save_llm_summary(summary, output_dir ="site"):

    file_name = "summary.txt"


    os.makedirs(output_dir, exist_ok=True)

    p = os.path.join(output_dir, file_name)


    with open(p, "w", encoding="utf-8") as f:
        f.write(summary)

    return p



def load_summary(path="site/summary.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()