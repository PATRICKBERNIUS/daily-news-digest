# Personalized Daily News Digest

A pipeline that fetches daily news on topics I care about (AI, technology,
biotech, health research, and general world-advancement news), filters and
summarizes it, and publishes a digest.

## Status
- [ ] Milestone 1: Fetch + filter + save locally
- [ ] Milestone 2: Automated tests + CI
- [ ] Milestone 3: Scheduled pipeline (GitHub Actions cron)
- [ ] Milestone 4: Publish to GitHub Pages dashboard
- [ ] Milestone 5: Email digest
- [ ] Milestone 6 (stretch): Text-to-speech version

## Setup
1. Get a free API key from https://newsapi.org/ (or https://gnews.io/ as an
   alternative — GNews has a more generous free tier).
2. Copy `.env.example` to `.env` and add your key.
3. `pip install -r requirements.txt`
4. `python src/fetch_news.py`

## Project structure
```
src/
  config.py       - topics list and settings
  fetch_news.py   - calls the news API, returns raw articles
  filter_news.py  - filters/dedupes articles by topic relevance
  digest.py       - formats and saves the final digest
tests/
  test_filter_news.py - unit tests for filtering logic
data/
  digest_YYYY-MM-DD.json - output goes here (gitignored)
```
