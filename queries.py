import pyodbc
import csv

server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'

conn = pyodbc.connect(
    f'DRIVER=ODBC Driver 17 for SQL Server;'
    f'SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

query = 'SELECT * FROM your_table'

cursor = conn.cursor()
cursor.execute(query)

rows = cursor.fetchall()

conn.close()

csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([column[0] for column in cursor.description])  # Write column headers
    csv_writer.writerows(rows)
