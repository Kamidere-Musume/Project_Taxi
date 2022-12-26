from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Scale")
root.geometry("250x250+100+100")

sc = Scale(root, from_=0, to=10, orient=HORIZONTAL)
sc.pack(fill=BOTH)
sc.set(5)

value=IntVar()
value.set(sc.get())
label = Label(root, textvariable=value)
label.pack()

def getvalue(event):
    value.set(sc.get())
    label.config(textvariable=value)

sc.bind("<B1-Motion>",getvalue)
sc.bind("<ButtonRelease-1>",getvalue)
root.mainloop()