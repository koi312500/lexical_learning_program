#This program's github site : https://github.com/gunwoo7/lexical_learning_program
#Please read "README.md" first before using the source code.
# "README.md" file contains instructions for using this source code.

#SETTINGS -->
meaning_of_word = '\0'
link_to_opendict_korean = '\0'
#SETTINGS -->
import time
import Get_word_dictionary as gc
import GUI_management as gui


def Error():
    print("Program detect the error! Exit automatically in 5 seconds")
    time.sleep(5)
    exit()

def Get_Word_Content():
    global meaning_of_word
    global example_of_word
    global link_to_opendict_korean
    gc.Get_Need_Content()
    meaning_of_word = gc.meaning_of_word
    link_to_opendict_korean = gc.link_to_opendict_korean
    example_of_word = gc.example_of_word

if __name__ == "__main__":
    gui.Control_GUI()
