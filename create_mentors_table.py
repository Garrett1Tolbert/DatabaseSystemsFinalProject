import pymongo 
import csv

client = pymongo.MongoClient("mongodb://localhost:3000/")
db = client.final_project

mentors = {
"Corin":["Saraah Cooper"],
"Endia":["Vensan Cabardo", "Cynthia Sustaita" ],
"Francis":["Anthony Ong"],
"Mircea":["Eduardo Todd-Jimenez"],
"Austin":["Cornelius Cooke"],
"Ian":["Aaron Sotelo, Jonathan Mckinley"],
"Megan":["Jainel Torres", "Anita Calmday"],
"Isaac":["Jesus Nunes", "Bijesh Subedi"],
"Nauman":["Matthew King"],
"Ikenna":["Jeff Beauplan"],
"Julie":["Daniel Erhabor", "Kay Sweebe"],
"Ammar":["Kaleshwar Singh"],
"Nathan":["Kode Williams"],
"Omar":["Garrett Tolbert", "Pedro Rivera"]
}

db.Mentors.remove()
db.Students.updateMany({},{"$rename":{"Last name":"Last Name"}})

# Reading a csv file
with open('mentor_data.csv','rb') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',',quotechar='|')
    
    for row in csvreader:
        db.Mentors.insert({'First Name':row[0],'Last name':row[1],'Homes State':row[2],
                            'Undergraduate Alma Mater':row[3],'Graduate Alma Mater':row[4],'Thesis Focus':row[5],
                            'Tech Interest':row[6],'Department/Team':row[7],'Role':row[8],'Years at Google':row[9]})

        
# 1.Add current classes array to each individual student       
for mentor in mentors:
    db.Mentors.update_one({'First Name':mentor}, {"$set": {"Mentees":mentors[mentor]}}, upsert=False)

            