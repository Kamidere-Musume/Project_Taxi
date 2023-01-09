import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox


class DriverDash(tk.Frame):
   
   def __init__(self,parent,controller):    
        
      super().__init__(parent)
      self.controller = controller
      self.resolution = "1000x500"
      self.title="Driver"

   # Adding Background Image     
      imagepath = absPath(__file__,"../pictures/booking1.png")
      bg = tk.PhotoImage(file=imagepath)
      canvas = tk.Canvas(self, width=1010, height=800)
      canvas.pack(fill="both", expand=True)
      canvas.image = bg
      canvas.create_image(0, 0, image=bg, anchor="nw")
      
   # Adding title 
      title_lbl = canvas.create_text(500,100,text="Booking Requests",fill="black",font=("Century",25))
      
   # Adding Frame and tree view
      self.frm = tk.Frame(canvas, width=1045,height=800,background="bisque")
      self.frm.place(relx=.5,rely=.8, anchor="c")
      
   # list for Table
      list1 = ["Booking ID","User ID","First Name","Last Name","Phone Number","Pick Up","Drop","Price","Distance","Booking Status"]  
      self.book_tbl = ttk.Treeview(self.frm,columns = list1, show="headings",height="10",)
      self.book_tbl.pack()
      
      for i in list1:
         self.book_tbl.column(i,stretch=NO,width=100)
         self.book_tbl.heading(i,text=i)
         
    # Creating Button 
      show_btn  = tk.Button(canvas, text="Show Requests",command=self.show)
      show_btn.place(x=700, y=200, height=30, width=90)

   # Complete Button 
      com_btn = tk.Button(canvas,text="Complete",command=self.complete)
      com_btn.place(x=800,y=200,height=30, width=90)
   
   
# Showing data in table    
   def show(self):
      print(self.controller.user_id)
      data1 =  "select booking.Booking_Id,user.User_Id,user.User_fname, user.User_lname, user.User_phone_Number,booking.Current_location,booking.Destination,booking.Price,booking.Distance,booking.Booking_Status From booking inner join user on User.User_Id = booking.User_Id where Driver_Id = %s and Booking_Status = 'Assigned'";
      con,cur = dbcon()
      cur.execute(data1,tuple(str(self.controller.user_id)))
      rows = cur.fetchall()
      cur.close()
      con.close()
      
      for i in rows:
            self.book_tbl.insert('','end',values=i)
    
    
# Completing data in table  
   def complete(self):
      con,cur = dbcon()
      query = "update driver set Assign_Status = 0 where Driver_Id = %s"
      query1 = "update booking set Booking_Status = 'Completed' where Booking_Id = %s"
      a = self.book_tbl.selection()[0]
      booking_id = self.book_tbl.item(a,"values")[0]
      values = tuple(booking_id)
      
      cur.execute(query,values)
      cur.execute(query1,values)
   
      con.commit()
      cur.close()
      con.close()
      