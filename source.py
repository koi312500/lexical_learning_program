#Please install bs4 by using "pip install bs4"
#Please install requests by using "pip install requests"
#please enter the your_key number to MAKING_URL function
#수정사항 -> 주소 확인, 오류상황 판단확인 GUI 제작
from bs4 import BeautifulSoup
import requests
import urllib.request as req
import time
import os.path

def Error():
    print("프로그램에서 오류가 발생된 것이 감지되었습니다. 5초 후 자동 종료합니다.")
    time.sleep(5)
    exit()
    
def Making_URL():
    global URL
    if word == -1:
        Error()
    URL = "https://opendict.korean.go.kr/api/search?certkey_no=575&key=your_key&target_type=search&part=word&q="
    URL = URL + word
    URL = URL + "&sort=dict&start=1&num=10"

def Get_XML():
    global Content_XML
    req = requests.get(URL)
    html = req.text
    if req.status_code != 200:
        Error()
    Content_XML = BeautifulSoup(html,'html.parser')

def Found_Content():
    global meaning_of_word
    global link_to_opendict_korean
    meaning_of_word = Content_XML.definition.get_text()
    link_to_opendict_korean = Content_XML.link.next_sibling

def GET_NEED_CONTENT():
    global word
    word = str(input())
    Making_URL()
    Get_XML()
    Found_Content()

GET_NEED_CONTENT()
