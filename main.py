# This program's github site : https://github.com/gunwoo7/lexical_learning_program
# Please read "README.md" first before using the source code.
# "README.md" file contains instructions for using this program.
# Compile this code file to compile the whole program.
# To use source code, install "pygame" using "pip install pygame".

#SETTINGS -->
meaning_of_word = '\0'
link_to_opendict_korean = '\0'
#SETTINGS -->
import time
import pygame
import Get_word_dictionary as gc
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
    exit(0)


def Error():
    print("Program detect the error! Exit automatically in 5 seconds")
    exit()

if __name__ == "__main__":
    print("Starting the lexical_learning_program!")
    print("Do not exit this tab if you want to use the program!")
    pygame.init()
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)
    gui.Control_GUI()
    finished_program()
