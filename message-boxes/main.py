from tkinter import *
from tkinter import messagebox  # import messagebox library


def click():
    # messagebox.showinfo(title="This is an info message box", message="You are a person")
    # messagebox.showwarning(title="Warning!", message="You have a virus!")
    # messagebox.showerror(title="Error!", message="Something went wrong! :(")

    # if messagebox.askokcancel(title="ask ok cancel!", message="Do you want to do nothing?"):
    #     print("You did a thing!")
    # else:
    #     print("You canceled a thing!")

    # if messagebox.askretrycancel(title="ask retry cancel!", message="Do you want to retry the thing?"):
    #     print("You retried a thing!")
    # else:
    #     print("You canceled a thing!")

    # if messagebox.askyesno(title="ask yes or no!", message="Do you like cake?"):
    #     print("Yes, I a cake")
    # else:
    #     print("Why do you not like cake?")

    # print(messagebox.askquestion(title="ask question", message="Do you like pie?"))
    # answer = messagebox.askquestion(title="ask question", message="Do you like pie?")
    # if answer == 'yes':
    #     print("Yes, I like pie :)")
    # else:
    #     print("Why do you not like cake?")

    # yes -> True, no -> False, cancel -> none
    answer = messagebox.askyesnocancel(title="ask yes no or cancel", message="Do you lice to code?", icon='error')
    if answer == True:
        print("You like to code? :(")
    elif answer == False:
        print("Then, why are you watching a video on coding?")
    else:
        print("You have dodged the question")


window = Tk()
window.title("Messagebox Widget")

button = Button(window, text="Click me!", command=click)
button.pack()

window.mainloop()
