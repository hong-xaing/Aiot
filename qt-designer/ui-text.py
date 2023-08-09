# ui轉換成py檔案

# pyuic5 -x qt-1.ui -o mainwindow.py

from mainwindow import Ui_Dialog
from PyQt5.Qtwidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

app =QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
widget.show()
app.exec_()