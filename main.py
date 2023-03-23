# Last edit date : 2023.03.23
# This project's github site : https://github.com/koi312500/lexical_learning_program/tree/DSHS40_English
# 사용 전에 Github 사이트에 들어가서, README.md 를 읽어주세요!
# Please read "README.md" first before using the source code.
# "README.md" file contains instructions for using this program.
# Compile this code file to run the whole program.
# Compile each code file to run the file.

import time
import GUI_management as gui

def finished_program(): # Print lexical level ending sign
    if gui.selected_level == 1:
        print("End of elementary 5 lexical level.")
    elif gui.selected_level == 2:
        print("End of elementary 6 lexical level.")
    elif gui.selected_level == 3:
        print("End of middle 1 lexical level.")
    elif gui.selected_level == 4:
        print("End of middle 2 lexical level.")
    elif gui.selected_level == 5:
        print("End of middle 3 lexical level.")
    else:
        print("End of TEST lexical level.")
    print("Exit the lexical_learning_program.")
    time.sleep(5) # User need check!


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

'''
def main():
    try: # Error processing
        print("Starting the lexical_learning_program!")
        print("Do not exit this tab if you want to use the program!")
        print("To exit the program, use the Exit button to save the data.")
        print("Exiting this tab will close the program and no program data will be saved.")
        gui.Control_First_Second_GUI() # First Second Page
        gui.Control_Third_GUI() # Third Page
        finished_program() # Print lexical level ending sign
        exit(0)
    except Exception:
        Error()
'''

def main():
    print("Starting the lexical_learning_program!")
    print("Do not exit this tab if you want to use the program!")
    print("To exit the program, use the Exit button to save the data.")
    print("Exiting this tab will close the program and no program data will be saved.")
    gui.Control_First_Second_GUI() # First Second Page
    gui.Control_Third_GUI() # Third Page
    finished_program() # Print lexical level ending sign
    exit(0)
main()
