import numpy as np
import pandas as pd
def train_linear_regression(X, y, learning_rate=0.01, epochs=1000):
    m, n = X.shape
    w = np.zeros(n)
    b = 0
    for _ in range(epochs):
        y_pred = np.dot(X, w) + b
        dw = (1/m) * np.dot(X.T, (y_pred - y))
        db = (1/m) * np.sum(y_pred - y)
        w -= learning_rate * dw
        b -= learning_rate * db
    return w, b
def predict_price(X, w, b):
    return np.dot(X, w) + b
df = pd.read_csv('data.csv')
features = ['bedrooms', 'bathrooms', 'sqft_living']
X = df[features].values
y = df['price'].values
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_normalized = (X - X_mean) / X_std
w, b = train_linear_regression(X_normalized, y, learning_rate=0.1, epochs=1000)
print("Enter the details of the house to predict its price:")
bedrooms = float(input("Bedrooms (e.g., 3): "))
bathrooms = float(input("Bathrooms (e.g., 2.5): "))
sqft_living = float(input("Sqft living (e.g., 2000): "))
user_house = np.array([[bedrooms, bathrooms, sqft_living]])
user_house_normalized = (user_house - X_mean) / X_std
predicted_price = predict_price(user_house_normalized, w, b)
print(f"\nPredicted price for the house is: ${predicted_price[0]:,.2f}")


# def sigmoid(z):
#     return 1 /(1 + np.exp(-z))
# def train(X, y, learning_rate = 0.01, epochs = 100):
#     m, n = X.shape
#     w = np.zeros(n)
#     b=0
#     for _ in range(epochs):
#         z = np.dot(X, w) + b
#         a = sigmoid(z)
#         dw = (1/m) * np.dot(X.T, (a - y))
#         db = (1/m) * np.sum(a - y)
#         w -= learning_rate * dw
#         b -= learning_rate * db
#     return w, b
# def predict(X, w, b, threshold = 0.5):
#     probabalities = sigmoid(np.dot(X, w)+ b)
#     return (probabalities >= threshold).astype(int)

# df = pd.read_csv('data.csv')
# features = ['bedrooms','bathrooms','sqft_living']
# X = df[features].values
# prices = df['price'].values
# print("Enter thresflod Value : ")
# threshold = int(input( ))
# y = (prices >= threshold).astype(int)
# X_mean = np.mean(X ,axis = 0)
# X_std = np.std(X ,axis= 0)
# X_normalized = (X - X_mean) / X_std
# n = len(X)
# train_idx = int(0.8*n)
# X_train, X_test = X_normalized[:train_idx], X_normalized[train_idx:]
# y_train, y_test = y[:train_idx], y[train_idx:]
# w, b = train(X_train, y_train, learning_rate = 0.01, epochs = 500)
# y_pred_test = predict(X_test, w, b)
# accuracy = np.mean(y_pred_test == y_test)
# print(f"model accuracy set to {accuracy :.2f}")
# bedrooms = float(input("Bedrooms (e.g., 3): "))
# bathrooms = float(input("Bathrooms (e.g., 2.5): "))
# sqft_living = float(input("Sqft living (e.g., 2000): "))
# # Normalize user input
# user_house = np.array([[bedrooms, bathrooms, sqft_living]])
# user_house_normalized = (user_house - X_mean) / X_std

# # Predict
# prediction = predict(user_house_normalized, w, b)[0]
# label = "expensive" if prediction == 1 else "affordable"
# print(f"\nPrediction: The house is {label} (price {'above or equal to' if prediction == 1 else 'below'} ${threshold:.2f})")