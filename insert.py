import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'FAITH KARIMI',23,3450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'BOB KURIA',32,150000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'JANE MUTHONI',23,40000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'MARY ANNE',28,280000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'PAUL KAMAU',25,3450000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()