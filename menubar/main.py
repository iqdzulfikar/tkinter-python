from tkinter import *


def open_file():
    print("File has been opened")


def save_file():
    print("File has been saved")


def cut():
    print("You cut some text")


def copy():
    print("You copied some text")


def paste():
    print("You pasted some text")


window = Tk()

open_image = PhotoImage(file="open.png")
save_image = PhotoImage(file="save.png")
exit_image = PhotoImage(file="exit.png")

cut_image = PhotoImage(file="cut.png")
copy_image = PhotoImage(file="copy.png")
paste_image = PhotoImage(file="paste.png")

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0, font=("Arial", 15))
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=open_image, compound='left')
file_menu.add_command(label="Save", command=save_file, image=save_image, compound='left')
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_image, compound='left')

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut, image=cut_image, compound='left')
edit_menu.add_command(label="Copy", command=copy, image=copy_image, compound='left')
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste, image=paste_image, compound='left')

window.mainloop()
