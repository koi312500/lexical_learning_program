#This control GUI part of Typing_program_new


import tkinter as tk

win = tk.Tk()

#*** Settings ***#
win.title("Typing-Program_new")
win.geometry("660x450")
wall = tk.PhotoImage(file = "pictures_gui.gif")
wall_label = tk.Label(image = wall)
wall_label.place(x = 0, y = 0)
#*** Settings ***#

#*** Test code ***#
def click_me():
    action.configure(text="** I have been clicked")

action = tk.Button(win,text = "Click me!",command=click_me)
action.grid(column=1, row=0)
#*** Test code ***#

win.mainloop()
