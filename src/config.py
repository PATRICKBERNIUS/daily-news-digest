"""
Central config for the news digest pipeline.
Edit TOPICS to change what you track.
"""

TOPICS = [
    "artificial intelligence",
    "technology",
    "biotechnology",
    "health research",
    "scientific breakthrough",
]

# How many articles to fetch per topic, per run
ARTICLES_PER_TOPIC = 5

# Where the daily digest gets saved
OUTPUT_DIR = "data"
