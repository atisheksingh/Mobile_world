import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from MobileWorld.dbconnection import DbConnection as dbc

class Mobilerating():
    def __init__(self):
        # super.__init__()
        self.con=dbc.createConnection()
        self.mycursor=self.con.cursor()
        self.finddetails()

    def finddetails(self):
        strsql="SELECT sum(s.Quantity) as total ,m.brandid from sales s, modeldetails m WHERE s.ModelNumber=m.ModelNumber group by m.brandid;"
        self.mycursor.execute(strsql)
        dataset=self.mycursor.fetchall()
        print(dataset)
        self.sales = []
        self.brands = []
        for i in dataset:
            self.sales.append(i[0])
            self.brands.append(i[1])
        print(self.sales)
        print(self.brands)




    def showChart(self):
        # placerating=pd.read_excel("Ratings.xlsx",sheet_name="Place")
        # print(placerating)
        plt.xlabel("brandNames")
        plt.ylabel("sold quantity")
        plt.title("Mobile rating")
        plt.bar(self.brands,self.sales)
        plt.show()




def main():
    p=Mobilerating()
    p.showChart()
    #p.finddetails()

if __name__ == '__main__':main()