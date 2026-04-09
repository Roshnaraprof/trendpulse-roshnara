import pandas as pd

def main():
    df = pd.read_csv("data/trends_cleaned.csv")

    print("\nTop 5 Posts by Score:")
    print(df.sort_values(by="score", ascending=False).head())

    print("\nAverage Score per Category:")
    print(df.groupby("category")["score"].mean())

    print("\nTotal Comments per Category:")
    print(df.groupby("category")["num_comments"].sum())

    print("\nTop Authors:")
    print(df["author"].value_counts().head())

if __name__ == "__main__":
    main()