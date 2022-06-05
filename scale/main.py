# Scale ->
from tkinter import *


def submit():
    print(f"The temperature is: {scale.get()} degrees celcius")


window = Tk()

fire_image = PhotoImage(file='fire_30px.png')
fire_label = Label(image=fire_image)
fire_label.pack()



scale = Scale(window, from_=100,
              to=-60,
              length=500,
              orient=VERTICAL,  # orientation of scale
              font=('Consolas', 20),
              tickinterval=10,  # adds numeric indicators for value
              # showvalue=0, #hide current value
              resolution=5,  # increment of scale
              troughcolor='#69EAFF', # change the trough color
              fg='#FF1C00',
              bg='#111111')
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

snowflake_image = PhotoImage(file='snowflake_30px.png')
snowflake_label = Label(image=snowflake_image)
snowflake_label.pack()


window.mainloop()
