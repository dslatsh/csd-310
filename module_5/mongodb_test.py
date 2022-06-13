from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List -- \n", 
db.list_collection_names())
<<<<<<< HEAD
input("Program has finished please press enter to exit....")
=======
input("Program has finished please press enter to exit....")
>>>>>>> 6e0123ad6bd62b61c1c766ddf54bcf37e3ff11e0
