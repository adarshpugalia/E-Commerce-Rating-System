'''

This code works only in the given format of the review. Any mismatch or absence of a quantity/data will throw an error.
***Required Imports: 1. python-dev libmysqlclient-dev
					 2. mysql-connector-python
'''
import json
import operator
import mysql.connector

# change the username, password and database here.
data1 = []
cnx = mysql.connector.connect(user='root', password='123', database='amazon')
cursor = cnx.cursor()

sql = "DROP TABLE IF EXISTS products";
cursor.execute(sql)

sql = "CREATE TABLE products (\
	ID CHAR(30) NOT NULL PRIMARY KEY,\
	Title VARCHAR(1000) NOT NULL)"

cursor.execute(sql)

# remove the print statements for faster execution.
i = 0
with open("./meta_Cell_Phones_and_Accessories.json") as f:
    for line in f:
    	
    	x = eval(line)
    	if 'title' in x.keys():
    		id = x["asin"]
    		title = x["title"]

    		sql = "INSERT INTO products (ID, Title) VALUES (%s, %s)"
    		data_product = (id, title)

    		cursor.execute(sql, data_product)
    		cnx.commit()
    		print i, x["title"]

    		i = i+1

cursor.close()
cnx.close()