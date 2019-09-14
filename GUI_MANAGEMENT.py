# Compile main.py to compile the whole program.
# This control GUI part of lexical_learning_program with PyQt5, Qt designer.
# To use source code, install "PyQt5" using "pip install PyQt5".


import sys
import time
import random
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *
import Get_word_dictionary as gwd


app = QApplication(sys.argv)
pass_the_stage = 0
selected_level = 0
selected_word = "  "
now_check_word = "\0"
stage = 1
step = 0
word_list = []

# First_page_Start

form_class_first = uic.loadUiType("GUI_files\First_page.ui")[0]
class First_page(QMainWindow, form_class_first):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setupUi(self)
        self.exit.clicked.connect(self.exitf)
        self.start_button.clicked.connect(self.buttonClick)

    def exitf(self):
        print("Exit the lexical_learning_program.")
        exit(0)

    def buttonClick(self):
        global pass_the_stage
        pass_the_stage = 1
        self.close()

#First_page_End

# Second_page_Start

form_class_second = uic.loadUiType("GUI_files\Second_page.ui")[0]
class Second_page(QMainWindow, form_class_second):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setupUi(self)
        self.exit.clicked.connect(self.exitf)
        self.e_5_button.clicked.connect(self.button_click_e_5)
        self.e_6_button.clicked.connect(self.button_click_e_6)
        self.m_1_button.clicked.connect(self.button_click_m_1)
        self.m_2_button.clicked.connect(self.button_click_m_2)
        self.test_button.clicked.connect(self.button_click_test)

    def exitf(self):
        print("Exit the lexical_learning_program.")
        exit(0)

    def button_click_e_5(self):
        global selected_level
        global pass_the_stage
        selected_level = 1
        pass_the_stage = 1
        self.close()

    def button_click_e_6(self):
        global selected_level
        global pass_the_stage
        selected_level = 2
        pass_the_stage = 1
        self.close()

    def button_click_m_1(self):
        global selected_level
        global pass_the_stage
        selected_level = 3
        pass_the_stage = 1
        self.close()

    def button_click_m_2(self):
        global selected_level
        global pass_the_stage
        selected_level = 4
        pass_the_stage = 1
        self.close()

    def button_click_m_3(self):
        global selected_level
        global pass_the_stage
        selected_level = 5
        pass_the_stage = 1
        self.close()

    def button_click_test(self):
        global selected_level
        global pass_the_stage
        selected_level = 0
        pass_the_stage = 1
        self.close()

# Second_page_End

# Third_page_Start

form_class_third = uic.loadUiType("GUI_files\Third_page.ui")[0]
class Third_page(QMainWindow, form_class_third):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setupUi(self)
        global selected_word
        global now_check_word
        global step
        if step == 1:
            now_check_word = selected_word
            self.text_to_user.setText(now_check_word)
            self.answer_true_false.setText("단어를 입력해 주세요.")
            self.step_show.setText("Step : 1")
            self.enter_text.setText("")
        if step == 2:
            now_check_word = gwd.meaning_of_word
            self.text_to_user.setText(now_check_word)
            self.answer_true_false.setText("단어의 뜻을 입력해 주세요.")
            self.step_show.setText("Step : 2")
            self.enter_text.setText("")
        if step == 3:
            now_check_word = gwd.example_of_word
            self.text_to_user.setText(now_check_word)
            self.answer_true_false.setText("단어의 예문을 입력해 주세요.")
            self.step_show.setText("Step : 3")
            self.enter_text.setText("")

        self.exit.clicked.connect(self.exitf)
        self.check_button.clicked.connect(self.buttonClick)


    def buttonClick(self):
        global now_check_word
        global step
        global recheck_bool
        print(now_check_word)
        if(self.enter_text.toPlainText() != now_check_word ):
            if step == 1:
                recheck_bool = recheck_bool + 1
                self.answer_true_false.setText("입력하신 단어에 오타가 존재합니다.")
                recheck_bool = recheck_bool + 1
            if step == 2:
                self.answer_true_false.setText("입력하신 문장에 오타가 존재합니다.")
                recheck_bool = recheck_bool + 1
            if step == 3:
                self.answer_true_false.setText("입력하신 문장에 오타가 존재합니다.")
                recheck_bool = recheck_bool + 1
        else:
            if step == 1:
                step = 2
                now_check_word = gwd.meaning_of_word
                self.text_to_user.setText(now_check_word)
                self.answer_true_false.setText("단어의 뜻을 입력해 주세요.")
                self.step_show.setText("Step : 2")
                self.enter_text.setText("")
                return
            if step == 2:
                step = 3
                now_check_word = gwd.example_of_word
                self.text_to_user.setText(now_check_word)
                self.answer_true_false.setText("단어의 예문을 입력해 주세요.")
                self.step_show.setText("Step : 3")
                self.enter_text.setText("")
                return
            if step == 3:
                global pass_the_stage
                global selected_word
                global word_list
                pass_the_stage = 1
                if recheck_bool != 0:
                    word_list.append(word_list.pop(0))
                else:
                    word_list.pop(0)
                if len(word_list) != 0:
                    selected_word = word_list[0]
                    gwd.Get_Need_Content(selected_word)
                self.close()

    def exitf(self): # Just_for_Test_level
        global word_list
        print("Saving data...")
        print("Do not exit program! It can gets error!")
        print("Testing exit, saving data")
        fp = open("Data\data_user.dat","w",encoding = "UTF-8")
        for i in word_list:
            if i != word_list[-1]:
                fp.write(i)
                fp.write("\n")
            else:
                fp.write(i)
        print("Exit the lexical_learning_program.")
        fp.close()
        exit(0)

# Third_page_End

def Control_GUI():
    global pass_the_stage
    global step
    global selected_word
    global stage
    global recheck_bool
    Start_First_GUI()
    check_x_button(1)
    pass_the_stage = 0
    Start_Second_GUI()
    check_x_button(2)
    pass_the_stage = 0
    get_word_from_file()
    selected_word = word_list[0]
    gwd.Get_Need_Content(selected_word)
    while len(word_list):
        recheck_bool = 0
        step = 1
        Start_Third_GUI()
        check_x_button(3)
        pass_the_stage = 0


def Start_First_GUI(): # Load First_page
    First_App = First_page()
    First_App.show()
    app.exec_()

def Start_Second_GUI(): # Load Second_page
    Second_App = Second_page()
    Second_App.show()
    app.exec_()

def Start_Third_GUI(): # Load Third_page
    Third_App = Third_page()
    Third_App.show()
    app.exec_()

def check_x_button(stage):
    global pass_the_stage
    while 1:
        if pass_the_stage == 1:
            return
        else:
            if stage == 1:
                Start_First_GUI()
                check_x_button(1)
            elif stage == 2:
                Start_Second_GUI()
                check_x_button(2)
            else:
                Start_Third_GUI()
                check_x_button(3)

def get_word_from_file():
    global word_list
    global selected_level
    if selected_level == 1:
        print("Loading elementary 6 lexical level.")
        print("CAN NOT OPEN")
        print("NOT MADE")
        exit(0)
        #p = open("Data\data_e5.dat","rt",encoding = "UTF-8")
    elif selected_level == 2:
        print("Loading elementary 6 lexical level.")
        print("CAN NOT OPEN")
        print("NOT MADE")
        exit(0)
        #fp = open("Data\data_e6.dat","rt",encoding = "UTF-8")
    elif selected_level == 3:
        print("Loading middle 1 lexical level.")
        fp = open("Data\data_m1.dat","rt",encoding = "UTF-8")
    elif selected_level == 4:
        print("Loading middle 2 lexical level.")
        fp = open("Data\data_m2.dat","rt",encoding = "UTF-8")
    elif selected_level == 5:
        print("Loading middle 3 lexical level.")
        fp = open("Data\data_m3.dat","rt",encoding = "UTF-8")
    else:
        print("Loading TEST lexical level.")
        fp = open("Data\data_TEST.dat","rt",encoding = "UTF-8")

    word_list = fp.readlines()
    for i in range(len(word_list)-1):
        word_list[i] = word_list[i][:len(word_list[i])-1]
    fp.close()
    random.shuffle(word_list)



if __name__ == "__main__":
    Control_GUI() #This line used for test GUI_management.py
                  #Remove it when editing GUI_management.py is finished.
