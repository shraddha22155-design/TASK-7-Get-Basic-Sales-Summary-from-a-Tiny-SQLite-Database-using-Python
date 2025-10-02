
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("sales_data.db")

# Run SQL query
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Print results
print(df)

# Plot revenue by product
df.plot(kind="bar", x="product", y="revenue", legend=False, title="Revenue by Product")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("sales_chart.png")

# Save summary as CSV
df.to_csv("sales_summary.csv", index=False)

conn.close()
