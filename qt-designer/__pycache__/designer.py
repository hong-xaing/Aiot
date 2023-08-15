from mainwindow import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

global form
form=1

def addNumber():
    try:
        print("Add Two Numbers")
        try:
            num1=int(ui.lineEdit.text())
            num2=int(ui.lineEdit_2.text())
        except:
            num1=float(ui.lineEdit.text())
            num2=float(ui.lineEdit_2.text())
        global form
        if form==1:
            ui.total.setText(str(num1+num2))
        else:
            ui.total.setText(str(num1-num2))
    except:
        messagebox=QMessageBox()
        messagebox.setWindowTitle("通知")
        messagebox.setInformativeText("輸入內容有誤！")
        messagebox.exec_()
def change():
    print("Change")
    global form
    if form==1:
        form=2
        ui.label.setText("-")
    else:
        form=1
        ui.label.setText("+")
    messagebox=QMessageBox()
    messagebox.setWindowTitle("通知")
    messagebox.setInformativeText("加減轉換成功")
    messagebox.exec_()

app=QApplication(sys.argv)
widget=QWidget()
ui=Ui_Dialog()
ui.setupUi(widget)

ui.pushButton.clicked.connect(addNumber)
ui.pushButton_2.clicked.connect(change)

widget.show()
app.exec_()