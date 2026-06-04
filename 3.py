import pandas as pd

df = pd.read_csv("sample_-_superstore.csv", encoding="latin1")

print("=" * 50)
print("TASK 3 : EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 50)


print("Total Sales:", df["Sales"].sum())

print("Average Sales:", df["Sales"].mean())

print("Total Profit:", df["Profit"].sum())

print("Average Profit:", df["Profit"].mean())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum())

print("\nTop 10 Products by Sales:")
print(df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10))