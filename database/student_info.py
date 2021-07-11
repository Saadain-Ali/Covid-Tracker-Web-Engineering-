from sqlite3.dbapi2 import DatabaseError
import student
from database.csv_editor import csv_editor as editor
import sqlite3

class data_handle:


    def __init__(self,name,bloodtype,location,country,recoverydate,gender):
        self.name = name 
        self.bloodtype = bloodtype 
        self.location  = location  
        self.country  = country
        self.recoverydate = recoverydate
        self.gender  = gender 
    
    def store_to_DB(self):
        """
        write code to store data to db on runtime
        """
        with sqlite3.connect('database/covid.db') as conn:
           _query = f"""
              INSERT INTO finds (name,bloodtype,location,country,recoverydate,gender)
                VALUES({self.name},'{self.bloodtype},'{self.location}','{self.country}'','{self.recoverydate}','{self.gender}');
               """
           row = []
           try:
               cursor = conn.execute(_query)
               conn.commit()
               row = cursor.lastrowid()
               print("row is added swith success",end='')
               print(row)
           except DatabaseError as identifier:
               print("error " + str(identifier))
           finally:
               return row
    # make it a seperate thread
    def getData(self,name):
        row = []
        conn = sqlite3.connect('database/covid.db')
        # print("Opened database successfully")
        cursor = conn.execute("SELECT name,bloodtype,location,country,recoverydate,gender From student WHERE name = " + '"' + name + '"')
        row = cursor.fetchone()
        # print(row)
        conn.close()
        if row:
            return {
                'name' :  row[0] ,
                'bloodtype' :   row[1],
                'location':  row[2],
                'country' :   row[3],
                'recoverydate' :     row[4],
                'gender' :  row[5]
            }
        return None

    def getDataByCountry(self,country):
        row = []
        conn = sqlite3.connect('database/covid.db')
        # print("Opened database successfully")
        cursor = conn.execute("SELECT name,bloodtype,location,country,recoverydate,gender From student WHERE country = " + '"' + country + '"')
        row = cursor.fetchone()
        # print(row)
        conn.close()
        if row:
            return {
                'name' :  row[0] ,
                'bloodtype' :   row[1],
                'location':  row[2],
                'country' :   row[3],
                'recoverydate' :     row[4],
                'gender' :  row[5]
            }
        return None

    def getDataByLocation(self,location):
        row = []
        conn = sqlite3.connect('database/covid.db')
        # print("Opened database successfully")
        cursor = conn.execute("SELECT name,bloodtype,location,country,recoverydate,gender From student WHERE location = " + '"' + location + '"')
        row = cursor.fetchone()
        # print(row)
        conn.close()
        if row:
            return {
                'name' :  row[0] ,
                'bloodtype' :   row[1],
                'location':  row[2],
                'country' :   row[3],
                'recoverydate' :     row[4],
                'gender' :  row[5]
            }
        return None