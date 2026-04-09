import json
import pandas as pd
import os

def load_latest_json():
    files = os.listdir("data")
    json_files = [f for f in files if f.endswith(".json")]
    latest = sorted(json_files)[-1]
    return os.path.join("data", latest)

def clean_data(data):
    cleaned = []
    for item in data:
        if not item.get("title") or not item.get("category"):
            continue

        item["score"] = item.get("score", 0)
        item["num_comments"] = item.get("num_comments", 0)

        cleaned.append(item)

    return cleaned

def main():
    file_path = load_latest_json()

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    cleaned = clean_data(data)

    df = pd.DataFrame(cleaned)

    output_file = "data/trends_cleaned.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved cleaned data to {output_file}")
    print(f"Total records: {len(df)}")

if __name__ == "__main__":
    main()