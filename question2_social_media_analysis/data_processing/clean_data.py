# This script cleans and preprocesses the raw book data
import re

import pandas as pd

def clean_data(input_file="books_raw.csv", output_file="books_clean.csv"):
    """Clean scraped book data and save cleaned version."""
    df = pd.read_csv(input_file)

    # Remove any non-numeric characters (handles £, Â, commas, etc.)
    df["price"] = df["price"].apply(lambda x: float(re.sub(r"[^0-9.]", "", str(x))))

    # Convert rating text to numeric scale
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["rating"] = df["rating"].map(rating_map)

    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")
    return df
