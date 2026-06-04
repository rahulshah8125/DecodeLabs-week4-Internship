import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("sample_-_superstore.csv", encoding="latin1")

print("=" * 50)
print("TASK 5: Predictive Model")
print("=" * 50)


# Select features and target
X = df[["Sales", "Quantity", "Discount"]]
y = df["Profit"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
print("Model Performance")
print("-" * 30)

print("R2 Score:", r2_score(y_test, predictions))
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))

# Sample predictions
result = pd.DataFrame({
    "Actual Profit": y_test.values[:10],
    "Predicted Profit": predictions[:10]
})

print("\nSample Predictions:")
print(result)