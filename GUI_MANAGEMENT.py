#This control GUI part of Typing_program_new


import tkinter as tk

win = tk.Tk()

#*** wallpaper - Settings ***#
win.title("Typing-Program_new")
win.geometry("768x432")
wall = tk.PhotoImage(file = "wallpaper-768x432.gif")
wall_label = tk.Label(image = wall)
wall_label.place(x = -2, y = -2)
#*** Settings ***#

#*** Test code ***#
def click_me():
    action.configure(text="** I have been clicked")

pixel = tk.PhotoImage(file='pixel.gif')
action = tk.Button(win,text = "Click me!",command=click_me,image=pixel,compound='center')
action.grid(column=1, row=0)
action.config(width=100,height=100)
#*** Test code ***#

win.mainloop()
