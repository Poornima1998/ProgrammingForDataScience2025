import plotly.express as px

def interactive_hist(df):
    fig = px.histogram(df, x="price", color="rating", title="Interactive Price Distribution by Rating")
    fig.show()
