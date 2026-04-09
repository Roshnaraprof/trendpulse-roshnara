# task2_data_processing.py

import pandas as pd
import os

# -------------------------------
# 1. Load JSON File
# -------------------------------

file_path = r"D:\AIML\trendpulse-roshnara\data\trends_20260409.json"

# Check if file exists
if not os.path.exists(file_path):
    print("❌ File not found. Check the file path.")
    exit()

# Load JSON into DataFrame
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}\n")

# -------------------------------
# 2. Clean the Data
# -------------------------------

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types safely
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# Drop rows where conversion failed
df = df.dropna(subset=["score", "num_comments"])

# Convert to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-quality stories
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Clean whitespace in title
df["title"] = df["title"].str.strip()

## -------------------------------
# 3. Save as CSV
# -------------------------------

output_path = r"D:\AIML\trendpulse-roshnara\data\trends_cleaned.csv"

# Create folder if it doesn't exist
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save file
df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")
# -------------------------------
# Summary
# -------------------------------

print("\nStories per category:")
print(df["category"].value_counts())