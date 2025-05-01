import pandas as pd
import os

# Load cleaned dataset
input_path = r'C:\Users\gsrid\Desktop\SQL Learning Journey\Amazon Data Set\amazon_cleaned_data_v1.csv'
df = pd.read_csv(input_path)

# Convert review columns to lists
columns_to_split = ['user_id', 'user_name', 'review_id', 'review_title', 'review_content']
for col in columns_to_split:
    df[col] = df[col].astype(str).str.split(',')

# Container for new rows
expanded_rows = []

# Process row-by-row (safe for memory)
for i, row in df.iterrows():
    length = len(row['user_id'])
    
    for j in range(length):
        try:
            expanded_rows.append({
                'product_id': row['product_id'],
                'product_name': row['product_name'],
                'category': row['category'],
                'discounted_price': row['discounted_price'],
                'actual_price': row['actual_price'],
                'discount_percentage': row['discount_percentage'],
                'rating': row['rating'],
                'rating_count': row['rating_count'],
                'about_product': row['about_product'],
                'img_link': row['img_link'],
                'product_link': row['product_link'],
                'user_id': row['user_id'][j],
                'user_name': row['user_name'][j],
                'review_id': row['review_id'][j],
                'review_title': row['review_title'][j],
                'review_content': row['review_content'][j],
            })
        except IndexError:
            # skip incomplete rows if lengths don’t match
            continue

# Convert to DataFrame
final_df = pd.DataFrame(expanded_rows)

# Save final exploded dataset
output_path = r'C:\Users\gsrid\Desktop\SQL Learning Journey\Amazon Data Set\amazon_cleaned_data_v2.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
final_df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned and safely exploded file saved to:\n{output_path}")
