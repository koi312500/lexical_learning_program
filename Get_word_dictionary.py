# Compile main.py to run the whole program.
# Compile this code file to run this file
# This code uses the API to get the meaning of the word and the dictionary address.
# API provider address : https://opendict.korean.go.kr/service/openApiInfo
# To use the source code, enter the API code in the "Key.key file" without spaces or line breaks.
# To use source code, install "BeautifulSoup" using "pip install BeautifulSoup".
# To use source code, install "request" using "pip install requests".

from bs4 import BeautifulSoup
import requests
import urllib.request as req
import time
import webbrowser
import os.path

def Get_Key_From_File():
    global key
    file = open("Key.key")
    key = file.read()

def Making_URL1(word):
    global URL1
    if word == -1:
        Error()
    URL1 = "https://opendict.korean.go.kr/api/search?certkey_no=575&key=" + key + "&target_type=search&part=word&q=" + word + "&sort=dict&start=1&num=10"

def Making_URL2(word):
    global URL2
    if word == -1:
        Error()
    URL2 = "https://opendict.korean.go.kr/api/search?certkey_no=575&key=" + key + "&target_type=search&part=exam&q=" + word + "&sort=dict&start=1&num=10"


def Get_XML1():
    global Content_XML1
    req = requests.get(URL1)
    html = req.text
    if req.status_code != 200:
        Error()
    Content_XML1 = BeautifulSoup(html,'html.parser')

def Get_XML2():
    global Content_XML2
    req = requests.get(URL2)
    html = req.text
    if req.status_code != 200:
        Error()
    Content_XML2 = BeautifulSoup(html,'html.parser')

def Found_Content1():
    global meaning_of_word
    global link_to_opendict_korean
    meaning_of_word = Content_XML1.definition.get_text()
    target_code_word = Content_XML1.target_code.get_text()
    link_to_opendict_korean = "https://opendict.korean.go.kr/dictionary/view?sense_no=" + target_code_word + "&viewType=confirm"

def Found_Content2():
    global example_of_word
    example_of_word = Content_XML2.example.get_text()


def Get_Need_Content(word):
    Get_Key_From_File()
    Making_URL1(word)
    Get_XML1()
    Found_Content1()
    Making_URL2(word)
    Get_XML2()
    Found_Content2()
