import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox
import csv
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkcalendar import DateEntry
from datetime import date


class Dashboard(tk.Frame):
   
   graph = dict()
   
   def __init__(self,parent,controller):
      
      super().__init__(parent)
      self.controller = controller
      self.resolution = "1000x800"
      self.title = "Dashboard"
        
      # Adding Locations 
      def addLocation(a, b, distance):
         if a not in self.graph:
            self.graph[a] = [(b, distance)]
         else:
            self.graph[a].append((b, distance))

      with open("D:\Assignment\Assignment-1\Code\distance_lib.csv") as f:
         reader = csv.reader(f)
         for row in reader:
            a, b = row[0].split("-")
            addLocation(a, b, int(row[1]))
            addLocation(b, a, int(row[1]))
               
     
   # Adding background image 
      imagepath = absPath(__file__,"../pictures/booking1.png")
      bg = tk.PhotoImage(file=imagepath)
      canvas = tk.Canvas(self, width=500, height=300)
      canvas.pack(fill="both", expand=True)
      canvas.image = bg
      canvas.create_image(0, 0, image=bg, anchor="nw")
      
   # Frame
      frame = tk.Frame(canvas,highlightbackground="black",highlightthickness=2,width=900, height=500, bd= 0)
      frame.place(x=0,y=450)
      
   # Title 
      title_lbl = canvas.create_text(450,50,text="Taxi Booking",fill="black",font=("Century",15))
      
   # Start
      # Start Label 
      start_lbl = canvas.create_text(70,123, text="Current Location",fill="black",font=("Century",12))
      
      # Start Auto complete
      self.start_txt = AutocompleteCombobox(
         canvas, 
         width=30, 
         font=('Century', 10),
         completevalues=list(self.graph.keys())
         )
      self.start_txt.place(x=145,y=110, height=25, width=150)
      
   # Destination 
      # Destination Label
      desti_lbl = canvas.create_text(650,123,text="Destination",fill="black", font=("Century",12))
      
      # Destination Auto complete
      self.desti_txt = AutocompleteCombobox(
         canvas, 
         width=30, 
         font=('Century', 10),
         completevalues=list(self.graph.keys())
         )
      self.desti_txt.place(x=700,y = 110, height=25,width=150)
   
   # Date
      # Date Label
      date_lbl = canvas.create_text(70,200,text="Pick Up Date",fill="black", font=("Century",12))
      
      # Date Entry Box
      self.date_txt = DateEntry(canvas,selectmode='day')
      self.date_txt.place(x=145,y=190,height=25, width=150)
      

   # Distance Label
      distance_lbl = canvas.create_text(60,280,text="Distance",fill="black", font=("Century",12))
      
      self.dis_lbl = Label(canvas,text="0 Km")
      self.dis_lbl.place(x=150,y=270,width=150)
           
   # Price Label
      price_lbl = canvas.create_text(630,280,text="Price",fill="black", font=("Century",12))
      
      self.price_lbl = Label(canvas,text="Rs 0")
      self.price_lbl.place(x=700,y=270,width=150)
      
# Time
      # Time Label
      time_lbl = canvas.create_text(630,200,text="Pick Up Time",fill="black", font=("Century",12))
      
      # Time Entry Box
      self.v = tk.StringVar()
      self.time_txt = tk.Entry(canvas,textvariable=self.v)
      self.time_txt.place(x=700,y=190,height=25, width=150)
     
      
   # Search Button 
      src_btn = tk.Button(canvas,text="Search",command = self.search)
      src_btn.place(x = 250, y= 350,height=30,width=60)
      
   # Update Button 
      update_btn = tk.Button(canvas,text="Update",command=self.updatedb)
      update_btn.place(x=350, y= 350,height=30,width=60)
      
   # Book Button
      bookbtn = tk.Button(canvas,text="Book",command = self.bookingdb)
      bookbtn.place(x=450,y=350,height=30,width=60)
    
     # Cancel Booking Button
      cancel_btn = tk.Button(canvas,text="Cancel",command=self.cancel)
      cancel_btn.place(x=550,y=350,height=30,width=60)
        
   # Sign out Button 
      signbtn = tk.Button(canvas,text="Sign Out",command = lambda: self.destroy())
      signbtn.place(x=900,y=10,height=30,width=60)
      
  
   #Tree View for the customer booking 
      # List of data for table
      list1 = ["User ID","Booking ID","User First Name","User Last Name","Current Location","Destination","Pick Up Date","Pick Up Time","Price","Distance","Booking Status"]   
      data1 = "select user.User_Id,booking.Booking_Id,user.User_fname, user.User_lname,booking.Current_location,booking.Destination,booking.Pickup_Date,booking.Pickup_Time,booking.Price,booking.Distance,booking.Booking_Status From booking inner join user on User.User_Id = booking.User_Id;"
      
      self.complete_tbl = ttk.Treeview(frame,columns = list1, show="headings",height="18")
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
      
      self.complete_tbl.bind("<Double-1>",self.showvalue)


# Calculation distance and price 
   def location(self,a,b):
      if a == b:
         return 0,0
      
      work = [{'at':a,'route':[],'distance':0}]
      i = 0
      while i < len(work):
        at = work[i]['at']
        distance = work[i]['distance']
        route = work[i]['route']
        for place in self.graph[at]:
            if place[0] == b:
                temp = distance + place[1]
                return (temp,temp*15)
             
            if not any([i['at'] == place[0] for i in work]):
                work.append({'at':place[0],'route':[*route,place],'distance':distance+place[1]})
        i += 1
     
     
# Searching for the location   
   def search(self):
      start = self.start_txt.get()
      desti = self.desti_txt.get()
      
      if not start or not desti or not start in self.graph or not desti in self.graph:
         messagebox.showerror("Error","Location not found") 

      distance, price = self.location(start,desti)
      self.dis_lbl.config(text= f'{str(distance)} Km')
      self.price_lbl.config(text= f'Rs {str(price)}')
   
      
# Database Connection  
   # Booking
   def bookingdb(self):
      con,cur = dbcon()
      query = "insert into booking(Booking_Id,User_Id,Current_location,Destination,Price,Distance,Booking_Status,Pickup_Date,Pickup_Time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      values = (0,self.controller.user_id,self.start_txt.get(),self.desti_txt.get(),self.price_lbl.cget("text"),self.dis_lbl.cget("text"),"Pending",self.date_txt.get(),self.time_txt.get())
      cur.execute(query,values)
      con.commit()
      cur.close()
      con.close()
      messagebox.showinfo("Book","Booked")
      self.complete_tbl(values=[self.start_txt.get(),self.desti_txt.get(),self.date_txt.get(),self.time_txt.get(),self.price_lbl.cget("text"),self.dis_lbl.cget("text"),"Accepted"])


   # Showing value
   def showvalue(self,event):
      item = self.complete_tbl
      
      selection = self.complete_tbl.selection()[0]
      customer_id = self.complete_tbl.item(selection,"values")

      start_ind = self.start_txt["values"].index(customer_id[4])
      self.start_txt.current(start_ind)
      
      desti__ind = self.desti_txt["values"].index(customer_id[5])
      self.desti_txt.current(desti__ind)
      
      self.price_lbl.config(text=customer_id[8])
      self.dis_lbl.config(text=customer_id[9])
      
      date_ind = list(map(int,customer_id[6].split("/")))
      self.date_txt.set_date(date(date_ind[2],date_ind[0],date_ind[1]))
      
      self.v.set(customer_id[7])
    
    
# Cancel Booking
   def cancel(self,a,booking_id):
      a = self.driverbook_tbl.selection()[0]
      driver_id = self.driverbook_tbl.item(a,"values")[0]
      
      con,cur = dbcon()
      query = "delete * from booking where Booking_id = %s"
      values = (driver_id,booking_id[0])
      
      cur.execute(query,values)
      con.commit()
      cur.close()
      con.close()
      messagebox.showinfo("Book","Booked")


      
   # Updating values
   def updatedb(self):
      con,cur = dbcon()
      query = "update booking set Current_Location = %s,Destination = %s,Price=%s,Distance = %s,Pickup_Date = %s,Pickup_Time = %s where Booking_Id = %s"
      selection = self.complete_tbl.selection()[0]
      customer_id = self.complete_tbl.item(selection,"values")
      values = (self.start_txt.get(),self.desti_txt.get(),self.price_lbl.cget("text"),self.dis_lbl.cget("text"),self.date_txt.get(),self.time_txt.get(),customer_id[1])
      cur.execute(query,values)
      con.commit()
      cur.close()
      con.close()
      print(customer_id)
      self.complete_tbl.item(selection,values=[*customer_id[:4],self.start_txt.get(),self.desti_txt.get(),self.date_txt.get(),self.time_txt.get(),self.price_lbl.cget("text"),self.dis_lbl.cget("text"),"Accepted"])
    
    