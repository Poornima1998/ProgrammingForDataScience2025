import pandas as pd
import re

def clean_books_data(filename):
    df = pd.read_csv(filename)
    df = df.drop_duplicates().dropna()
    df['title'] = df['title'].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x)).strip().lower())
    return df
