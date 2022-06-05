from tkinter import *


def create_window():
    # Toplevel() -> new window 'on top' of other windows. Linked to a 'bottom' window
    # new_window = Toplevel()
    # new_window.title("Top Window")

    main_window.destroy()  # close out of main window
    new_window = Tk()  # Tk() -> new independent window


main_window = Tk()
main_window.title("Main/Bottom Window")
main_window.geometry("200x200")

Button(main_window, text="Create a new window", command=create_window).pack()
main_window.eval('tk::PlaceWindow . center')
main_window.mainloop()
