from filter_news import is_relevant, filter_recent, dedupe_articles
from datetime import datetime, timezone, timedelta









# Clearly relevant to "AI"
article_ai_relevant = {
    "id": "abc123",
    "title": "New AI breakthrough helps doctors diagnose disease faster",
    "description": "Researchers unveiled a new artificial intelligence model...",
    "url": "https://example.com/ai-breakthrough",
    "publishedAt": "2026-09-15T12:00:00Z",
    "source": {"name": "Example News", "url": "https://example.com"},
}

# Clearly NOT relevant to "AI" (e.g. a sports story)
article_unrelated = {
    "id": "def456",
    "title": "Local team wins championship in overtime thriller",
    "description": "Fans celebrated late into the night after a stunning win.",
    "url": "https://example.com/sports-win",
    "publishedAt": "2026-09-15T12:00:00Z",
    "source": {"name": "Example Sports", "url": "https://example.com"},
}

# Missing 'description' entirely
article_no_description = {
    "id": "ghi789",
    "title": "AI regulation debate heats up in Congress",
    "url": "https://example.com/ai-regulation",
    "publishedAt": "2026-09-15T12:00:00Z",
    "source": {"name": "Example Politics", "url": "https://example.com"},
}

# 'description' present but explicitly None
article_none_description = {
    "id": "jkl012",
    "title": "AI startup raises funding round",
    "description": None,
    "url": "https://example.com/ai-funding",
    "publishedAt": "2026-09-15T12:00:00Z",
    "source": {"name": "Example Biz", "url": "https://example.com"},
}

















def test_is_relevant_true():
    res = is_relevant(article_ai_relevant, "AI")
    assert res 



def test_is_relevant_false():
    res = is_relevant(article_unrelated, "AI")
    assert not res


def test_is_relevant_missing_fields():
    res  = is_relevant(article_no_description, "AI")
    assert res

    res_two = is_relevant(article_none_description, "AI")
    assert res_two







recent_time = datetime.now(timezone.utc) - timedelta(hours=2)
article_recent = {
    "id": "recent1",
    "title": "Recent AI news",
    "description": "...",
    "publishedAt": recent_time.isoformat(),
}



def test_filter_recent_keeps_new_articles():
    res = filter_recent([article_recent])
    assert res


old_time = datetime.now(timezone.utc) - timedelta(hours=72)
article_old = {
    "id": "old1",
    "title": "Old AI news",
    "description": "...",
    "publishedAt": old_time.isoformat(),
}

def test_filter_recent_drops_old_articles():
    res = filter_recent([article_old])
    assert not res


duplicate_article = {
    "id": "dup001",
    "title": "New AI model predicts protein structures",
    "description": "Researchers combined AI and biotech techniques...",
    "url": "https://example.com/ai-protein",
    "publishedAt": "2026-09-15T12:00:00Z",
    "source": {"name": "Example Science", "url": "https://example.com"},
}


topic_articles_with_dupe = {
    "AI": [duplicate_article],
    "biotechnology": [duplicate_article],
}



def test_dedup_removes_duplicates():
    res = dedupe_articles(topic_articles_with_dupe)


    assert len(res) == 1