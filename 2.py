import pandas as pd

df = pd.read_csv("sample_-_superstore.csv", encoding="latin1")

print("=" * 50)
print("TASK 2 : DATA CLEANING & PREPROCESSING")
print("=" * 50)


print("Before Cleaning:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna("Unknown")

# Remove spaces from column names
df.columns = df.columns.str.strip()

print("\nAfter Cleaning:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("cleaned_superstore.csv", index=False)

print("\nDataset Cleaned Successfully")