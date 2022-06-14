"""
  Title: mongodb_test.py
  Author: Devin Latshaw
  Date: 6/12/2022
  Description: Creates a connction to the mongoDB using the below connection string
               it will then connect to the client.pytech database and print out the collection list
"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List -- \n", 
db.list_collection_names())
input("Program has finished please press enter to exit....")
