#                    clock with python
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title('CodeX Clock')

def time():
    format=strftime('%I:%M:%S %p')
    label.config(text=format)
    label.after(1000,time)

label=Label(root,font=('Algerian',80),background = 'black',foreground = 'cyan')
label.pack(anchor='center')
time()

mainloop() 