import requests
import json
import os
import random
import time
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
    title = title.lower()
    for category, keywords in CATEGORIES.items():
        if any(word in title for word in keywords):
            return category
    return None


def main():
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        all_ids = response.json()[:500]
    except Exception as e:
        print("Error:", e)
        return

    random.shuffle(all_ids)

    collected_data = []
    category_count = {cat: 0 for cat in CATEGORIES}

    for story_id in all_ids:
        if all(count >= 25 for count in category_count.values()):
            break

        try:
            url = ITEM_URL.format(story_id)
            story = requests.get(url, headers=headers).json()
        except:
            continue

        if not story or "title" not in story:
            continue

        category = get_category(story["title"])
        if category is None or category_count[category] >= 25:
            continue

        data = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_data.append(data)
        category_count[category] += 1

        if category_count[category] == 25:
            time.sleep(2)

    os.makedirs("data", exist_ok=True)

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(collected_data, f, indent=4)

    print(f"Collected {len(collected_data)} stories. Saved to {filename}")


if __name__ == "__main__":
    main()