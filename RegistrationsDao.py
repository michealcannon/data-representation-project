import mysql.connector
import dbconfig as cfg
class RegistrationsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )
    
    # return last entry from database
    def getOne(self):
        cursor = self.db.cursor()
        sql="select * from registrations"
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    # return account that matches values entered 
    def findOne(self, values):
        cursor = self.db.cursor()
        sql="select * from registrations where (email = %s and password = %s)"
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    # create account from values passed
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into registrations (email, password) values (%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def convertToDictionary(self, result):
        colnames=['id','email','password']
        registration = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                registration[colName] = value
        
        return registration
        
registrationsDao = RegistrationsDAO()
