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
        
    # Title 
        title_lbl = canvas.create_text(450,50,text="Admin",fill="white",font=("Helvatica",15))

    # Search Box
        # Temporary Text
        def temp_text(e):
            self.search_txt.delete(0,"end")
            
        # Search Entry Box
        self.search_txt = tk.Entry(canvas)
        self.search_txt.place(x=350, y=510,height=25,width=150)
        self.search_txt.insert(0,"Search")
        self.search_txt.bind("<FocusIn>",temp_text)
        self.search_txt.place(x=350,y=200, height=25, width=140)
             
    # Search Customer Button
        self.usersearch_btn = tk.Button(canvas,text="Search",command=self.showtable)
        self.usersearch_btn.place(x=500,y=200,height=25,width=60)

    # Table for customer
 
      # Adding Frame and tree view
        self.frm = tk.Frame(canvas, width=1045,height=500,background="bisque")
        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.book_tbl = ttk.Treeview(self.frm, columns=(1,2,3,4,5,6,7,8), show="headings",height="10")
        self.book_tbl.pack()

        # Adding scrollbar in tree view 
        self.scroll = ttk.Scrollbar(self.frm,orient="vertical",command= self.book_tbl.yview)
        self.scroll.place(x=1025, y = 25, height=200)
        
        self.book_tbl.configure(yscrollcommand=self.scroll.set)
        # Adding tree view data in table
        self.book_tbl.column(1,stretch = NO,width=80)
        self.book_tbl.heading(1, text="User ID")

        self.book_tbl.column(2,stretch = NO,width=80)      
        self.book_tbl.heading(2,text="User First Name")
        
        self.book_tbl.column(3,stretch = NO,width=110)      
        self.book_tbl.heading(3,text="User Last Name")
        
        self.book_tbl.column(4,stretch = NO,width=110)      
        self.book_tbl.heading(4,text="User Email")
        
        self.book_tbl.column(5,stretch = NO,width=110)      
        self.book_tbl.heading(5,text="User Password")
        
        self.book_tbl.column(6,stretch = NO,width=110)      
        self.book_tbl.heading(6,text="User Address")
        
        self.book_tbl.column(7,stretch = NO,width=110)
        self.book_tbl.heading(7,text="User Phone Number")
        
        self.book_tbl.column(8,stretch = NO,width=110)      
        self.book_tbl.heading(8,text="Payment Method")
        

    def showtable(self):
        con,cur = dbcon()
        query = "select * from user"
        cur.execute(query)
        rows = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
        
        for i in rows:
         self.book_tbl.insert('','end',values=i)
        
if __name__ == "__main__":
    app = CustomerDash()
    app.mainloop()