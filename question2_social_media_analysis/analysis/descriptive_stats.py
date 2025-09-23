def summarize(df):
    print("Summary statistics:")
    print(df.describe())
    print("Number of books:", len(df))
    print("Most common rating:", df['rating'].mode()[0])
