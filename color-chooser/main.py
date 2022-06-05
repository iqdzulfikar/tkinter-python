from tkinter import *
from tkinter import colorchooser


def change_bg():
    # color = colorchooser.askcolor()
    # print(color[0]) # rgb_code
    # print(color[1]) # hex_
    # window.config(bg=color[1])  # change background color with hex_code

    # one line
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("420x420")

button = Button(text="Change Bg Color", command=change_bg)
button.pack()

window.mainloop()
