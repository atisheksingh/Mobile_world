from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from MobileWorld.dbconnection import DbConnection as dbc
import sys
class BrandDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Madd_Brand.ui",self)
        self.con=dbc.createConnection()
        self.mycursor=self.con.cursor()

        pixmap = QtGui.QPixmap("wallpaper1.jpg")
        self.lblimage.setPixmap(pixmap)


        self.btnadd.clicked.connect(self.fetchData)
    def fetchData(self):
        self.brandid=self.txtbrandid.text().strip()
        self.brandname=self.txtbrandname.text().strip()
        # self.customername=self.txtcustomername.text().strip()
        # self.email=self.txtemail.text().strip()
        # self.address=self.txtaddress.text().strip()
        # self.phone=self.txtphone.text().strip()
        # self.date=self.txtdate.text().strip()
        if len(self.brandid)==0 or len(self.brandname)==0 :
            self.showMessage("Error","Data Needed")
        else:
            strinsert="insert into brand(BrandId, BrandName)values(%s,%s)"
            self.mycursor.execute(strinsert,(self.brandid,self.brandname))
            self.con.commit()
            self.showMessage("insertion","row inserted succerssfully")



    def showMessage(self,title,message):
        msg=QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

       # print(self.name,self.email,self.phone,self.age)

def main():
    app=QApplication(sys.argv)
    frame=BrandDetails()
    frame.show()
    app.exec_()

if __name__ == '__main__':main()

