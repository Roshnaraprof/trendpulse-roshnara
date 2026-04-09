# task3_analysis.py

import pandas as pd
import numpy as np

# -------------------------------
# 1. LOAD AND EXPLORE DATA
# -------------------------------

# Correct file path (from your previous task)
input_path = r"D:\AIML\trendpulse-roshnara\data\trends_cleaned.csv"

# Load CSV
df = pd.read_csv(input_path)

# Display basic info
print("Loaded data:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

# Calculate averages using Pandas
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))


# -------------------------------
# 2. NUMPY ANALYSIS
# -------------------------------

print("\n--- NumPy Stats ---")

scores = df["score"].to_numpy()
comments = df["num_comments"].to_numpy()

# Mean, Median, Std
print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))

# Max & Min
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# Category with most stories
most_common_category = df["category"].value_counts().idxmax()
count_category = df["category"].value_counts().max()

print(f"\nMost stories in: {most_common_category} ({count_category} stories)")

# Story with most comments
max_comment_index = np.argmax(comments)

top_story_title = df.loc[max_comment_index, "title"]
top_story_comments = df.loc[max_comment_index, "num_comments"]

print(f"\nMost commented story: \"{top_story_title}\" — {top_story_comments} comments")


# -------------------------------
# 3. ADD NEW COLUMNS
# -------------------------------

# Engagement column
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular column
df["is_popular"] = df["score"] > avg_score


# -------------------------------
# 4. SAVE RESULT
# -------------------------------

output_path = r"D:\AIML\trendpulse-roshnara\data\trends_analysed.csv"

df.to_csv(output_path, index=False)

print("\nSaved to:", output_path)