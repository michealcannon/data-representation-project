import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class StudentDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql["host"],
            user= cfg.mysql["user"],
            password = cfg.mysql["password"],
            database =cfg.mysql["database"],
        )
        print ("connection made")

    # create student from values inputted
    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into students (first_name, surname, grade, absences) values (%s,%s,%s, %s)"
        
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # return all students from database
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from students'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    # find student using student id
    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from students where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        
    # update student info
    def update(self, values):
       cursor = self.db.cursor()
       sql = "update students set first_name = %s, surname = %s, grade = %s, absences = %s where id = %s"
       cursor.execute(sql, values)
       self.db.commit()
       
    # delete student using their id
    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from students where id = %s'
       values = [id]
       cursor.execute(sql, values)
       self.db.commit()
       return {}



    def convertToDict(self, result):
        colnames = ['id','first_name', 'surname', 'grade', 'absences']
        student = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                student[colName] = value
        return student

studentDao = StudentDao()
