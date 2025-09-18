# This script generates simple visualizations for the dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_plots(input_file="books_clean.csv"):
    """Generate visualizations from cleaned dataset."""
    df = pd.read_csv(input_file)

    # Histogram of prices
    plt.figure(figsize=(8, 5))
    sns.histplot(df["price"], bins=20, kde=True)
    plt.title("Distribution of Book Prices")
    plt.xlabel("Price (£)")
    plt.ylabel("Count")
    plt.savefig("price_distribution.png")
    plt.close()

    # Countplot of ratings
    plt.figure(figsize=(6, 4))
    sns.countplot(x="rating", data=df, palette="viridis")
    plt.title("Book Ratings Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.savefig("rating_distribution.png")
    plt.close()

    # Scatter plot of price vs rating
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x="rating", y="price", data=df)
    plt.title("Price vs Rating")
    plt.xlabel("Rating")
    plt.ylabel("Price (£)")
    plt.savefig("price_vs_rating.png")
    plt.close()

    print("Plots saved: price_distribution.png, rating_distribution.png, price_vs_rating.png")
