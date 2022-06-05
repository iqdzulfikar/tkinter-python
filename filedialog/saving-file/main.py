from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(initialdir="E:\\Program\\Python\\tkinter-python\\filedialog\\saving-file",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])

    if file is None:
        return
    # filetext = str(text.get(1.0, END))
    filetext = input("Enter some text I guess: ")
    file.write(filetext)
    file.close()


window = Tk()

text = Text()
text.pack()

button = Button(text="Save", command=save_file)
button.pack()

window.mainloop()
