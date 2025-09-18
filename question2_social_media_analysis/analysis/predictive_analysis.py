# This script runs a simple linear regression to predict book price from rating
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def predictive_analysis(input_file="books_clean.csv"):
    """Run a simple regression model to predict price based on rating."""
    df = pd.read_csv(input_file)

    if "price" not in df.columns or "rating" not in df.columns:
        print("Dataset missing required columns.")
        return

    X = df[["rating"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    print("\n--- Predictive Analysis ---")
    print(f"Coefficient (impact of rating on price): {model.coef_[0]:.4f}")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")
