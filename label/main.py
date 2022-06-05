# Labels -> an area widget that holds text and/or image within a window
from tkinter import *

window = Tk()
# window.geometry("700x500")

icon = PhotoImage(file="python.png")

# change icon on window bar
window.iconphoto(True, icon)

# change background color
window.config(bg="black")

my_label = Label(window, text="This a label widget", font=("Comic Sans", 20, "bold"),
                 fg="#00ff00", bg="black", image=icon, compound="bottom")

# my_label.pack()
my_label.place(x=20, y=30)

window.mainloop()
