from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List -- \n", 
db.list_collection_names())