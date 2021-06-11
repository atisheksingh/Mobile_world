from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from MobileWorld.MAdd_Brand import BrandDetails
from MobileWorld.Madd_model import ModelDetails
from MobileWorld.MAddnew import ClientDetails
from MobileWorld.Mparticularbrand import ShowBrand
from MobileWorld.Msearch_mobile import SearchMobile
from MobileWorld.Msearchsoldmobile import soldmobiles
from MobileWorld.Mbargraph import Mobilerating

import sys
class Admin(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("Mmainwindow.ui",self)
        self.btnAbrand.clicked.connect(self.Addbrand)
        self.btnAmodel.clicked.connect(self.Addmodel)
        self.btnAcustomer.clicked.connect(self.Addcustomer)
        self.btnSmodel.clicked.connect(self.Seeparticularbrand)
        self.btnSdetails.clicked.connect(self.Seeparticularmodel)
        self.btnScustomer.clicked.connect(self.Seecustomer)
        self.btngraph.clicked.connect(self.Seegraph)
    def Addbrand(self):
        self.t=BrandDetails()
        self.t.show()

    def Addmodel(self):
        self.p=ModelDetails()
        self.p.show()

    def Addcustomer(self):
        self.p = ClientDetails()
        self.p.show()

    def Seeparticularbrand(self):
        self.p=ShowBrand()
        self.p.show()

    def Seeparticularmodel(self):
        self.p=SearchMobile()
        self.p.show()

    def Seecustomer(self):
        self.p=soldmobiles()
        self.p.show()

    def Seegraph(self):
        self.p=Mobilerating()
        self.p.showChart()


def main():
    app=QApplication(sys.argv)
    admin=Admin()
    admin.show()
    app.exec_()

if __name__ == '__main__':main()
