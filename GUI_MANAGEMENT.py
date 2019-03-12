#This control GUI part of Typing_program_new


import tkinter as tk

win = tk.Tk()

#*** first settings ***#
#*** wallpaper - Settings ***#
win.title("Typing-Program_new")
win.geometry("768x432")
wall = tk.PhotoImage(file = "pictures\wallpaper-768x432.gif")
wall_label = tk.Label(image = wall)
wall_label.place(x = -2, y = -2)
#*** END ***#

pixel = tk.PhotoImage(file='pictures\pixel.gif') # Use to change to Button size #
#*** END ***#




win.mainloop()
