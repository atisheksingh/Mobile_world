from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from MobileWorld.dbconnection import DbConnection as dbc
import sys
class ModelDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Madd_model.ui",self)
        self.con=dbc.createConnection()
        self.mycursor=self.con.cursor()

        # self.btndelete.setIcon(QtGui.QIcon("tulips.jpg"))
        pixmap = QtGui.QPixmap("wallpaper.jpg")
        self.lbl_image.setPixmap(pixmap)


        self.btnsubmit.clicked.connect(self.fetchData)
    def fetchData(self):
        self.modelnumber=self.txtmodelnumber.text().strip()
        self.brandid=self.txtbrandid.text().strip()
        self.modelname=self.txtmodelname.text().strip()
        self.price=self.txtprice.text().strip()
        self.features=self.txtfeatures.text().strip()
        self.quantity=self.txtquantity.text().strip()

        if len(self.modelnumber)==0 or len(self.brandid)==0 or len(self.modelname)==0 or len(self.price)==0 or len(self.features)==0 or len(self.quantity)==0:
            self.showMessage("Error","Data Needed")
        else:
            strinsert="insert into modeldetails(ModelNumber, BrandId, ModelName, Price, Features, Quantity)values(%s,%s,%s,%s,%s,%s)"
            self.mycursor.execute(strinsert,(self.modelnumber,self.brandid,self.modelname,float(self.price),self.features,int(self.quantity)))
            self.con.commit()
            self.showMessage("insertion","row inserted succerssfully")
    #
    #

    def showMessage(self,title,message):
        msg=QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()
       #
       # print(self.name,self.email,self.phone,self.age)

def main():
    app=QApplication(sys.argv)
    frame=ModelDetails()
    frame.show()
    app.exec_()

if __name__ == '__main__':main()

