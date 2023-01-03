import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox
from Customerlist import CustomerList

#class driverdash(tk.Tk):
class AdminDash(tk.Tk):
   #def __init__(self):
    revenue = 0
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
        # customerlistorary Text
        def temp_text(e):
            self.search_txt.delete(0,"end")
            
        # Search Entry Box
        self.search_txt = tk.Entry(canvas)
        self.search_txt.place(x=350, y=510,height=25,width=150)
        self.search_txt.insert(0,"Search")
        self.search_txt.bind("<FocusIn>",temp_text)
        self.search_txt.place(x=350,y=200, height=25, width=140)
             
    # Customer Search Button
        self.usersearch_btn = tk.Button(canvas,text="User list",command= self.customerlist)
        self.usersearch_btn.place(x=500,y=200,height=25,width=60)
    
     # Complete Button
        self.complete_btn = tk.Button(canvas,text="Complete",command=self.complete)
        self.complete_btn.place(x=200,y=200)
        
# Top level for customer list 
    def customerlist(self):
        win = tk.Toplevel(self)
        win.geometry("1045x800")
        win.title("Customer")
        
    # Customer List Data 
        list2 = ["Booking ID","User ID","User First Name","User Last Name","User Phone Number","Current Location","Destination","Price","Distance","Booking Status"]
        data2 = "select booking.Booking_Id,user.User_Id,user.User_fname, user.User_lname, user.User_phone_Number,booking.Current_location,booking.Destination,booking.Price,booking.Distance,booking.Booking_Status From booking inner join user on User.User_Id = booking.User_Id where Booking_Status = 'Pending'"

   
        
    # Assign Button
        self.assin_btn = tk.Button(win,text="Assign",command = self.driverlist)
        self.assin_btn.place(x=200,y=300)
        
    # Frame and Treeview    
        self.frm = tk.Frame(win, width=500,height=200,background="bisque")
        self.book_tbl = ttk.Treeview(self.frm,columns = list2, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.book_tbl.pack()
        
        
        for i in list2:
            self.book_tbl.column(i,stretch=NO,width=100)
            self.book_tbl.heading(i,text=i)
        
    # Database    
        con,cur = dbcon()
        cur.execute(data2)
        rows = cur.fetchall()
        con.close()
      
        for i in rows:
            self.book_tbl.insert('','end',values=i)

        
# Top Level For Driver List 
    def driverlist(self):
        
    # Data selection for customer    
        a = self.book_tbl.selection()[0]
        booking_id = self.book_tbl.item(a,"values")
        
        print(booking_id)
        win = tk.Toplevel(self)
        win.geometry("1045x800")
        win.title("Driver")
        
    # Driver List Data
        list1 = ["Driver ID","Driver First Name","Driver Last Name","Driver Phone Number","Vehicle ID"]
        data1 = "select Driver_Id,Driver_Fname,Driver_Lname,Driver_Phone_Number,Vehicle_Id from driver where Assign_status = 0"
    # Button
        self.assin_btn = tk.Button(win,text="Assign",command=lambda: self.accept(booking_id,win,a))
        self.assin_btn.place(x=200,y=300)

    # Frame and Treeview    
        self.frm = tk.Frame(win, width=500,height=200,background="bisque")
        self.driverbook_tbl = ttk.Treeview(self.frm,columns = list1, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.driverbook_tbl.pack()
        
        
        for i in list1:
            self.driverbook_tbl.column(i,stretch=NO,width=100)
            self.driverbook_tbl.heading(i,text=i)
        
    # Database    
        con,cur = dbcon()
        cur.execute(data1)
        rows = cur.fetchall()
        cur.close()
        con.close()
      
        for i in rows:
            self.driverbook_tbl.insert('','end',values=i)

# Action: Accepting booking
    def accept(self,booking_id,win):
        a = self.driverbook_tbl.selection()[0]
        driver_id = self.driverbook_tbl.item(a,"values")[0]
        
        query = "update booking set Booking_Status = 'Accepted',Driver_Id = %s where Booking_Id = %s"
        query1 = "update driver set Assign_Status = 1 where Driver_Id = %s"
        values = (driver_id,booking_id[0])
        print(values)
        
        con,cur = dbcon()
        cur.execute(query,values)
        cur.execute(query1,tuple(driver_id))
        con.commit()
        cur.close()
        con.close()
        win.destroy()        
        self.book_tbl.item(a,values=[*booking_id[:-1],"Accepted"])

# Top level for complete
    def complete(self):
    
        win = tk.Toplevel(self)
        win.geometry("1045x800")
        win.title("Assigned")
        
    # Complete Button 
        com_btn = tk.Button(win,text="Complete",command=self.finish)
        com_btn.place(x=200,y=300)
        
        list1 = ["Driver ID","Driver First Name","Driver Last Name","Driver Phone Number","Vehicle ID","Assign Status"]
        data1 = "select Driver_Id,Driver_Fname,Driver_Lname,Driver_Phone_Number,Vehicle_Id,Assign_Status from driver where Assign_Status = 1"
 # Frame and Treeview    
        self.frm = tk.Frame(win, width=500,height=200,background="bisque")
        self.complete_tbl = ttk.Treeview(self.frm,columns = list1, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.complete_tbl.pack()
        
        
        for i in list1:
            self.complete_tbl.column(i,stretch=NO,width=100)
            self.complete_tbl.heading(i,text=i)        
        
        con,cur = dbcon()
        cur.execute(data1)
        rows = cur.fetchall()
        cur.close()
        con.close()
      
        for i in rows:
            self.complete_tbl.insert('','end',values=i)

# Action: Completing the trip    
    def finish(self):
        con,cur = dbcon()
        query = "update driver set Assign_Status = 0 where Driver_Id = %s"
        query2 = "select Price from booking where Driver_Id = %s"
        query1 = "delete from booking where Driver_Id = %s"
        a = self.complete_tbl.selection()[0]
        driver_id = self.complete_tbl.item(a,"values")[0]
        values = tuple(driver_id)
        cur.execute(query2,values)
        price = cur.fetchone()[0]
        query3 = "insert into revenue(Revenue_Id,revenue) values (%s,%s)"
        cur.execute(query3,(0,price))
        cur.execute(query1,values)
        print(price)
        cur.execute(query,values)
        con.commit()
        cur.close()
        con.close()

    
    
    
if __name__ == "__main__":
    app = AdminDash()
    app.mainloop()