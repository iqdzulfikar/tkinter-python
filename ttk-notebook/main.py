# ttk.Notebook() -> widget that manages a collection of windows/displays
from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

# new frame for tab 1 and 2
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True,  # expand to fill any space not otherwise
              fill="both"  # fill space on x and y axis
              )

Label(tab1, text="Hello, this is tab#1", width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab#2", width=50, height=25).pack()

window.mainloop()
