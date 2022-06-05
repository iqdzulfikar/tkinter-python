from tkinter import *
from tkinter import filedialog


def open_file():
    # print out file path
    # filepath = filedialog.askopenfilename()
    # print(filepath)

    # filepath = filedialog.askopenfilename() # by default open document directory

    # initial directory when open button click
    filepath = filedialog.askopenfilename(initialdir="E:\\Program\\Python\\tkinter-python\\filedialog",
                                          title="Open file okay?",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    file = open(filepath, 'r')  # -> 'r/rt' read
    print(file.read())
    file.close()


window = Tk()

button = Button(text="Open", command=open_file)
button.pack()

window.mainloop()
