##not working properly sql not supporting
import sqlite3

# Connect to the database (Replace 'your_database.db' with actual database file)
conn = sqlite3.connect("employee.xlsx")
cursor = conn.cursor()

# Fetch data from table
cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()

# Get row count
row_count = len(rows)

# Get column count
column_count = len(cursor.description)  # cursor.description contains column metadata

print(f"Rows: {row_count}, Columns: {column_count}")

# Close the connection
conn.close()
