import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox

#class driverdash(tk.Tk):
class DriverDash(tk.Frame):
   #def __init__(self):
   def __init__(self,parent,controller):
      super().__init__(parent)
      self.controller = controller
      #self.geometry("1045x800")
      self.resolution = "1000x800"
      #self.resizable(False,False)
      self.title = "Driver"

      # Adding Background Image 
       # Adding background image 
      imagepath = absPath(__file__,"../pictures/wall3.png")
      bg = tk.PhotoImage(file=imagepath)
      canvas = tk.Canvas(self, width=1000, height=800)
      canvas.pack(fill="both", expand=True)
      canvas.image = bg
      canvas.create_image(0, 0, image=bg, anchor="nw")
      
      # Adding title 
      title_lbl = canvas.create_text(500,100,text="Booking Requests",fill="white",font=("Helvatica",15))
      
      # Adding Frame and tree view
      self.frm = tk.Frame(canvas, width=1045,height=500,background="bisque")
      self.frm.place(relx=.5,rely=.7, anchor="c")
      self.book_tbl = ttk.Treeview(self.frm, columns=(1,2,3,4,5,6,7,8,9,10), show="headings",height="10")
      self.book_tbl.pack()

      # Adding scrollbar in tree view 
      self.scroll = ttk.Scrollbar(self.frm,orient="vertical",command= self.book_tbl.yview)
      self.scroll.place(x=1025, y = 25, height=200)
      
      self.book_tbl.configure(yscrollcommand=self.scroll.set)
      # Adding tree view data in table
      self.book_tbl.column(1,stretch = NO,width=80)
      self.book_tbl.heading(1, text="Booking ID")

      self.book_tbl.column(2,stretch = NO,width=80)      
      self.book_tbl.heading(2,text="User ID")
      
      self.book_tbl.column(3,stretch = NO,width=110)      
      self.book_tbl.heading(3,text="User First Name")
      
      self.book_tbl.column(4,stretch = NO,width=110)      
      self.book_tbl.heading(4,text="User Last Name")
      
      self.book_tbl.column(5,stretch = NO,width=110)      
      self.book_tbl.heading(5,text="User Number")
      
      self.book_tbl.column(6,stretch = NO,width=110)      
      self.book_tbl.heading(6,text="Pick up")
      
      self.book_tbl.column(7,stretch = NO,width=110)
      self.book_tbl.heading(7,text="Destination")
      
      self.book_tbl.column(8,stretch = NO,width=110)      
      self.book_tbl.heading(8,text="Price")
      
      self.book_tbl.column(9,stretch = NO,width=110)
      self.book_tbl.heading(9,text="Distance")

      self.book_tbl.column(10,stretch=NO,width=110)
      self.book_tbl.heading(10,text="Booking Status")

      # Creating Button 
      show_btn  = tk.Button(canvas, text="Show Requests",command=self.showtable)
      show_btn.place(x=800, y=300, height=25, width=90)

      # Confirm Button
      con_btn = tk.Button(canvas,text="Accept",command = self.accept)
      con_btn.place(x=800,y=400,height=25, width=90)
      
      
   # Showing the data in database
   def showtable(self):
      con,cur = dbcon()
      query = "select booking.Booking_Id,user.User_Id,user.User_fname, user.User_lname, user.User_phone_Number,booking.Current_location,booking.Destination,booking.Price,booking.Distance,booking.Booking_Status From booking inner join user on User.User_Id = booking.User_Id;"
      cur.execute(query)
      rows = cur.fetchall()
      con.commit()
      cur.close()
      con.close()
      
      for i in rows:
         self.book_tbl.insert('','end',values=i)

   def accept(self):
      a = self.book_tbl.selection()[0]
      booking_id = self.book_tbl.item(a,"values")
      
      if booking_id[-1].strip() == "Accepted":
         messagebox.showerror("Error","Already Accepted")
         return
         
      con,cur = dbcon()
      query = "update booking set Booking_Status = 'Accepted' where Booking_Id = %s"
      value = tuple(booking_id[0])
      cur.execute(query,value)
      con.commit()
      cur.close()
      con.close()
   
      self.book_tbl.item(a,values=[*booking_id[:-1],"Accepted"])
      
   
if __name__=="__main__":
   app = DriverDash()
   app.mainloop()
    