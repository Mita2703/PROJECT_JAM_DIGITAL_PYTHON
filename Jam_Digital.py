# project python Jam Digital 
# from youtube   : MEDIA SEBELAS https://youtu.be/lF7_MINr9yM?si=y9v0XLQM6RQyWXZ-
# dibuat oleh    : Mita Octavia

from tkinter import *
from tkinter .ttk import *

from time import strftime

root = Tk()
root.title("JAM DIGITAL")

def time() :
    string = strftime ('%H:%M:%S:%p')
    Label.config (text=string)
    Label.after (1000, time)

Label = Label(root, font=("DS-DIGITAL", 70), background= "pink", foreground="black")
Label.pack(anchor='center')


time()

mainloop()