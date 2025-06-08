import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 1
# In your assignment11 folder, connect to ../db/lesson.db. 
conn = sqlite3.connect('../db/lesson.db')

# SQL query
query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e JOIN orders o 
ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

employee_results = pd.read_sql_query(query, conn)
conn.close()

# Pandas plotting - create a bar chart where the x axis is the employee last name and the y axis is the revenue.
# Give appropriate titles, labels, and colors.Show the plot.
plt.figure(figsize=(10, 6))
employee_results.plot(x='last_name', y='revenue', kind='bar', color='#7CA1CC')
plt.title('Employee Revenue KPI')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()