import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_-_superstore.csv", encoding="latin1")

print("=" * 50)
print("TASK 4 : DATA VISUALIZATION")
print("=" * 50)

# Sales by Region
df.groupby("Region")["Sales"].sum().plot(kind="bar", figsize=(8,5))
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.show()

# Profit by Category
df.groupby("Category")["Profit"].sum().plot(kind="bar", figsize=(8,5))
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.show()

# Sales Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=20)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Category Share
df["Category"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Distribution")
plt.ylabel("")
plt.show()