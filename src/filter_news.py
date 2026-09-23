import os
import time
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta


def is_relevant(article, topic):

    title = article.get('title') or ""
    description = article.get('description') or ""

    if topic.lower() in title.lower() or topic.lower() in description.lower():
        return True
    else:
        return False
    
    



def dedupe_articles(topic_articles):

    seen_ids = set()
    arts = []
    
    for topic, articles in topic_articles.items():
        for article in articles:
            if is_relevant(article, topic) and article['id'] not in seen_ids:
                article["matched_topic"] = topic
                arts.append(article)
                seen_ids.add(article['id'])
    
    return arts





def filter_recent(articles, max_age_hours=48):

    now = datetime.now(timezone.utc)
    time_ago = now - timedelta(hours=max_age_hours)

    arts = []

    for article in articles:
        raw_date = article.get("publishedAt")
        if raw_date is None:
            continue
        pub_date = datetime.fromisoformat(raw_date)

        if time_ago <= pub_date:
            arts.append(article)

    return arts

    



def process_articles(topic_articles):
    
    single_articles = dedupe_articles(topic_articles)

    return filter_recent(single_articles)


