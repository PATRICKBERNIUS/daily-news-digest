import os
import time
import requests
from dotenv import load_dotenv


env_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path=env_path)

GNEWS_BASE_URL = "https://gnews.io/api/v4/search"
apikey = os.getenv("GNEWS_API_KEY")







def fetch_articles_for_topic(topic, max_articles):
    

    r = requests.get(
    GNEWS_BASE_URL,
    params={
        "q": topic,
        "lang": "en",
        "max": max_articles,
        "apikey": apikey
    }
)

    if r.status_code != 200:
        raise RuntimeError(f"GNews returned {r.status_code}: {r.text}")

    res = r.json()

    if "errors" in res:
        raise RuntimeError(res["errors"])

    if "articles" not in res or len(res["articles"]) == 0:
        raise ValueError(f"No articles matching topic {topic} found.")

    return res["articles"]



def fetch_all_articles(topics):

    tops = {}

    for topic in topics:
        try:
            f = fetch_articles_for_topic(topic, 20)

            tops[topic] = f
            time.sleep(1)
        except Exception as e:
            print(f"Warning: Failed at topic {topic}: {e}")
            tops[topic] = []




    return tops








