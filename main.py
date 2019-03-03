#This program's github site : https://github.com/gunwoo7/Typing_Program_new
#Please install bs4 by using "pip install bs4"
#Please install requests by using "pip install requests"
#수정사항 -> 주소 확인, 오류상황 판단확인 GUI 제작
#Please input your key to key veriable to GET_CODE.py

#SETTINGS -->
meaning_of_word = '\0'
link_to_opendict_korean = '\0'
#SETTINGS -->
import time
import GET_CODE as gc

def Error():
    print("Program detect the error! Exit automatically in 5 seconds")
    time.sleep(5)
    exit()

def Get_Word_Content():
    global meaning_of_word
    global link_to_opendict_korean
    gc.Get_Need_Content()
    meaning_of_word = gc.meaning_of_word
    link_to_opendict_korean = gc.link_to_opendict_korean

Get_Word_Content()
print(meaning_of_word)
