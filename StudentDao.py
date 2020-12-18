import mysql.connector
from mysql.connector import cursor

class StudentDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'root',
            database ='datarepresentation'
        )
        print ("connection made")

    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into students (first_name, surname, grade, absences) values (%s,%s,%s, %s)"
        
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

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

    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from students where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, values):
       cursor = self.db.cursor()
       sql = "update students set first_name = %s, surname = %s, grade = %s, absences = %s where id = %s"
    #    values = [
    #        student['first_name'],
    #        student['surname'],
    #        student['grade'],
    #        student['absences']
    #    ]
       cursor.execute(sql, values)
       self.db.commit()
       

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
