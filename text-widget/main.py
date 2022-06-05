# Text Widget -> functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    print(text.get("1.0", END))

window = Tk()

text = Text(window, font=("Ink Free", 30),
            height=8, width=20,
            padx=20, pady=20,
            fg='purple', bg='light yellow')
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()