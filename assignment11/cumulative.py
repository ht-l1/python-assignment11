import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 2
conn = sqlite3.connect('../db/lesson.db')

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

print("Without cumulative:")
print(df.head())

df['cumulative'] = df['total_price'].cumsum()

print("\nWith cumulative column:")
print(df.head())

# Create line plot using Pandas plotting
plt.figure(figsize=(12, 6))
df.plot(x='order_id', y='cumulative', kind='line', color='lightgreen', linewidth=2)
plt.title('Cumulative Revenue by Orders')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()