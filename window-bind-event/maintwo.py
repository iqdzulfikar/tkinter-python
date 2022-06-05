from tkinter import *


def dosomething(event):
    print(str(event))
    print(f"Mouse Coordinate: {event.x}x{event.y}")


window = Tk()

window.bind("<Button-1>", dosomething)  # left mouse click
window.bind("<Button-2>", dosomething)  # mouse wheel
window.bind("<Button-3>", dosomething)  # right mouse click
window.bind("<ButtonRelease>", dosomething)  # right mouse click
window.bind("<Enter>", dosomething)  # Enter click
window.bind("<Leave>", dosomething)  # Leave
window.bind("<Motion>", dosomething)  # Motion

window.mainloop()
