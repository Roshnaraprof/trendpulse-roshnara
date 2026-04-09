import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("data/trends_cleaned.csv")

    # Bar chart: posts per category
    df["category"].value_counts().plot(kind="bar")
    plt.title("Posts per Category")
    plt.show()

    # Bar chart: average score
    df.groupby("category")["score"].mean().plot(kind="bar")
    plt.title("Average Score per Category")
    plt.show()

    # Histogram: comments
    plt.hist(df["num_comments"])
    plt.title("Comments Distribution")
    plt.show()

if __name__ == "__main__":
    main()