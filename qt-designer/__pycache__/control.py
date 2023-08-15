import mainwindow
from auto_mechine import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# 按鈕
global a 
a = 0 

def button_click():
    print("hello world")
#     回覆視窗
#     messageBox = QMessageBox()  
#     messageBox.setWindowTitle("正確")
#     messageBox.setInformativeText("Fuck World")
#     messageBox.exec_()
#     ui.label.setText("按鈕被點了")
    global a 
    a += 1
    if a%2 == 0:
        ui.label.setText("<html><head/><body><p align=\"center\">開啟</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>")
        a = 0
    else :
        ui.label.setText("關閉")
        #         ui.label.setText(str(a))
def button_click1():
    # print("hello world")
#     回覆視窗
    messageBox = QMessageBox()  
    messageBox.setWindowTitle("正確")
    messageBox.setInformativeText("Fuck Your Mom.")
    messageBox.exec_()
def button_click2():
    print("hello world")
#     回覆視窗
    messageBox = QMessageBox()  
    messageBox.setWindowTitle("正確")
    messageBox.setInformativeText("Fuck Your Dad.")
    messageBox.exec_()
app =QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.pushButton.clicked.connect(button_click)
ui.pushButton_2.clicked.connect(button_click1)
ui.pushButton_3.clicked.connect(button_click2)

widget.show()
app.exec_()