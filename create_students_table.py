import pymongo 
import csv

client = pymongo.MongoClient("mongodb://localhost:3000/")
db = client.final_project


# current classes array
classes = {
"Jesus":["Machine Learning", "Software Enginnering", "Database Systems", "Theory Of Computation", "Technical Interview"],
"Arianna":["Machine Learning", "Software Enginnering", "Mobile Apps", "Database Systems", "Technical Interview"],
"Marco":["Machine Learning", "Software Enginnering", "Mobile Apps", "Product Management", "Technical Interview"],
"Cynthia":["Machine Learning", "Mobile Apps", "Database Systems", "Product Management", "Technical Interview"],
"Jacob":["Machine Learning", "Mobile Apps", "Database Systems", "Product Management", "Technical Interview"],
"Ruel":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Database Systems", "Theory Of Computation", "Technical Interview"],
"Aaron":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Theory Of Computation", "Technical Interview"],
"Jorde":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Theory Of Computation", "Technical Interview"],
"Fernando":["Machine Learning", "Mobile Apps", "Product Management", "Theory Of Computation"],
"Lianne":["Machine Learning", "Software Enginnering", "Mobile Apps", "Product Management", "Technical Interview"],
"Kristalys":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps"],
"Joshua":["Machine Learning", "Fundamentals of Algorithms", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Pedro":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Product Management", "Technical Interview"],
"Cornelius":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Technical Interview"],
"Garrett":["Fundamentals of Algorithms", "Software Enginnering", "Database Systems", "Theory Of Computation"],
"Tabia":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Product Management", "Theory Of Computation", "Technical Interview"],
"Kay":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Product Management", "Technical Interview"],
"Kishor":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Saraah":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Database Systems", "Theory Of Computation", "Technical Interview"],
"Victoria":["Product Management"],
"Anthony":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Database Systems", "Theory Of Computation", "Technical Interview"],
"Jainel":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Database Systems", "Technical Interview"],
"Cicely":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Product Management", "Theory Of Computation"],
"Anita":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Peace":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Database Systems", "Theory Of Computation", "Technical Interview"],
"Biswash":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Product Management", "Theory Of Computation", "Technical Interview"],
"Taylor":["Software Enginnering", "Mobile Apps", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Chris":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Technical Interview"],
"Morgan":["Machine Learning", "Fundamentals of Algorithms", "Database Systems", "Product Management", "Technical Interview"],
"Michael":["Machine Learning", "Fundamentals of Algorithms", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Maya":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Kiara":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Shaunelle":["Fundamentals of Algorithms", "Software Enginnering", "Mobile Apps", "Database Systems", "Product Management", "Theory Of Computation", "Technical Interview"],
"Shumba":["Machine Learning", "Fundamentals of Algorithms", "Software Enginnering", "Database Systems", "Product Management", "Theory Of Computation"],
"Kode":["Machine Learning", "Fundamentals of Algorithms", "Database Systems", "Theory Of Computation", "Technical Interview"]
}

languages = [
    {"Java":"Expert","Python":"Intermediate","C++":"Beginner","HTML/CSS":"Expert","JavaScript":"Intermediate"},
    {"Java":"Expert","Python":"Beginner","C++":"Expert","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Beginner","C++":"Beginner","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Beginner","C++":"N/A","HTML/CSS":"N/A","JavaScript":"N/A"},
    {"Java":"Expert","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Beginner","JavaScript":"N/A"},
    {"Java":"Beginner","Python":"Expert","C++":"Expert","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"Expert","Python":"Intermediate","C++":"Beginner","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Expert","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Expert","JavaScript":"Intermediate"},
    {"Java":"Expert","Python":"Intermediate","C++":"N/A","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Expert","Python":"Intermediate","C++":"N/A","HTML/CSS":"N/A","JavaScript":"Beginner"},
    {"Java":"Expert","Python":"Expert","C++":"N/A","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Beginner","Python":"Intermediate","C++":"N/A","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"Expert","Python":"Intermediate","C++":"N/A","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"N/A","Python":"N/A","C++":"Intermediate","HTML/CSS":"Beginner","JavaScript":"N/A"},
    {"Java":"N/A","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Expert","JavaScript":"Intermediate"},
    {"Java":"Beginner","Python":"Intermediate","C++":"Intermediate","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Beginner","Python":"Intermediate","C++":"N/A","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Beginner","Python":"Intermediate","C++":"Intermediate","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Beginner","Python":"Intermediate","C++":"Beginner","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Expert","Python":"Intermediate","C++":"Beginner","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Expert","Python":"Intermediate","C++":"Beginner","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Beginner","C++":"Expert","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Intermediate","Python":"Intermediate","C++":"Intermediate","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Intermediate","Python":"Intermediate","C++":"Expert","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Beginner","Python":"Beginner","C++":"Beginner","HTML/CSS":"Intermediate","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Beginner","C++":"Expert","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"N/A","Python":"Intermediate","C++":"Beginner","HTML/CSS":"Beginner","JavaScript":"N/A"},
    {"Java":"N/A","Python":"Intermediate","C++":"Beginner","HTML/CSS":"N/A","JavaScript":"N/A"},
    {"Java":"Beginner","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"N/A","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Beginner","JavaScript":"Beginner"},
    {"Java":"Beginner","Python":"Beginner","C++":"Intermediate","HTML/CSS":"Expert","JavaScript":"Beginner"},
    {"Java":"Intermediate","Python":"Intermediate","C++":"Intermediate","HTML/CSS":"Intermediate","JavaScript":"Intermediate"},
    {"Java":"Intermediate","Python":"Intermediate","C++":"Expert","HTML/CSS":"Expert","JavaScript":"Expert"}
]


db.Students.remove()
db.Students.updateMany({},{"$rename":{"Last name":"Last Name"}})
count = 0

# Reading a csv file
with open('student_data.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',',quotechar='|')
    
    for row in csvreader:
        db.Students.insert({'First Name':row[0],'Last name':row[1],'School':row[2],
                            'Home State':row[3],'Horoscope':row[4],'Favorite Cuisine':row[5],
                            'Type of Diet':row[6],'Favorite Music Genre':row[7]})

        
# 1.Add current classes array to each individual student       
# 2.Add programming languages as an embedded document to each individual student       
for student in classes:
    db.Students.update_one({'First Name':student}, {"$set": {"Current Classes":classes[student]}}, upsert=False)
    db.Students.update_one({'First Name':student}, {"$set": {"Progamming Languages":languages[count]}}, upsert=False)
    count += 1
            
for student in db.Students.find():
#     print(student["Current Classes"])
    if len(student["Current Classes"]) < 4:
        db.Students.update_one({'First Name':student["First Name"]}, {"$set": {"Full Time":0}}, upsert=False)
    else:
        db.Students.update_one({'First Name':student["First Name"]}, {"$set": {"Full Time":1}}, upsert=False)
