"""
    Title: pytech_queries.py
    Author: Devin Latshaw
    Date: 6/13/2022
    Description: Will query the students collection located in the MongoDB cluster under pytech
"""

""" This is to import the connection using a URL string connection then creating that connection and connecting to the 
    pytech database then going to the students collection so can query"""

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students 

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

list_students = students.find({})

for doc in list_students:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")



print("\n -- DISPLAYING STUDENT DOCUMENT student_id: 1009 FROM find_one() QUERY --")

jackie = students.find_one({"student_id": "1009"})

print(" Student ID: " + jackie["student_id"] + "\n First Name: " + jackie["first_name"] + "\n Last Name: " + jackie["last_name"] + "\n")

input("\n This is the end of the program please press enter to exit")