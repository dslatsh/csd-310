"""
    Title: pytech_insert.py
    Author: Devin Latshaw
    Date: 6/13/2022
    Description: Will insert new documents into the student collection 
                 of mongoDB
    Steps
    1. Import MongoClient and create a DB connection
    2. Create the documents of three students with student_ids of 1007, 1008, 1009
    3. tie students to the db.students (database.students)
    4. Insert each student and provide an output of the insert statements
    5. Upon completing inserts prompt user to hit enter to close program
"""


""" Used for Import """
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.jnvyvcc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

""" Documents of the three students IDs 1007, 1008, 1009"""
# Nathan Jameson's document
nathan = {
    "student_id": "1007",
    "first_name": "Nathan",
    "last_name": "Jameson",
    "enrollment": [ 
        { 
            "term": "Winter",
            "gpa": "3.3",
            "start_date": "2022-09-15",
            "end_date": "2022-12-15",
            "course": [
                {
                    "course_id": "CIS-145",
                    "description": "Beginners to Information Technology",
                    "instructor": "James Burns",
                    "grade": "B+"
                }
            ]
        }
    ]
}

# Kory Cubin Document
kory = {
    "student_id": "1008",
    "first_name": "Kory",
    "last_name": "Cubin",
    "enrollment": [
        {
            "term": "Winter",
            "gpa": "3.42",
            "start_date": "2022-09-15",
            "end_date": "2022-12-15",
            "course": [
                {
                    "course_id": "CIS-145",
                    "description": "Beginners to Information Technology",
                    "instructor": "James Burns",
                    "grade": "B-"
                }
            ]
        }
    ]
}

# Jackie Disco's document
jackie = {
    "student_id": "1009",
    "first_name": "Jackie",
    "last_name": "Disco",
    "enrollment": [
        {
            "term": "Winter",
            "gpa": "3.89",
            "start_date": "2022-09-15",
            "end_date": "2022-12-15",
            "course": [
                {
                    "course_id": "CIS-145",
                    "description": "Beginners to Information Technology",
                    "instructor": "James Burns",
                    "grade": "A+"
                }
            ]
        }
    ]
}

students = db.students

print("\n -- INSERT STATEMENTS --")
nathan_student_id = students.insert_one(nathan).inserted_id
print(" Inserted student record Nathan Jameson into the students collection with document_id " + str(nathan_student_id))

kory_student_id = students.insert_one(kory).inserted_id
print(" Inserted student record Kory Cubin into the students collection with document_id " + str(kory_student_id))

jackie_student_id = students.insert_one(jackie).inserted_id
print(" Inserted student record Jackie Disco into the students collection with document_id " + str(jackie_student_id))

input("\n End of program, please press enter to exit")