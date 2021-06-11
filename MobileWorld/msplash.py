from PyQt5.QtWidgets import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QPixmap


import sys
import time
from MobileWorld.mlogin import Mylogin

def main():





    app=QApplication(sys.argv)


    splash_pix=QPixmap("tulips.jpg")
    splash=QSplashScreen(splash_pix)


    current_window_flags=splash.windowFlags()
    splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | current_window_flags)

    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(80)
    splash.setFont(font)

    splash.showMessage('welcome...',QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom,QtGui.QColor.fromRgb(150,100,100))

    splash.show()



    import xlrd
    import pyttsx as p
    engine = p.init()  # object creation

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume',10)
    engine.say("welcome to the future")
    engine.setProperty('rate', 100)
    engine.runAndWait()
    engine.stop()


    app.processEvents()
    import time
    time.sleep(4)
    login=Mylogin()
    login.show()
    splash.finish(login)
    app.exec_()




if __name__ == '__main__':main()
