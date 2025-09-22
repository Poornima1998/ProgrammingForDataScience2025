def clean_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates()
    # Remove missing values
    df = df.dropna()
    # Normalize the Title by stripping spaces and changing to lowercase
    df['Title'] = df['Title'].str.strip().str.lower()
    return df
