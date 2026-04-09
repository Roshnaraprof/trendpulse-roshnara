# Task 4 — Visualizations
# TrendPulse Project
# This script loads analysed data and creates 3 charts + 1 dashboard

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# 1. SETUP
# -------------------------------

# Load the analysed CSV file from Task 3
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create outputs folder if it doesn't exist
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# -------------------------------
# 2. CHART 1: Top 10 Stories by Score
# -------------------------------

# Sort data by score and take top 10
top_stories = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles to max 50 characters
top_stories["short_title"] = top_stories["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_stories["short_title"], top_stories["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # Highest score at top

# Save chart
plt.savefig(f"{output_folder}/chart1_top_stories.png")
plt.close()


# -------------------------------
# 3. CHART 2: Stories per Category
# -------------------------------

# Count number of stories per category
category_counts = df["category"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

# Save chart
plt.savefig(f"{output_folder}/chart2_categories.png")
plt.close()


# -------------------------------
# 4. CHART 3: Score vs Comments
# -------------------------------

# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Create scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

# Save chart
plt.savefig(f"{output_folder}/chart3_scatter.png")
plt.close()


# -------------------------------
# 5. BONUS: DASHBOARD
# -------------------------------

# Create subplots (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# ---- Chart 1 in dashboard ----
axes[0].barh(top_stories["short_title"], top_stories["score"])
axes[0].set_title("Top Stories")
axes[0].set_xlabel("Score")
axes[0].invert_yaxis()

# ---- Chart 2 in dashboard ----
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Count")

# ---- Chart 3 in dashboard ----
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Comments")
axes[2].legend()

# Overall title
plt.suptitle("TrendPulse Dashboard")

# Save dashboard
plt.savefig(f"{output_folder}/dashboard.png")
plt.close()


print("✅ All charts saved successfully in 'outputs/' folder!")