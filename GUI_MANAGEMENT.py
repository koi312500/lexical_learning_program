#This control GUI part of lexical_learning_program


import tkinter as tk
from tkinter import ttk

win = tk.Tk()

#*** first settings ***#
#*** wallpaper - Settings ***#
win.title("lexical_learning_program")
win.geometry("768x432")
wall = tk.PhotoImage(file = "pictures\wallpaper-768x432.gif")
wall_label = tk.Label(image = wall)
wall_label.place(x = -2, y = -2)
#*** END ***#

pixel = tk.PhotoImage(file='pictures\pixel.gif') # Use to change to Button size #
#*** END ***#


ttk.Label(win, text='').grid(column=0, row=0)
action = tk.Button(win,text = "lexical_learning_program start",image=pixel,compound='center') # command=click_me,
action.grid(column=150,row=150)
action.config(width=400,height=20)


win.mainloop()
