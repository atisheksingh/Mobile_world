from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from MobileWorld.dbconnection import DbConnection as dbc
import sys
class ClientDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Madd.ui",self)
        self.con=dbc.createConnection()
        self.mycursor=self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchData)
    def fetchData(self):
        self.modelnumber=self.txtmodelnumber.text().strip()
        self.quantity=self.txtquantity.text().strip()
        self.customername=self.txtcustomername.text().strip()
        self.email=self.txtemail.text().strip()
        self.address=self.txtaddress.text().strip()
        self.phone=self.txtphone.text().strip()
        self.date=self.txtdate.text().strip()
        if len(self.modelnumber)==0 or len(self.quantity)==0 or len(self.customername)==0 or len(self.email)==0 or len(self.address)==0 or len(self.phone)==0 or len(self.date)==0:
            self.showMessage("Error","Data Needed")
        else:
            strinsert="insert into sales(ModelNumber, Quantity, CustomerName, Email, Address, Phone, Date)values(%s,%s,%s,%s,%s,%s,%s)"
            self.mycursor.execute(strinsert,(self.modelnumber,int(self.quantity),self.customername,self.email,self.address,self.phone,self.date))
            self.con.commit()
            self.showMessage("insertion","row inserted succerssfully")

            strupdate="update modeldetails set quantity=quantity-%s where modelnumber=%s"
            self.mycursor.execute(strupdate,(int(self.quantity),self.modelnumber))
            self.con.commit()
            print("data updated")



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
    frame=ClientDetails()
    frame.show()
    app.exec_()

if __name__ == '__main__':main()

