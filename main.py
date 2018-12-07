import pymongo 
import sys
import csv

client = pymongo.MongoClient("mongodb://localhost:3000/")
db = client.final_project
students = db["Students"]
mentors = db["Mentors"]
classes = db["Classes"]

def showMenu():
    # Show menu
    print("\n****************Main Menu*********************")
    print("\nSelect one of the options below to get started\n ")
    print("1.) Insert\n2.) Find Documents\n3.) Update\n4.) Delete\n5.) Aggregation\n")
    print("Press 'x' to exit program\n")
    selected_option = raw_input()
    runQuery(selected_option)
    
def runQuery(selected_option):
    if selected_option == "x":
        sys.exit()
    elif selected_option == "1":
        Insert()
    elif selected_option == "2":
        Find()
    elif selected_option == "3":
        Update()
    elif selected_option == "4":
        Delete()
    elif selected_option == "5":
        Aggregate()
    else:
        print("\nInvalid Choice. Please try again.")
        showMenu()

        
def Insert():
    print("\nWhich would you like to add to?")
    print("\na.) Student\nb.) Mentor\nc.) Class\n")
    
    insert_option = raw_input()
    
    if insert_option == 'a':
        insertStudent()
    elif insert_option == 'b':
        insertMentor()
    elif insert_option == 'c':
        insertClass()
    else:
        print("\nInvalid Choice. Please try again.")
        Insert()
    
def insertStudent():
    new_student = {"First Name":raw_input("First Name: "),"Last Name":raw_input("Last Name: "),
                  "School":raw_input("School: "),"Current Classes":raw_input("Current Classes: ").split(','),"Home State":raw_input("Home State: "),"Horoscope: ":raw_input("Horoscope: "),
                  "Type of Diet":raw_input("Typeof Diet: "),"Favorite Music Genre": raw_input("Favorite Music Genre: "),
                  "Favorite Cuisine":raw_input("Favorite Cuisine: "),
                   "Programming Languages":{"Python":raw_input("Python: "),"Java":raw_input("Java: "),"JavaScript":raw_input("JavaScript: "),
                                           "C++":raw_input("C++: "),"HTML/CSS":raw_input("HTML/CSS: ")}}
    
    students.insert_one(new_student)
    print "\n",new_student["First Name"]," has been added to [Students]."

def insertMentor():
    new_mentor = {"First Name":raw_input("First Name: "),"Last Name":raw_input("Last Name: "),"Home State":raw_input("Home State: "),
                 "Undergraduate Alma Mater":raw_input("Undergraduate Alma Mater: "),"Graduate Alma Mater":raw_input("Graduate Alma Mater: "),"Thesis Focus":raw_input("Thesis Focus: "),
                 "Tech Interest":raw_input("Tech Interest: "),"Department/Team":raw_input("Department/Team: "),"Role":raw_input("Role: "),"Years at Google":raw_input("Years at Google: "),"Mentees":raw_input("Mentees: ").split(',')}
    
    mentors.insert_one(new_mentor)
    print "\n",new_mentor["First Name"]," has been added to [Mentors]."

def insertClass():
    new_class = {"Course Number":raw_input("Course Number: "),"Course Name":raw_input("Course Name: "),"Instructor":raw_input("Instructor: ")}
    
    classes.insert_one(new_class)
    print "\n",new_class["Course Name"]," has been added to [Classes]."

    
def Find():
    print("\nWhat would you like to find?")
    print("\na.) Student\nb.) Mentor\nc.) Class\n")
    
    insert_option = raw_input()
    
    if insert_option == 'a':
        findStudent()
    elif insert_option == 'b':
        findMentor()
    elif insert_option == 'c':
        findClass()
    else:
        print("\nInvalid Choice. Please try again.")
        Find()    

def findStudent():
    category = raw_input("\nWhat would you like to search for (Last Name, Home State, etc.)? ")
    if category == "Programming Languages":
        specified_language = raw_input("\nWhich language are you looking for? ")
        new_filter = raw_input("\nProficiency Level: ")
    else:
        new_filter = raw_input("\nWhat are you trying to find? ")
        
    stud_results = []
    
    if category == "Current Classes":
        for student in students.find():
            if new_filter in student[category]:
                stud_results.append(student)
    elif category == "Programming Languages":
        for student in students.find():
            if student[category][specified_language] == new_filter:
                stud_results.append(student)        
    else:
        for student in students.find():
            if student[category] == new_filter:
                stud_results.append(student)

    if len(stud_results) == 0:
        print "Sorry, no results were found."
    else:            
        print "\nHere are the results:"
        for x in stud_results:
            print x["First Name"],x["Last Name"]        

def findMentor():
    category = raw_input("\nWhat would you like to search for (Last Name, Home State, etc.)? ")
    new_filter = raw_input("\nWhat are you trying to find? ")
    ment_results = []
    
    if category == "Mentees":
        for mentor in mentors.find():
            if new_filter in mentor[category]:
                ment_results.append(mentor)        
    else:
        for mentor in mentors.find():
            if mentor[category] == new_filter:
                ment_results.append(mentor)
    
    if len(ment_results) == 0:
        print "Sorry, no results were found."
    else:
        print "\nHere are the results:"
        for x in ment_results:
            print x["First Name"],x["Last Name"]        
        
def findClass():
    category = raw_input("\nWhat would you like to search for (Course Number or Instructor)? ")
    
    if category == "Course Number":
        new_filter = raw_input("\nCourse Number: ")
    else:
        new_filter = raw_input("\nInstructor: ")

    class_results = []
    
    for this_class in classes.find():
        if this_class[category] == new_filter:
            class_results.append(this_class)
    
    if len(class_results) == 0:
        print "Sorry, no results were found."
    else:
        print "\nHere are the results:"
        for x in class_results:
            print x["Course Name"]  
        
        
def Update():
    print("\nWhich would you like to update?")
    print("\na.) Student\nb.) Mentor\nc.) Class\n")
    
    update_option = raw_input()
    
    if update_option == 'a':
        updateStudent()
    elif update_option == 'b':
        updateMentor()
    elif update_option == 'c':
        updateClass()
    else:
        print("\nInvalid Choice. Please try again.")
        Update()    
    
def updateStudent():
    curr_student = raw_input("\nWhich student's record would you like to update? ")
    
    for student in students.find():
        if student["First Name"] == curr_student:
            update_student = student
    
    update_field = raw_input("\nWhat would you like to update? ")
    question = "\n" + update_field + ": "
    students.update_one({'First Name':curr_student}, {"$set": {update_field:raw_input(question)}}, upsert=False)

    print "\nRecord successfully updated."

def updateMentor():
    curr_mentor = raw_input("\nWhich mentor's record would you like to update? ")
    
    for mentor in mentors.find():
        if mentor["First Name"] == curr_mentor:
            update_mentor = mentor
    
    update_field = raw_input("\nWhat would you like to update? ")
    question = "\n" + update_field + ": "
    mentors.update_one({'First Name':curr_mentor}, {"$set": {update_field:raw_input(question)}}, upsert=False)

    print "\nRecord successfully updated."    
    
def updateClass():
    curr_class = raw_input("\nCourse number you'd like to update? ")
    
    for this_class in classes.find():
        if this_class["Course Number"] == curr_class:
            update_class = this_class
    
    update_field = raw_input("\nWhat would you like to update? ")
    question = "\n" + update_field + ": "
    classes.update_one({'First Name':curr_class}, {"$set": {update_field:raw_input(question)}}, upsert=False)

    print "\nRecord successfully updated."    
    
    
def Delete():
    print("\nWhich would you like to delete to?")
    print("\na.) Student\nb.) Mentor\nc.) Class\n")
    
    delete_option = raw_input()
    
    if delete_option == 'a':
        deleteStudent()
    elif delete_option == 'b':
        deleteMentor()
    elif delete_option == 'c':
        deleteClass()
    else:
        print("\nInvalid Choice. Please try again.")
        Insert()    
    
def deleteStudent():
    curr_student = raw_input("\nWhich student would you like to delete? ")
    delete_student = None
    
    for student in students.find():
        if student["First Name"] == curr_student:
            delete_student = student
    
    if delete_student == None:
        print "\nNo record was found for ",curr_student
    else:
        students.delete_one(delete_student)
        print "\nRecord successfully deleted from [Students]."
    
def deleteMentor():
    curr_mentor = raw_input("\nWhich mentor would you like to delete? ")
    delete_mentor = None
    
    for mentor in mentors.find():
        if mentor["First Name"] == curr_mentor:
            delete_mentor = mentor
    
    if delete_mentor == None:
        print "\nNo record was found for ",curr_mentor
    else:
        mentors.delete_one(delete_mentor)
        print "\nRecord successfully deleted from [Mentors]."
        
def deleteClass():
    curr_class = raw_input("\nCourse Number you'd like to delete? ")
    delete_class = None
    
    for this_class in classes.find():
        if this_class["Course Number"] == curr_class:
            delete_class = this_class
    
    if delete_class == None:
        print "\nNo record was found for ",curr_class
    else:
        classes.delete_one(delete_class)
        print "\nRecord successfully deleted from [Classes]."
    
        
def Aggregate():
    print("\nWhich would you like to aggregate?")
    print("\na.) Students\nb.) Mentors\nc.) Classes\n")
    
    agg_option = raw_input()
    
    if agg_option == 'a':
        aggStudents()
    elif agg_option == 'b':
        aggMentors()
    elif agg_option == 'c':
        aggClasses()
    else:
        print("\nInvalid Choice. Please try again.")
        Aggregate()    

def aggStudents():
    print("\nWhich aggregation method would you like to use? ")
    method = raw_input("Available methods include 'group','sort': ")
    

    if method == "group":
        group_by = raw_input("\nGroup by: ")
            
        results = students.aggregate([
            
                {"$group":{"_id":"$"+group_by}}            
        ])
        print "\nHere are the results:"
        for x in results:
            print(x[u"_id"]) 
        
    elif method == "sort":
        sort_by = raw_input("\nSort by: ")
        order_input = raw_input("Ascending or Descending? ")
        if order_input == "Ascending":
            viewOrder = 1
        else:
            viewOrder = -1
    
        results = students.find().sort(sort_by,viewOrder)     
        
        print "\nHere are the results:"
        for x in results:
            print(x[sort_by])

def aggMentors():
    print("\nWhich aggregation method would you like to use? ")
    method = raw_input("Available methods include 'group','sort': ")
    

    if method == "group":
        group_by = raw_input("\nGroup by: ")
            
        results = mentors.aggregate([
            
                {"$group":{"_id":"$"+group_by}}            
        ])
        
        print "\nHere are the results:"
        for x in results:
            print(x[u"_id"]) 
            
    elif method == "sort":
        sort_by = raw_input("\nSort by: ")
        order_input = raw_input("Ascending or Descending? ")
        if order_input == "Ascending":
            viewOrder = 1
        else:
            viewOrder = -1
    
        results = mentors.find().sort(sort_by,viewOrder)     
        
        print "\nHere are the results:"
        for x in results:
            print(x[sort_by])        

def aggClasses():
    print("\nWhich aggregation method would you like to use? ")
    method = raw_input("Available methods include 'group','sort': ")
    

    if method == "group":
        group_by = raw_input("\nGroup by: ")
            
        results = classes.aggregate([
            
                {"$group":{"_id":"$"+group_by}}            
        ])
        
        print "\nHere are the results:"
        for x in results:
            print(x[u"_id"]) 
            
    elif method == "sort":
        sort_by = raw_input("\nSort by: ")
        order_input = raw_input("Ascending or Descending? ")
        if order_input == "Ascending":
            viewOrder = 1
        else:
            viewOrder = -1
    
        results = classes.find().sort(sort_by,viewOrder)     
        
        print "\nHere are the results:"
        for x in results:
            print(x[sort_by])        
            
        
while True:        
    showMenu()
    