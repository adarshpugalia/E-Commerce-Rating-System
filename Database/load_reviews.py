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

sql = "DROP TABLE IF EXISTS reviews";
cursor.execute(sql)

sql = "CREATE TABLE reviews (\
    reviewID VARCHAR(30) NOT NULL,\
    unixReviewTime VARCHAR(30) NOT NULL,\
    asin VARCHAR(30) NOT NULL,\
    review VARCHAR(50000) NOT NULL,\
	PRIMARY KEY (reviewID, unixReviewTime))"

cursor.execute(sql)

# remove the print statements for faster execution.
i = 0
with open("./reviews_Cell_Phones_and_Accessories.json") as f:
    for line in f:
    	
    	x = eval(line)
    	if 'reviewerID' in x.keys() and 'asin' in x.keys() and 'reviewText' in x.keys() and 'unixReviewTime' in x.keys():
    		id = x["reviewerID"]
		asin = x["asin"]
            	review = x["reviewText"]
            	uTime = x["unixReviewTime"]
		
		try:
        		sql = "INSERT INTO reviews (reviewID, unixReviewTime, asin, review) VALUES (%s, %s, %s, %s)"
        		data_product = (id, uTime, asin, review)

        		cursor.execute(sql, data_product)
		except mysql.connector.IntegrityError:
                	cnx.rollback()
		else:
			cnx.commit()
			print i, x["reviewText"]
			i = i+1

cursor.close()
cnx.close()
