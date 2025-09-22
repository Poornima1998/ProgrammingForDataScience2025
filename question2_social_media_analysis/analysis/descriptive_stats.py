import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data(df):
    print("Summary Statistics:")
    print(df.describe())

    # Plot histogram of prices
    sns.histplot(df['Price'], bins=10, kde=True)
    plt.title('Price Distribution')
    plt.xlabel('Price (£)')
    plt.ylabel('Count')
    plt.show()

    # Scatter plot Price vs Rating
    sns.scatterplot(x='Rating', y='Price', data=df)
    plt.title('Price vs Rating')
    plt.show()
