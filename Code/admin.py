import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox
from Customerlist import CustomerList

#class driverdash(tk.Tk):
class AdminDash(tk.Tk):
   #def __init__(self):
    def __init__(self):
        super().__init__()
        self.geometry("1045x800")
      #self.resolution = "1000x800"
        self.resizable(False,False)
        self.title("Admin")

    # Adding Background Image 
  
        imagepath = absPath(__file__,"../pictures/wall1.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=500, height=300)
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
        list = ["User ID","Booking ID","User First Name","User Last Name","User Phone Number","Current Location","Destination","Price","Distance","Booking Status"]
        data = "select booking.Booking_Id,user.User_Id,user.User_fname, user.User_lname, user.User_phone_Number,booking.Current_location,booking.Destination,booking.Price,booking.Distance,booking.Booking_Status From booking inner join user on User.User_Id = booking.User_Id"

        self.usersearch_btn = tk.Button(canvas,text="User list",command= lambda:self.temp(list,data))
        self.usersearch_btn.place(x=500,y=200,height=25,width=60)


    def temp(self,column,query):
        win = tk.Toplevel(self)
        win.geometry("1045x800")
        win.title("Customer")
        
        
    # Button
        self.assin_btn = tk.Button(win,text="Assign")
        self.assin_btn.place(x=200,y=300)
        
        self.frm = tk.Frame(win, width=500,height=200,background="bisque")
        self.book_tbl = ttk.Treeview(self.frm,columns = column, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.book_tbl.pack()
        
        
        for i in column:
            self.book_tbl.column(i,stretch=NO,width=100)
            self.book_tbl.heading(i,text=i)
        
    # Database    
        con,cur = dbcon()
        cur.execute(query)
        rows = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
      
        for i in rows:
            self.book_tbl.insert('','end',values=i)

    
if __name__ == "__main__":
    app = AdminDash()
    app.mainloop()