import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk
from tkinter import messagebox
import csv
from ttkwidgets.autocomplete import AutocompleteCombobox
#class Dashboard(tk.Tk):
class Dashboard(tk.Frame):
   graph = dict()
   def __init__(self,parent,controller):
      
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
               
      super().__init__(parent)
      self.controller = controller
      #self.geometry("900x800")
      self.resolution = "1000x800"
      #self.resizable(False,False)
      self.title = "Dashboard"
        
   # Adding background image 
      imagepath = absPath(__file__,"../pictures/wall1.png")
      bg = tk.PhotoImage(file=imagepath)
      canvas = tk.Canvas(self, width=500, height=300)
      canvas.pack(fill="both", expand=True)
      canvas.image = bg
      canvas.create_image(0, 0, image=bg, anchor="nw")


   
          

     
      # Title 
      title_lbl = canvas.create_text(450,50,text="Taxi Booking",fill="white",font=("Helvatica",15))

   # Start
      # Start Label 
      start_lbl = canvas.create_text(70,123, text="Current Location",fill="white",font=("Helvatica",10))
      
      # Start Auto complete
      self.start_txt = AutocompleteCombobox(
         canvas, 
         width=30, 
         font=('Helvatica', 10),
         completevalues=list(self.graph.keys())
         )
      self.start_txt.place(x=145,y=110, height=25, width=150)
      
   # Destination 
      # Destination Label
      desti_lbl = canvas.create_text(650,123,text="Destination",fill="white", font=("Helvatica",10))
      
      # Destination Auto complete
      self.desti_txt = AutocompleteCombobox(
         canvas, 
         width=30, 
         font=('Helvatica', 10),
         completevalues=list(self.graph.keys())
         )
      self.desti_txt.place(x=700,y = 110, height=25,width=150)
       
   # Book Button
      bookbtn = tk.Button(canvas,text="Book",command = self.bookingdb)
      bookbtn.place(x=500,y=250,height=30,width=60)
     
   # Distance Label
      distance_lbl = canvas.create_text(40,250,text="Distance",fill="white", font=("Helvatica",10))
      
      self.dis_lbl = Label(canvas,text="0 Km")
      self.dis_lbl.place(x=200,y=250)
           
   # Price Label
      price_lbl = canvas.create_text(40,345,text="Price",fill="white", font=("Helvatica",10))
      self.price_lbl = Label(canvas,text="Rs 0")
      self.price_lbl.place(x=200,y=300)
      
   # Search Button 
      src_btn = tk.Button(canvas,text="Search",command = self.search)
      src_btn.place(x = 400, y= 250,height=30,width=60)
      
      print(self.graph)
# Database Connection  
   def bookingdb(self):
      con,cur = dbcon()
      query = "insert into booking(Booking_Id,User_Id,Current_location,Destination,Price,Distance,Booking_Status) values(%s,%s,%s,%s,%s,%s,%s)"
      values = (0,self.controller.user_id,self.start_txt.get(),self.desti_txt.get(),self.price_lbl.cget("text"),self.dis_lbl.cget("text"),"Pending")
      cur.execute(query,values)
      con.commit()
      cur.close()
      con.close()
      messagebox.showinfo("Book","Booked")
   
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
        
   def search(self):
      start = self.start_txt.get()
      desti = self.desti_txt.get()
      
      if not start or not desti or not start in self.graph or not desti in self.graph:
         messagebox.showerror("Error","Location not found") 

      distance, price = self.location(start,desti)
      self.dis_lbl.config(text= f'{str(distance)} Km')
      self.price_lbl.config(text= f'Rs {str(price)}')
   
if __name__=="__main__":
   app = Dashboard()
   app.mainloop()

    