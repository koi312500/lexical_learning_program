#This code uses the API to obtain the meaning of the word and the address of the dictionary.
#API provider address : https://opendict.korean.go.kr/service/openApiInfo
#Please input your key to key veriable

from bs4 import BeautifulSoup
import requests
import urllib.request as req
import time
import webbrowser
import os.path

key = "YOUR_KEY"
    
def Making_URL():
    global URL
    if word == -1:
        Error()
    URL = "https://opendict.korean.go.kr/api/search?certkey_no=575&key=" + key + "&target_type=search&part=word&q="
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
    target_code_word = Content_XML.target_code.get_text()
    link_to_opendict_korean = "https://opendict.korean.go.kr/dictionary/view?sense_no=" + target_code_word + "&viewType=confirm"
    

def Get_Need_Content():
    global word
    word = str(input("Please enter the word You want to search : "))
    Making_URL()
    Get_XML()
    Found_Content()

