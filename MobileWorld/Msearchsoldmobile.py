from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui,QtCore
import sys
from MobileWorld.dbconnection import DbConnection as dbc

class soldmobiles(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Msearch_soldmobile.ui",self)
        self.con=dbc.createConnection()
        self.mycursor = self.con.cursor()
        # self.fetchdata()
        self.btngo.clicked.connect(self.searchsoldmodel)

    def searchsoldmodel(self):
        strsql="select* from sales"
        self.mycursor.execute(strsql)
        dataset = self.mycursor.fetchall()
        print(dataset)
        # following code is for number of rows 
        self.rowcnt = len(dataset)
        print(self.rowcnt)
        self.tbl.setRowCount(self.rowcnt)
        rownum = 0
        for row in dataset:
            for column in range(len(row)):
                print(row[column])
                self.tbl.setItem(rownum, column, QTableWidgetItem(str((row[column]))))
            rownum = rownum + 1

def main():
    app = QApplication(sys.argv)
    st = soldmobiles()
    st.show()
    app.exec_()


if __name__ == '__main__': main()