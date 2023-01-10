import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox

class AdminDash(tk.Tk):
    
    revenue = 0
    def __init__(self):
        
        super().__init__()
        self.geometry("1045x800")
        self.title("Admin")

    # Adding Background Image 
        imagepath = absPath(__file__,"../pictures/admin2.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=500, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")
        
    # Title 
        title_lbl = canvas.create_text(500,50,text="Admin",fill="black",font=("Century",25))
 
    # Customer Search Button
        self.cuslist_btn = tk.Button(canvas,text="User list",command= self.customerlist,background="#CCCCFF")
        self.cuslist_btn.place(x=150,y=700,height=80,width=100)
    
     # Driver search Button
        self.drivlist_btn = tk.Button(canvas,text="Driver List",command=self.driverlist,background="#CCCCFF")
        self.drivlist_btn.place(x=270,y=700,height=80,width=100)
               
    # Booking List Button
        self.bookinglist_btn = tk.Button(canvas,text="Booking list",command= self.bookinglist,background="#CCCCFF")
        self.bookinglist_btn.place(x=390,y=700,height=80,width=100)
    
     # Histor Button
        self.history_btn = tk.Button(canvas,text="History",command=self.history,background="#CCCCFF")
        self.history_btn.place(x=510,y=700,height=80,width=100)
    
    # Revenue Button
        self.revenue_btn = tk.Button(canvas,text="Revenue",command=self.revenue,background="#CCCCFF")
        self.revenue_btn.place(x=630,y=700,height=80,width=100)
    
    # Exit Buttone
        self.exit_btn = tk.Button(canvas,text="Exit",command= lambda: self.destroy() ,background="#CCCCFF")
        self.exit_btn.place(x=750,y=700,height=80,width=100)

        
# Top level for customer list
    def customerlist(self):
        
        win = tk.Toplevel(self)
        win.geometry("1000x400")
        win.title("Assigned")
        win.resizable(False,False)
    # frame 
        self.frm1 = tk.Frame(win, width=1045,height=800,background="#89a7b1")
        self.frm1.place(relx=.5,rely=.1, anchor="c")
    # Title 
        title_lbl = tk.Label(win,text="Customer List",font=("Century",18),background="#89a7b1")
        title_lbl.place(x=400,y=60)
    
    # back Button
        back_btn = tk.Button(win,text="<-Back",command= lambda : win.destroy())
        back_btn.place(x=10,y=10) 
        
 # Search Box
        # customerlistorary Text
        def temp_text(e):
            self.search_txt.delete(0,"end")
            
        # Search Entry Box
        self.search_txt = tk.Entry(win)
        self.search_txt.insert(0,"Search")
        self.search_txt.bind("<FocusIn>",temp_text)
        self.search_txt.place(x=350,y=100, height=25, width=140)   
        
    # Search Button 
        search_btn = tk.Button(win,text="Search",command=self.custsearch)
        search_btn.place(x=200,y=100)
        
        list1 = ["CustomerID","Customer First Name","Customer Last Name","Customer Phone Number","Custome Address","Payment Method","Customer Email","Customer Password"]
        data1 = "select User_Id,User_Fname,User_Lname,User_Phone_Number,User_Address,Payment_Method,User_Email,User_Password from user"

 # Frame and Treeview    
        self.frm = tk.Frame(win, width=1045,height=200)
        self.complete_tbl = ttk.Treeview(self.frm,columns = list1, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.complete_tbl.pack()
        
        for i in list1:
            self.complete_tbl.column(i,stretch=NO,width=120)
            self.complete_tbl.heading(i,text=i)        
        
        con,cur = dbcon()
        cur.execute(data1)
        rows = cur.fetchall()
        cur.close()
        con.close()
      
        for i in rows:
            self.complete_tbl.insert('','end',values=i)
            
            
#Top level for Driver list
    def driverlist(self):
    
        win = tk.Toplevel(self)
        win.geometry("960x400")
        win.title("Assigned")
        win.resizable(False,False)
            
    # frame 
        self.frm1 = tk.Frame(win, width=960,height=800,background="#89a7b1")
        self.frm1.place(relx=.5,rely=.1, anchor="c")
        
    # Title 
        title_lbl = tk.Label(win,text="Driver List",font=("Century",18),background="#89a7b1")
        title_lbl.place(x=400,y=60)
    
    # back Button
        back_btn = tk.Button(win,text="<-Back",command= lambda : win.destroy())
        back_btn.place(x=10,y=10)
         
 # Search Box
        # customerlistorary Text
        def temp_text(e):
            self.search_txt1.delete(0,"end")
            
        # Search Entry Box
        self.search_txt1 = tk.Entry(win)
        self.search_txt1.place(x=350, y=150,height=25,width=150)
        self.search_txt1.insert(0,"Search")
        self.search_txt1.bind("<FocusIn>",temp_text)
        self.search_txt1.place(x=350,y=100, height=25, width=140)
        
    # Search Button 
        search_btn = tk.Button(win,text="Search",command=self.drivesearch)
        search_btn.place(x=200,y=100)
        
        list1 = ["Driver ID","Driver First Name","Driver Last Name","Driver Phone Number","Vehicle ID","Driver Address","Driver Email","Driver Password"]
        data1 = "select Driver_Id,Driver_Fname,Driver_Lname,Driver_Phone_Number,Vehicle_Id,Driver_Address,Driver_Email,Driver_Password from driver"
        
 # Frame and Treeview    
        self.frm = tk.Frame(win, width=500,height=200,background="bisque")
        self.complete_tbl = ttk.Treeview(self.frm,columns = list1, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.complete_tbl.pack()
        
        
        for i in list1:
            self.complete_tbl.column(i,stretch=NO,width=115)
            self.complete_tbl.heading(i,text=i)        
        
        con,cur = dbcon()
        cur.execute(data1)
        rows = cur.fetchall()
        cur.close()
        con.close()
      
        for i in rows:
            self.complete_tbl.insert('','end',values=i)       
            
            
# Top level for bookinglist
    def bookinglist(self):
        win = tk.Toplevel(self)
        win.geometry("1040x400")
        win.title("Booking List")
        win.resizable(False,False)
           
    # frame 
        self.frm1 = tk.Frame(win, width=1040,height=800,background="#89a7b1")
        self.frm1.place(relx=.5,rely=.1, anchor="c")
        
    # Title 
        title_lbl = tk.Label(win,text="Booking List",font=("Century",18),background="#89a7b1")
        title_lbl.place(x=400,y=60)
 
    # back Button
        back_btn = tk.Button(win,text="<-Back",command= lambda : win.destroy())
        back_btn.place(x=10,y=10) 
        
    # Customer List Data 
        list2 = ["Booking ID","User ID","User First Name","User Last Name","User Phone Number","Current Location","Destination","Price","Distance","Booking Status"]
        data2 = "select booking.Booking_Id,user.User_Id,user.User_fname, user.User_lname, user.User_phone_Number,booking.Current_location,booking.Destination,booking.Price,booking.Distance,booking.Booking_Status From booking inner join user on User.User_Id = booking.User_Id where Booking_Status = 'Pending'"

    # Assign Button
        self.assin_btn = tk.Button(win,text="Assign",command = self.bookingassign)
        self.assin_btn.place(x=200,y=100,width=55,height=40)
        
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

        
# Top Level For Booking Assign 
    def bookingassign(self):
        
    # Data selection for customer    
        a = self.book_tbl.selection()[0]
        booking_id = self.book_tbl.item(a,"values")

        win = tk.Toplevel(self)
        win.geometry("1045x800")
        win.title("Driver")
        win.resizable(False,False)
        
                  
    # frame 
        self.frm1 = tk.Frame(win, width=1045,height=150,background="#89a7b1")
        self.frm1.place(relx=.5,rely=.1, anchor="c")
        
    # back Button
        back_btn = tk.Button(win,text="<-Back",command= lambda : win.destroy())
        back_btn.place(x=10,y=10) 
        
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


# Top level for history
    def history(self):
        
        win = tk.Toplevel(self)
        win.geometry("960x400")
        win.title("Assigned")
        win.resizable(False,False) 
    
    # frame 
        self.frm1 = tk.Frame(win, width=960,height=800,background="#a7dbd8")
        self.frm1.place(relx=.5,rely=.1, anchor="c")
        
    # Title 
        title_lbl = tk.Label(win,text="History",font=("Century",18),background="#a7dbd8")
        title_lbl.place(x=400,y=60)
 
 # back Button
        back_btn = tk.Button(win,text="<-Back",command= lambda : win.destroy())
        back_btn.place(x=10,y=10) 
        
 # Search Box
        # customerlistorary Text
        def temp_text(e):
            self.search_txt1.delete(0,"end")
            
        # Search Entry Box
        self.search_txt1 = tk.Entry(win)
        self.search_txt1.place(x=350, y=150,height=25,width=150)
        self.search_txt1.insert(0,"Search")
        self.search_txt1.bind("<FocusIn>",temp_text)
        self.search_txt1.place(x=350,y=100, height=25, width=140)
        
    # Search Button 
        search_btn = tk.Button(win,text="Search",command=self.drivesearch)
        search_btn.place(x=200,y=100)
        
        list1 = ["Driver ID","Driver First Name","Driver Last Name","Driver Phone Number","Vehicle ID","Driver Address","Driver Email","Driver Password"]
        data1 = "select Driver_Id,Driver_Fname,Driver_Lname,Driver_Phone_Number,Vehicle_Id,Driver_Address,Driver_Email,Driver_Password from driver"
        
 # Frame and Treeview    
        self.frm = tk.Frame(win, width=500,height=200,background="bisque")
        self.complete_tbl = ttk.Treeview(self.frm,columns = list1, show="headings",height="10",)

        self.frm.place(relx=.5,rely=.7, anchor="c")
        self.complete_tbl.pack()
        
        
        for i in list1:
            self.complete_tbl.column(i,stretch=NO,width=115)
            self.complete_tbl.heading(i,text=i)        
       
        rows = self.historydb()
        for i in rows:
            self.complete_tbl.insert('','end',values=i)       
            

                        
# function for customer search
    def custsearch(self):
        items = self.complete_tbl.get_children()
        for item in items:
            custid = self.complete_tbl.item(item,"values")[0]
            custemail = self.complete_tbl.item(item,"values")[6]
            if custid == self.search_txt.get() or custemail == self.search_txt.get():
                self.complete_tbl.selection_set(item)
                break
            else:
                self.complete_tbl.selection_remove(item)

        else:
            messagebox.showinfo("Info","User doesnot exist")
            
# Functio for driversearch
    def drivesearch(self):
        items = self.complete_tbl.get_children()
        for item in items:
            custid = self.complete_tbl.item(item,"values")[0]
            custemail = self.complete_tbl.item(item,"values")[6]
            if custid == self.search_txt1.get() or custemail == self.search_txt1.get():
                self.complete_tbl.selection_set(item)
                break
            else:
                self.complete_tbl.selection_remove(item)

        else:
            messagebox.showinfo("Info","Driver doesnot exist")
    
             
# Action: Accepting booking
    def accept(self,booking_id,win,a):
        
        a = self.driverbook_tbl.selection()[0]
        driver_id = self.driverbook_tbl.item(a,"values")[0]
        
        query = "update booking set Booking_Status = 'Assigned',Driver_Id = %s where Booking_Id = %s"
        query1 = "update driver set Assign_Status = 1 where Driver_Id = %s"
        values = (driver_id,booking_id[0])
        
        con,cur = dbcon()
        cur.execute(query,values)
        cur.execute(query1,tuple(driver_id))
        con.commit()
        cur.close()
        con.close()
        win.destroy()        
        self.book_tbl.item(a,values=[*booking_id[:-1],"Accepted"])


# Action: History
    def historydb(self):
        con,cur = dbcon()
        query = "select * from booking where Booking_Status = 'Completed'"
        cur.execute(query)
        data =  cur.fetchall()
        cur.close()
        con.close()
        return data
    
# Action: Revenue 
    def revenue(self):
        con,cur = dbcon()
        query = "select Price from booking where Booking_Status = 'Completed'"
        cur.execute(query)
        price = cur.fetchall()
        cur.close()
        con.close()
        total = sum([int(i[0][3:].strip()) for i in price])
   
        
if __name__ == "__main__":
    app = AdminDash()
    app.mainloop()