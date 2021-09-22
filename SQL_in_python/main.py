import pyodbc
from pprint import pprint

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = docker_Northwind.cursor()

cursor.execute("SELECT * "
               "FROM Customers")

row = cursor.fetchone()
# print(row)

rows = cursor.execute("SELECT *"
                      "FROM Customers").fetchall()

# pprint(rows)

rowsp = cursor.execute("SELECT *"
                       "FROM Products").fetchall()
# fetchall stores all the rows in memory so is bad as it can be thousands of rows so fill up the memory really quickly.

# for record in rowsp:
# print(record.UnitPrice)

rowsproducts = cursor.execute("SELECT *"
                              "FROM Products")
while True:
    recordone = rowsproducts.fetchone()
    if recordone is None:
        break
    print(recordone.UnitPrice)
