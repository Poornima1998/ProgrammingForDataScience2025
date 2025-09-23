import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(df):
    sns.histplot(df['price'], bins=20, kde=True)
    plt.title('Book Price Distribution')
    plt.show()

def plot_scatter(df):
    sns.scatterplot(x='rating', y='price', data=df)
    plt.title('Rating vs Price')
    plt.show()
