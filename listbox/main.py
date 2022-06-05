# Listbox -> A listing of selectable text items within its own container
from tkinter import *


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered:")
    for index in food:
        print(index)
    # print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    # listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()
window.title("Listbox Widget")

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia', 30),
                  width=15,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "salad")

listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()

window.mainloop()
