"""
    Title: pytech_update.py
    Author: Devin Latshaw
    Date: 6/22/2022
    Description: Will query the students collection located in the MongoDB cluster under pytech and then perform a last name update 
                 on Student 1007 and re-display just that student's info
"""

# This is to import the connection using a URL string connection then creating that connection and connecting to the 
# pytech database then going to the students collection so can query

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students 

# Will display a list of the students documents listing Student ID, First Name & Last Name
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

# Find all students in the list
list_students = students.find({})

# Print off students in a loop
for doc in list_students:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# Calling update command to update student_id 1007 per instructions
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Wilcox"}})

# Now we need to find the updated student doc
nathan = students.find_one({"student_id": "1007"})

# Message for displaying displaying student 1007
print("\n -- DISPLAYING UPDATED STUDENT DOCUMENT 1007 --")

# outputting the updated doc
print(" Student ID: " + nathan["student_id"] + "\n First Name: " + nathan["first_name"] + "\n Last Name: " + nathan["last_name"] + "\n")

# End of program message
input("\n This is the end of the program please press enter to exit")

