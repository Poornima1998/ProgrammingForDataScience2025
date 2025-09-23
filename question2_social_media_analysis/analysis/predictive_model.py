from sklearn.linear_model import LinearRegression
import numpy as np

def price_predictor(df):
    X = df[["rating"]].values
    y = df["price"].values
    model = LinearRegression().fit(X, y)
    print("Regression coefficient:", model.coef_[0])
    print("Intercept:", model.intercept_)
    return model
