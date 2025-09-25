from sklearn.linear_model import LinearRegression


def price_predictor(df):
    rating = df[["rating"]].values
    price = df["price"].values

    price_model = LinearRegression()
    price_model.fit(rating, price)

    slope = price_model.coef_[0]
    intercept = price_model.intercept_

    print(f"Coefficient (slope) of rating: {slope:.4f}")
    print(f"Intercept (base price): {intercept:.4f}")

    return price_model