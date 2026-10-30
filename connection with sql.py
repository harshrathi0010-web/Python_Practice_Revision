"""
SQL interaction
MySQL

for mySQL install dependencies
pip install mysql.connector
pip install mysql.connector.python


"""

import mysql.connector

conn=mysql.connector.connect(
    host="localhost",  # 127.0.0.1
    port="3306",
    user="root",
    password="1234",
    database="sales")

print(conn)

# for going to mysql by the python we need cursor

cur=conn.cursor()

# =========
# task

query="select*from customers"
cur.execute(query)
data=cur.fetchall()
for emp in data:
    print(emp)

# 
cur.close()
conn.close()








 
