# Last edit date : 2019.09.15 - compile check!
# Compile main.py to run the whole program.
# Compile this code file to run this file
# This control GUI part of lexical_learning_program with PyQt5, Qt designer.
# To use source code, install "PyQt5" using "pip install PyQt5".

# Import part Start

import sys
import time
import random
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

# Import part End

# Varible declare Start

app = QApplication(sys.argv)
pass_the_stage = 0
selected_level = 0
selected_word = []
now_check_word = "\0"
stage = 1
step = 0
word_list = []
sentence_list = []

def Error(): # error processing
    for i in range(100):
        print("lexical_learning_program detect the error! Exit automatically in 6 seconds")
        time.sleep(0.01)
    for i in range(4):
        print("lexical_learning_program detect the error! Exit automatically in 5 seconds")
        time.sleep(0.25)
    for i in range(100):
        print("lexical_learning_program detect the error! Exit automatically in 4 seconds")
        time.sleep(0.01)
    for i in range(4):
        print("lexical_learning_program detect the error! Exit automatically in 3 seconds")
        time.sleep(0.25)
    for i in range(100):
        print("lexical_learning_program detect the error! Exit automatically in 2 seconds")
        time.sleep(0.01)
    for i in range(100):
        print("Exit the lexical_learning_program.")
        time.sleep(0.01)
    exit(-1)

# Varible declare Start

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
        print("Exit lexical_learning_program")
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
        print("Exit lexical_learning_program.")
        exit(0)

    # Setting level function Start
    def button_click_e_5(self):
        print("This is not allowed by KOI3125.")
        time.sleep(5)
        Error()
        self.close()

    def button_click_e_6(self):
        print("This is not allowed by KOI3125.")
        time.sleep(5)
        Error()
        self.close()

    def button_click_m_1(self):
        print("This is not allowed by KOI3125.")
        time.sleep(5)
        Error()
        self.close()

    def button_click_m_2(self):
        print("This is not allowed by KOI3125.")
        time.sleep(5)
        Error()
        self.close()

    def button_click_m_3(self):
        print("This is not allowed by KOI3125.")
        time.sleep(5)
        Error()
        self.close()

    def button_click_test(self):
        global selected_level
        global pass_the_stage
        selected_level = 0
        pass_the_stage = 1
        self.close()

    # Setting level function Start

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
        if step == 1: # Word step
            now_check_word = selected_word
            self.text_to_user.setText(selected_word[1])
            self.answer_true_false.setText("단어를 입력해 주세요.")
            self.step_show.setText("Step : NULL")
            self.enter_text.setText("")

        self.exit.clicked.connect(self.exitf) # Exit button connect
        self.check_button.clicked.connect(self.buttonClick) # Check button connect


    def buttonClick(self): # Check Button clicked
        global now_check_word
        global step
        global recheck_bool
        print(now_check_word)

        # Next step or next word
        if(self.enter_text.toPlainText() != now_check_word[0]):
            # Typing Error - Show comment
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
            # Typing Correct - Next step & word
            if step == 1: # First step -> Second step
                global pass_the_stage
                global selected_word
                global word_list
                pass_the_stage = 1
                if recheck_bool != 0: # Typing error
                    word_list.append(word_list.pop(0)) # Move content to end of list
                else: # No typing error
                    random.shuffle(word_list)
                if len(word_list) != 0: # Next word
                    selected_word = word_list[0] # Selected_word = next word
                self.close()

    def exitf(self): # Just_for_Test_level
        global word_list
        print("Saving data...")
        print("Do not exit program! It can gets error!")
        print("Exit lexical_learning_program.")
        exit(0)

# Third_page_End

def Control_First_Second_GUI(): # Control Frist, Second page GUI
    global pass_the_stage
    Start_First_GUI()
    check_x_button(1)
    pass_the_stage = 0
    Start_Second_GUI()
    check_x_button(2)
    pass_the_stage = 0

def Control_Third_GUI(): # Control Third page GUI
    global pass_the_stage
    global step
    global selected_word
    global recheck_bool
    get_word_from_file()
    check_level_finished()
    selected_word = word_list[0]
    while len(word_list): # Run when word_list have element
        recheck_bool = 0
        step = 1
        Start_Third_GUI()
        check_x_button(3)
        pass_the_stage = 0
    saving_data() # word_list don't have element

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

def check_x_button(stage): # Click "X" button isn't allowed.
    global pass_the_stage  # Reload GUI
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

def get_word_from_file(): # Data folder files loading
    global word_list
    global selected_level
    
    print("Loading TEST lexical level.")
    fp = open("Data\data_TEST.dat","r",encoding = "UTF-8")

    tmp_list = fp.readlines()
    for i in range(len(tmp_list)): # Remove word_list's conten`t's line feed.
        word_list1 = tmp_list[i].split(sep = ' ', maxsplit = 2)
        print(word_list1)
        word_list.append([word_list1[1], word_list1[2][:len(word_list1[2]) - 1]])
    fp.close()
    random.shuffle(word_list) # Mix the list
    print(word_list[0])

def saving_data():          # Save data with blank
    print("Data didn't changed.")

def check_level_finished():
    global word_list
    if len(word_list) == 0:
        if selected_level == 1:
            print("Elementary 5 lexical level is already done.")
            print("Try different lexical level.")
            print("If you want to start this level again, copy Data_backup\data_e5.dat to Data\data_e5.dat")
        elif selected_level == 2:
            print("Elementary 6 lexical level is already done.")
            print("Try different lexical level.")
            print("If you want to start this level again, copy Data_backup\data_e6.dat to Data\data_e6.dat")
        elif selected_level == 3:
            print("Middle 1 lexical level is already done.")
            print("Try different lexical level.")
            print("If you want to start this level again, copy Data_backup\data_m1.dat to Data\data_m1.dat")
        elif selected_level == 4:
            print("Middle 2 lexical level is already done.")
            print("Try different lexical level.")
            print("If you want to start this level again, copy Data_backup\data_m2.dat to Data\data_m2.dat")
        elif selected_level == 5:
            print("Middle 3 lexical level is already done.")
            print("Try different lexical level.")
            print("If you want to start this level again, copy Data_backup\data_m3.dat to Data\data_m3.dat")
        else:
            print("TEST lexical level is already done.")
            print("Try different lexical level.")
            print("If you want to start this level again, copy Data_backup\data_TEST.dat to Data\data_TEST.dat")
        print("After 10 seconds, lexical_learning_program exits.")
        time.sleep(10) # User need check!
        exit(0)
