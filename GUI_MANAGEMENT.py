#This control GUI part of lexical_learning_program with PyQt5, Qt designer.
#To use source code, install "PyQt5" using "pip install PyQt5".


import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

# First_page
app = QApplication(sys.argv)
form_class_first = uic.loadUiType("GUI_files\First_page.ui")[0]
class First_page(QMainWindow, form_class_first):
    def __init__(self):
        super().__init__()
        self.dialogs = list()
        self.setUI()

    def setUI(self):
        self.setupUi(self)
        self.start_button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()

form_class_second = uic.loadUiType("GUI_files\Second_page.ui")[0]
class Second_page(QMainWindow, form_class_second):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setupUi(self)

# Third_page
form_class_third = uic.loadUiType("GUI_files\Third_page.ui")[0]
selected_word = "Just_For_Declare"
class Third_page(QMainWindow, form_class_third):
    def __init__(self):
        super().__init__()
        self.setUI()
        self.answer_true_false.setText("입력하신 단어에 오타가 존재합니다.")

    def setUI(self):
        self.setupUi(self)
        self.check_button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        if(self.enter_text.toPlainText() != selected_word):
            self.answer_true_false.setText("입력하신 단어에 오타가 존재합니다.")
        else:
            self.answer_true_false.setText("Your answer is true!-check!")




def Control_GUI():
    print("Starting the lexical_learning_program!")
    print("Do not exit this tab if you want to use the program!")
    Start_First_GUI()
    Start_Second_GUI()
    Start_Third_GUI()

def Start_First_GUI():
    First_App = First_page()
    First_App.show()
    app.exec_()

def Start_Second_GUI():
    Second_App = Second_page()
    Second_App.show()
    app.exec_()

def Start_Third_GUI():
    Third_App = Third_page()
    Third_App.show()
    app.exec_()

if __name__ == "__main__":
    Control_GUI() #This line used for test GUI_management.py
                  #Remove it when editing GUI_management.py is finished.
