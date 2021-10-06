import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem
from PyQt5 import uic

from layouts.mainwindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()