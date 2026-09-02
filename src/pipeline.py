import os
import pandas as pd


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sales_file_path = os.path.join(base_dir, "data", "sales.csv")
    
sales_df = pd.read_csv(sales_file_path)
print("Extracted Data:")
print(sales_df)

sales_df = sales_df[(sales_df['quantity'] > 0) & (sales_df['price'] >= 0)]
count = 0 
for row in sales_df.itertuples():
    count += 1
quantity = sales_df['quantity'].sum()

total = (sales_df['quantity'] * sales_df['price']).sum()

save_file_path = os.path.join(base_dir, "data", "processed_sales.txt")

with open(save_file_path, "w") as f:
    f.write(f"Total Sales: {total}")
    f.write(f"Total Quantity: {quantity}")
    f.write(f"Total products: {count}")

