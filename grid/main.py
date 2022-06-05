# grid() -> geometry manager that organizes widgets in a table --like structure in a parent
from tkinter import *
from tkinter import Tk

window: Tk = Tk()

Label(window, text="User Info", font=("Arial", 25, "bold")).grid(row=0, column=0, columnspan=2)

Label(window, text="First Name\t: ", font=("Arial", 20), pady=10).grid(row=1, column=0)
Entry(window, width=20, font=("Arial", 20)).grid(row=1, column=1)

Label(window, text="Last Name\t: ", font=("Arial", 20), pady=10).grid(row=2, column=0)
Entry(window, width=20, font=("Arial", 20)).grid(row=2, column=1)

Label(window, text="Email\t\t: ", font=("Arial", 20), pady=10).grid(row=3, column=0)
Entry(window, width=20, font=("Arial", 20)).grid(row=3, column=1)

Button(window, text="Submit", font=("Arial", 20), width=10).grid(row=4, column=1, columnspan=2, sticky='e')
window.mainloop()
