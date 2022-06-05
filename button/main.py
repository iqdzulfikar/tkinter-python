# Buttons -> You click it, then it does stuff
from tkinter import *

count = 0


def submit():
    global count
    count += 1
    print(count)


window = Tk()

window.title("Button Widget")

icon = PhotoImage(file="submit_48.png")

submit_button = Button(window, text="Submit", font=("Comic Sans", 20),
                       fg="#00ff00", bg="black", command=submit,
                       activebackground="#00ff00", activeforeground="black",
                       image=icon, compound="bottom")
submit_button.pack()

window.mainloop()
