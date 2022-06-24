"""
    Title: pytech_delete.py
    Author: Devin Latshaw
    Date: 6/23/2022
    Description: Makes connection to mongoclient, will query the list of student documents then takes 
                 jimmy document and inserts it into the cluster, queries the one student id 1010 to make sure
                 it was inserted, then will delete jimmy and queries the all the documents again to show he is gone
"""
#Used to make the countdown timer for deletion
import sys
import time

# This is to import the connection using a URL string connection then creating that connection and connecting to the 
# pytech database then going to the students collection so can query
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students 

#Creating a the student id 1010 document
jimmy = {
    "student_id": "1010",
    "first_name": "Jimmy",
    "last_name": "Dean",
    "enrollment": [
        {
            "term": "Winter",
            "gpa": "2.25",
            "start_date": "2022-09-15",
            "end_date": "2022-12-15",
            "course": [
                {
                    "course_id": "CIS-145",
                    "description": "Beginners to Information Technology",
                    "instructor": "James Burns",
                    "grade": "D"
                }
            ]
        }
    ]
}

# Will display a list of the students documents listing Student ID, First Name & Last Name
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

list_students = students.find({})

for doc in list_students:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# Insert the student ID for jimmy 1010
print("\n -- INSERT STATEMENTS --")
jimmy_student_id = students.insert_one(jimmy).inserted_id
print(" Inserted student record Jimmy Dean into the students collection with document_id " + str(jimmy_student_id))

# Will query and display one student in this case Student ID 1010 and list Student ID, First Name & Last Name
print("\n -- DISPLAYING STUDENT DOCUMENT student_id: 1010 FROM find_one() QUERY --")

jimmy = students.find_one({"student_id": "1010"})

print(" Student ID: " + jimmy["student_id"] + "\n First Name: " + jimmy["first_name"] + "\n Last Name: " + jimmy["last_name"] + "\n")

# Deleting 1010 student
print("\n --- DELETING STUDENT ID 1010 ---")
print("Deleting student ID 1010, give me a few seconds....")
for i in range(3,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)
jimmy_student_id_delete = students.delete_one({"student_id": "1010"})
print("\nJimmy is outta here!!!")


# Requery the students list and display them
list_students = students.find({})
print("\n -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY AFTER ID 1010 DELETION --")

for doc in list_students:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# Exiting message
input("\nThis is the end for you my friend, please press enter to exit....")