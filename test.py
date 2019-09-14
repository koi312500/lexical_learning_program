# This is a source code to check if a word is in the dictionary.

import Get_word_dictionary as gwd

def get_word_from_file():
    global word_list
    fp = open("Data\data_e6.dat","rt",encoding = "UTF-8")
    word_list = fp.readlines()
    for i in range(len(word_list)-1):
        word_list[i] = word_list[i][:len(word_list[i])-1]
    fp.close()
def main():
    get_word_from_file()
    a = 0
    selected_word = word_list[a]
    for i in range(a,len(word_list)):
        gwd.Get_Need_Content(selected_word)
        print(i)
        print(selected_word)
        print(gwd.meaning_of_word)
        print(gwd.example_of_word)
        print(" ")
        selected_word = word_list[i+1]

main()
