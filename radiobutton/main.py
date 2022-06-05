# Radiobutton -> similar to checkbox, but you can only select one from a grouping
from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")


window = Tk()

pizza_image = PhotoImage(file='pizza_40px.png')
hamburger_image = PhotoImage(file='hamburger_40px.png')
hotdog_image = PhotoImage(file='hot_dog_40px.png')

food_images = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radiobutton
                              variable=x,  # groups radiobutton together if they share the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx=25,  # adds padding on x-axis
                              font=("Impact", 25),
                              image=food_images[index],  # adds image to radio button
                              compound='left',  # adds image and text (left-side)
                              indicatoron=False,  # eliminate circle indicator
                              width=350,  # sets width of radiobutton
                              command=order  # sets command of radiobutton to function
                              )

    radiobutton.pack(anchor=W)

window.mainloop()
