import pandas as pd

file_path = r'C:\Users\gsrid\Desktop\SQL Learning Journey\Amazon Data Set\Amazon Raw Data.csv'

df=pd.read_csv(file_path,encoding='ISO-8859-1')

print(df.head())

# --- Clean Price Columns ---
# Remove currency symbols and commas, then convert to float
# Clean discounted_price
df['discounted_price'] = (
    df['discounted_price']
    .astype(str) # Convert to string first safely
    .str.encode('utf-8') # Re-encode properly
    .str.decode('utf-8', errors='ignore') # Ignore decoding errors
    .replace({'[^0-9.]': ''}, regex=True) # Remove everything except numbers and decimal points
    .replace('', '0') # If any field is empty, replace with 0
    .astype(float) # Now safely convert to float
)

# Clean actual_price
df['actual_price'] = (
    df['actual_price']
    .astype(str)
    .str.encode('utf-8')
    .str.decode('utf-8', errors='ignore')
    .replace({'[^0-9.]': ''}, regex=True)
    .replace('', '0')
    .astype(float)
)


# --- Clean Discount Percentage ---
df['discount_percentage'] = df['discount_percentage'].replace({'%': ''}, regex=True).astype(float)

# --- Clean Rating Count ---

df['rating_count'] = (
    df['rating_count']
    .replace({',': ''}, regex=True)  # Remove commas
    .fillna(0)                       # Fill missing values with 0
    .astype(int)                     # Now safely convert to int
)



# --- Basic Missing Value Check ---
print("\nMissing Values:\n", df.isnull().sum())

# --- Save the cleaned file ---
output_path = 'C:/Users/gsrid/Desktop/SQL Learning Journey/Amazon Data Set/amazon_cleaned_data_v1.csv'


df.to_csv(output_path, index=False)

print(f"\n Cleaned data saved successfully to {output_path}")