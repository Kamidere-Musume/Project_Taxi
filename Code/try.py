import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox

#class driverdash(tk.Tk):
class CustomerList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1045x800")
        self.resizable(False,False)
        self.title = "Admin"

    # Adding Background Image 
    
        imagepath = absPath(__file__,"../pictures/wall3.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=1000, height=800)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")
        
        
        self.frm = tk.Frame(canvas, width=1045,height=500,background="bisque")
        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.book_tbl = ttk.Treeview(self.frm, columns=(1,2,3,4,5,6,7,8), show="headings",height="10")
        self.book_tbl.pack()
        
        for i,j in enumerate(["a","b","c","d"]):
            self.book_tbl.column(i+1,stretch=NO,width=80)
            self.book_tbl.heading(i+1,text=j)
    

if __name__=="__main__":
    app = CustomerList()
    app.mainloop()