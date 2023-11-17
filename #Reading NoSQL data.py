#This example uses the pymongo module
#to read files stored in MongoDB, although
#there are several other packages available.
#We first make a connection with the databasse
#(MongoDB needs to be running)

#Data is read into pandas by combining
#a query with this connection.

#Here, Query should be replaced with a
#MongoDB query string (or {} to select all)


from pymongo import MongoClient

con = MongoClient()

db= con.database_name

cursor = db.collection_name.find(query)

df=pd.DataFrame(list(cursor))