from name_generator import text_gen
from number_gen import Number_Generator
from number_check import Number_Check
from text_check import text_check
from check import Check
from sorting import Sort

import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("GENERATOR 2000")
        self.showFullScreen()

        self.textgenbtn = QPushButton("Text generator")
        self.checknumberbtn = QPushButton("Check numbers")
        self.checknamesbtn = QPushButton("Check names")
        self.checkallbtn = QPushButton("Check all")
        self.sortbtn = QPushButton("Sort")
        self.exitbtn = QPushButton("EXIT")  

        numbergenbtn.clicked.connect(self.numbergen)
        textgenbtn.clicked.connect(self.textgen)
        checknumberbtn.clicked.connect(self.numbercheck)
        checknamesbtn.clicked.connect(self.namecheck)
        checkallbtn.clicked.connect(self.allcheck)
        sortbtn.clicked.connect(self.sorting)
        exitbtn.clicked.connect(self.exit_app)

    def numbergen(self):
        Number_Generator()
    def textgen(self):
        text_gen()
    def numbercheck(self):
        Number_Check()
    def namecheck(self):
        text_check()
    def allcheck(self):
        Check()
    def sorting(self):
        Sort()
    def exit_app(self):
        sys.exit(app.exec_())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()