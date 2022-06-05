from tkinter import *
from tkinter.ttk import *
import time


def start():
    size_of_file = 10
    download = 0
    speed = 1
    while download < size_of_file:
        time.sleep(0.05)
        bar['value'] += (speed/size_of_file) * 100
        download += speed
        percent.set(str(int((download / size_of_file) * 100)) + "%")
        text.set(str(download) + "/" + str(size_of_file) + " Mb Completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(orient=HORIZONTAL, length=300)
bar.pack(pady=10)

Label(window, textvariable=percent).pack()
Label(window, textvariable=text).pack()

Button(window, text="Download", command=start).pack()

window.mainloop()
