# Checkbutton -> by default the onvalue=1 and the offvalue=0
from tkinter import *


def display():
    # if x.get() == 1:  # using int
        # if x.get(): # using boolean
    if (x.get()=="YES"): # using string
        print("You agree")
    else:
        print("You don't agree! :(")


window = Tk()
window.title("Checkbutton Widget")

# x = StringVar()

icon = PhotoImage(file='python_48px.png')

# using int
# x = IntVar()
# check_button = Checkbutton(window, text="I agree to something", font=("Arial", 25),
#                            variable=x, onvalue=1, offvalue=0, command=display,
#                            fg='#00ff00', bg='black', activeforeground='#00ff00', activebackground='black',
#                            padx=25, pady=10, image=icon, compound='left')

# using boolean
# x = BooleanVar()
# check_button = Checkbutton(window, text="I agree to something", font=("Arial", 25),
#                            variable=x, onvalue=True, offvalue=False, command=display,
#                            fg='#00ff00', bg='black', activeforeground='#00ff00', activebackground='black',
#                            padx=25, pady=10, image=icon, compound='left')

# using string
x = StringVar()
check_button = Checkbutton(window, text="I agree to something", font=("Arial", 25),
                           variable=x, onvalue="YES", offvalue="NO", command=display,
                           fg='#00ff00', bg='black', activeforeground='#00ff00', activebackground='black',
                           padx=25, pady=10, image=icon, compound='left')
check_button.pack()

window.mainloop()
