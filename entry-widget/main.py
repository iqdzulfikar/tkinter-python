# Entry widget -> textbox accepts a single line of user input
from tkinter import *


def submit():
    password = entry.get()
    print("Hello " + password)
    # entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()
window.title("Entry Widget")

entry = Entry(window, font=("Arial", 30), fg="#00ff00", bg="black", show="*")
entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", font=("Arial", 25), command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", font=("Arial", 25), command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", font=("Arial", 25), command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
