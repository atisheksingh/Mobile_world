from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from PyQt5.uic import loadUi
import sys
from guiapps.AdminDash import Admin
class Mylogin(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("login1.ui",self)

        pixmap = QtGui.QPixmap("logo.png")
        self.lblimage.setPixmap(pixmap)

        self.btnLogin.clicked.connect(self.checkLogin)
       

    def checkLogin(self):
        ui=self.txtid.text()
        upass=self.txtpass.text()
        print(ui+" "+upass)
        if ui=="noddy" and upass=="tiger":
            # self.ad=Admin()
            # self.ad.show()
            # self.close()

            print("valid")
        else:
            print("invalid")
            msg=QMessageBox()
            msg.setWindowTitle("Errormessage")
            msg.setText("Invalid user password")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.buttonClicked.connect(self.checkButton)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setDetailedText("Detailed info")

            msg.show()
            msg.exec_()
    def checkButton(self,btn):
        caption=btn.text()
        if caption=="OK":
            print("kaam 25 haiii")

        if caption=="Cancel":
            print("clicked")




def main():

    app=QApplication(sys.argv)

    # Qapplication is a class used to provide environment  and sys.argv or [] is cumpolsary
    frame=Mylogin()
    frame.show()
    app.exec_()

    # .exec_() is used to hold the frame

if __name__ == '__main__': main()
