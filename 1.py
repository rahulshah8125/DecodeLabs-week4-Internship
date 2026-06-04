import pandas as pd

df = pd.read_csv("sample_-_superstore.csv", encoding="latin1")

print("=" * 50)
print("TASK 1: DATASET UNDERSTANDING")
print("=" * 50)


print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())