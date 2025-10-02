# Sales Data Analysis (Task 7)

This project is part of the **Data Analyst Internship - Task 7**.  
The objective is to create a small SQLite database, query it using Python, and generate a simple sales summary with visualization.

## Contents
- `sales_data.db` : SQLite database containing sample sales data
- `sales_summary.csv` : Aggregated sales summary (total quantity & revenue per product)
- `sales_chart.png` : Bar chart of revenue by product
- `sales_task.py` : Python script to reproduce the analysis

## Steps Performed
1. Created a SQLite database (`sales_data.db`) with a `sales` table.
2. Inserted sample sales records (product, quantity, price).
3. Queried the database using SQL:
   ```sql
   SELECT product, 
          SUM(quantity) AS total_qty, 
          SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product;
   ```
4. Loaded results into Pandas for easy handling.
5. Exported results to CSV (`sales_summary.csv`).
6. Visualized revenue by product using Matplotlib (`sales_chart.png`).

## How to Run
1. Clone this repository or download the ZIP.
2. Ensure you have Python installed with the following libraries:
   - `sqlite3`
   - `pandas`
   - `matplotlib`
3. Run the script:
   ```bash
   python sales_task.py
   ```
4. This will:
   - Query the database
   - Print the sales summary
   - Save a CSV file and chart
