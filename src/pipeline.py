import os
import pandas as pd

   
    
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sales_file_path = os.path.join(base_dir, "data", "sales.csv")
    
sales_df = pd.read_csv(sales_file_path)
print("Extracted Data:")
print(sales_df)
total = (sales_df['quantity'] * sales_df['price']).sum()

save_file_path = os.path.join(base_dir, "data", "processed_sales.txt")

with open(save_file_path, "w") as f:
    f.write(f"Total Sales: {total}")

