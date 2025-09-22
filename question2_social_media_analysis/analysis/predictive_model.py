import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def predictive_model(df):
    # Prepare data
    X = df[['Rating']].values
    y = df['Price'].values

    # Create linear regression model
    model = LinearRegression()
    model.fit(X, y)

    print(f"Model Coefficient (Effect of Rating on Price): {model.coef_[0]:.2f}")
    print(f"Model Intercept: {model.intercept_:.2f}")

    # Predict prices for ratings 1 to 5
    rating_test = np.array([[i] for i in range(1,6)])
    price_pred = model.predict(rating_test)

    # Plot predictions
    plt.plot(rating_test, price_pred, marker='o')
    plt.title('Predicted Price by Rating')
    plt.xlabel('Rating')
    plt.ylabel('Predicted Price (£)')
    plt.show()
