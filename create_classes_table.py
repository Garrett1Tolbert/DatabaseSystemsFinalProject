import pymongo 
import csv

client = pymongo.MongoClient("mongodb://localhost:3000/")
db = client.final_project


db.Classes.remove()

# Reading a csv file
with open('classes_data.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',',quotechar='|')
    
    for row in csvreader:
        db.Classes.insert({'Course Number':row[0],'Course Name':row[1],'Instructor':row[2]})


            