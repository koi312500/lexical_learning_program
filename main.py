# This project's github site : https://github.com/gunwoo7/lexical_learning_program
# Please read "README.md" first before using the source code.
# "README.md" file contains instructions for using this program.
# Compile this code file to run the whole program.
# Compile each code file to run the file.
# To use source code, install "pygame" using "pip install pygame".

#SETTINGS -->
meaning_of_word = '\0'
link_to_opendict_korean = '\0'
#SETTINGS -->
import time
import pygame
import GUI_management as gui
from pygame.locals import *

def finished_program():
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


def Error():
    pygame.mixer.music.stop()
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

if __name__ == "__main__":
    try:
        print("Starting the lexical_learning_program!")
        print("Do not exit this tab if you want to use the program!")
        print("To exit the program, use the Exit button to save the data.")
        print("Exiting this tab will close the program and no program data will be saved.")
        pygame.init()
        pygame.mixer.music.load('Data\\bgm1.mp3')
        pygame.mixer.music.play(-1)
        gui.Control_First_Second_GUI()
        pygame.mixer.music.load('Data\\bgm2.mp3')
        pygame.mixer.music.play(-1)
        gui.Control_Third_GUI()
        finished_program()
        time.sleep(5)
        exit(0)
    except:
        Error()
