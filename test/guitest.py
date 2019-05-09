# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *
from tkinter import messagebox
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
 
def clicked():
    res = messagebox.askquestion('Message title','Message content') 
    lbl.configure(text= res)
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()