from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import sys
from MobileWorld.dbconnection import DbConnection as dbc
class SearchMobile(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Msearch_mobile.ui", self)
        self.con=dbc.createConnection()
        self.mycursor=self.con.cursor()

        # self.btngo.setIcon(QtGui.QIcon("tulips.jpg"))
        # pixmap=QtGui.QPixmap("tulips.jpg")
        # self.lbl_image.setPixmap(pixmap)
        self.btngo.clicked.connect(self.fetchData)
    # def checkSearch(self):
    #     pass
    def fetchData(self):
        tid=self.txtmodelnumber.text()
        print(tid)
        modelnum=(tid,)
        strsql="select*from modeldetails where ModelNumber=%s"
        self.mycursor.execute(strsql,modelnum)
        dataset=self.mycursor.fetchone()
        print(dataset)
        chk=self.mycursor.rowcount
        if chk>0:
            print("mobile exists")
            print(dataset[0])
            print(dataset[1])
            print(dataset[2])
            print(dataset[3])
            print (dataset[4])
            print(dataset[5])
            self.lblbrandid.setText(dataset[1])
            self.lblmodelname.setText(dataset[2])
            self.lblprice.setText(str(dataset[3]))
            self.lblfeatures.setText(dataset[4])
            self.lblquantity.setText(str(dataset[5]))
        else:
            print("no such id")


def main():
        app = QApplication(sys.argv)
        st=SearchMobile()
        st.show()
        app.exec_()

if __name__ == '__main__': main()