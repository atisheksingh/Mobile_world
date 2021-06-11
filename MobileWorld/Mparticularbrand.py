from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui,QtCore
import sys
from MobileWorld.dbconnection import DbConnection as dbc

class ShowBrand(QFrame):
    def __init__(self):
      super().__init__()
      loadUi("Mparticularbrand.ui",self)
      self.con = dbc.createConnection()
      self.mycursor = self.con.cursor()
      self.fetchdata()
      self.btnsearch.clicked.connect(self.searchmodel)

    def fetchdata(self):

        strsql="select brandId from brand "
        self.mycursor.execute(strsql)
        dataset=self.mycursor.fetchall()
        print(dataset)
        for i in dataset:

            self.cmbbrandname.addItems(i)
    def searchmodel(self):

        sql="select ModelName,ModelNumber from modeldetails  where brandid=%s"
        id=self.cmbbrandname.currentText()
        data=(id,)
        print(id)
        self.mycursor.execute(sql,data)
        dataset=self.mycursor.fetchall()
        print(dataset)
        self.rowcnt=len(dataset)
        print(self.rowcnt)
        self.tbl.setRowCount(self.rowcnt)
        rownum=0
        for row in dataset:
            for column in range(len(row)):
                print(row[column])
                self.tbl.setItem(rownum, column, QTableWidgetItem(row[column]))
            rownum = rownum + 1













def main():
        app = QApplication(sys.argv)
        st = ShowBrand()
        st.show()
        app.exec_()


if __name__ == '__main__': main()
