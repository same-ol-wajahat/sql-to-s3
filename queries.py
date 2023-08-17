import pyodbc
import csv

# Connection settings
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'

# Create a connection
conn = pyodbc.connect(
    f'DRIVER=ODBC Driver 17 for SQL Server;'
    f'SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

# Define your query
query = 'SELECT * FROM your_table'

# Execute the query
cursor = conn.cursor()
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Close the connection
conn.close()

# Define the path to the CSV file
csv_file_path = 'output.csv'

# Write data to CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([column[0] for column in cursor.description])  # Write column headers
    csv_writer.writerows(rows)  # Write data rows
