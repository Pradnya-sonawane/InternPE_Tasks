#.....................................DIGITAL CLOCK BY USING PYTHON..........................................

from tkinter import *
from tkinter.ttk import *
import time

FG = "#092635"
BG = "#9EC8B9"
window = Tk()
window.title("Digital Clock")
window.config(padx=50, pady= 50, background=BG)

def clock():
    label2.config(text =time.strftime("%H:%M:%S %p"))
    window.after(1000, clock)

#Label 

label1 = Label(text="DIGITAL CLOCK", font= ('Ariel',24,"bold"),background=BG, foreground=FG)
label1.pack()
label2 = Label(text=time.strftime("%H:%M:%S %p"), font=('ds-digital',80) ,background=BG, foreground=FG)
label2.pack()

clock()

window.mainloop()



