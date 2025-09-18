# This script performs basic statistical analysis on the cleaned dataset

import pandas as pd

def descriptive_stats(input_file="books_clean.csv"):
    """Generate and display descriptive statistics."""
    df = pd.read_csv(input_file)

    print("\n--- Descriptive Statistics ---")
    print(df.describe(include="all"))

    avg_price = df["price"].mean()
    avg_rating = df["rating"].mean()

    print(f"\nAverage Price: £{avg_price:.2f}")
    print(f"Average Rating: {avg_rating:.2f} / 5")

    df.describe(include="all").to_csv("descriptive_stats.csv")
    print("Descriptive statistics saved to descriptive_stats.csv")
