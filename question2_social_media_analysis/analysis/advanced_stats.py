def advanced_stats(df):
    print("Mean price:", df['price'].mean())
    print("Price vs rating:", df['price'].corr(df['rating']))
    print("Category popularity:")
    print(df['rating'].value_counts())

    q1, q3 = df['price'].quantile([0.25, 0.75])
    iqr = q3 - q1
    outliers = df[(df['price'] < q1 - 1.5*iqr) | (df['price'] > q3 + 1.5*iqr)]
    print("Outliers found:", len(outliers))
