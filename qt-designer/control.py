import mainwindow
from auto_mechine import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
# from modbus_servo_fake import *

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
        ui.label.setText("<html><head/><body><p align=\"center\">servo on</p></body></html>")
        a = 0
    else :
        ui.label.setText("<html><head/><body><p align=\"center\">servo off</p></body></html>")
        #         ui.label.setText(str(a))
def button_click1():
    # print("hello world")
#     回覆視窗
    messageBox = QMessageBox()  
    messageBox.setWindowTitle("正確")
    messageBox.setInformativeText("原點歸零.")
    messageBox.exec_()
def button_click2():
#     回覆視窗
    messageBox = QMessageBox()  
    messageBox.setWindowTitle("正確")
    messageBox.setInformativeText("")
    messageBox.exec_()
def target():
    message = ui.lineEdit.text()
    print(message)

start = False
def button2_click():
    global start
    if start:
        start= False
        timmer.stop()
        print("timmer stop")
    else:
        start = True
        timmer.start(1000)

def count():
    print("hi")

app =QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
timmer = Qtime()
timmer.timeont.connect(count)
ui.pushButton.clicked.connect(button_click)
ui.pushButton_2.clicked.connect(button_click1)
ui.pushButton_3.clicked.connect(target)

widget.show()
app.exec_()