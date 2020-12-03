import mysql.connector
from mysql.connector import cursor

class BookDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'root',
            database ='datarepresentation'
        )
        print ("connection made")

    def create(self, book):
        cursor = self.db.cursor()
        sql = "insert into books (title, author, price) values (%s,%s,%s)"
        values = [
            book['title'],
            book['author'],
            book['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from books'
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
        sql = 'select * from books where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, book):
       cursor = self.db.cursor()
       sql = "update books set title = %s, author = %s, price = %s"
       values = [
           book['title'],
           book['author'],
           book['price'],
           

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return book

    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from books where id = %s'
       values = [id]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['id','title', 'author', 'price']
        book = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                book[colName] = value
        return book

bookDao = BookDao()
