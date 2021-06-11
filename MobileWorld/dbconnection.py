import mysql.connector as mysqlcon
class DbConnection():
    @staticmethod
    def createConnection():


        con=mysqlcon.connect(host="localhost",user="root",passwd="root",database="mobileinfo")
        return con