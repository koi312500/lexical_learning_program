# This program's github site : https://github.com/gunwoo7/lexical_learning_program
# Please read "README.md" first before using the source code.
# "README.md" file contains instructions for using this source code.
# Compile this code file to compile the whole program.

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
        print("초5 어휘력 단계를 마칩니다.")
    elif gui.selected_level == 2:
        print("초6 어휘력 단계를 마칩니다.")
    elif gui.selected_level == 3:
        print("중1 어휘력 단계를 마칩니다.")
    elif gui.selected_level == 4:
        print("중2 어휘력 단계를 마칩니다.")
    else:
        print("중3 어휘력 단계를 마칩니다.")
    print("프로그램을 종료합니다.")
    exit(0)


def Error():
    print("Program detect the error! Exit automatically in 5 seconds")
    time.sleep(5)
    exit()

if __name__ == "__main__":
    print("Starting the lexical_learning_program!")
    print("Do not exit this tab if you want to use the program!")
    pygame.init()
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)
    gui.Control_GUI()
    finished_program()
