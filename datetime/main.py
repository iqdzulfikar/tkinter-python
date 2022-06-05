from tkinter import *
from time import *


def update():
    time_str = strftime("%H:%M:%S")  # 24 hours
    # time_str = strftime("%I:%M:%S %p")
    time_label.config(text=time_str)

    day_str = strftime("%A, %B %d %Y")
    day_label.config(text=day_str)

    # date_str = strftime("%B %d %Y")
    # date_label.config(text=date_str)

    window.after(1000, update)


window = Tk()

time_label = Label(window, font=("Arial", 30), fg="#00ff00", bg='black')
time_label.pack()

day_label = Label(window, font=("Ink Free", 30, "bold"))
day_label.pack()

date_label = Label(window, font=("Ink Free", 30, "bold"))
date_label.pack()

update()

window.mainloop()
