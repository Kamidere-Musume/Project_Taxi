import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk

#class dashboard(tk.Tk):
class dashboard(tk.Frame):
   #def __init__(self):
   def __init__(self,parent,controller):
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
      start_lbl = canvas.create_text(70,123, text="Current Location",fill="white",font=("Helvatica",10))

      self.start_txt = tk.Entry(canvas)
      self.start_txt.place(x=145,y=110, height=25, width=150)
      
      # Destination 
      desti_lbl = canvas.create_text(650,123,text="Destination",fill="white", font=("Helvatica",10))
      
      self.desti_txt = tk.Entry(canvas)
      self.desti_txt.place(x=700,y = 110, height=25,width=150)
       
      # Book Button
      bookbtn = tk.Button(canvas,text="Book",command = self.bookingdb)
      bookbtn.place(x=500,y=250,height=30,width=60)
      
      # Distance slider
      distance_lbl = canvas.create_text(40,250,text="Distance",fill="white", font=("Helvatica",10))
      
      self.distance_slid = tk.Scale(canvas, from_=0, to =100,orient="horizontal")
      self.distance_slid.place(x=145,y=230)
       
      # Getting value from slider
      value = IntVar()
      value.set(self.distance_slid.get())
      
      def getvalue(event):
          value.set(self.calc())
          self.dis_lbl.config(textvariable=value)
      
      self.distance_slid.bind("<B1-Motion>",getvalue)
      self.distance_slid.bind("<ButtonRelease-1>",getvalue)
     

       
      # Price 
      price_lbl = canvas.create_text(40,345,text="Price",fill="white", font=("Helvatica",10))
      self.dis_lbl = Label(canvas,text=self.calc())
      self.dis_lbl.place(x=200,y=300)
      
      
   def bookingdb(self):
      con,cur = dbcon()
      query = "insert into booking(Booking_Id,User_Id,Current_location,Destination,Price,Distance,Booking_Status) values(%s,%s,%s,%s,%s,%s,%s)"
      values = (0,self.controller.user_id,self.start_txt.get(),self.desti_txt.get(),self.calc(),self.distance_slid.get(),"Pending")
      cur.execute(query,values)
      con.commit()
      cur.close()
      con.close()
      #self.cleardata()
   
   def calc(self):
         ppk = 50
         val = self.distance_slid.get()
         
         return "Rs"+ str(val * ppk)
      
if __name__=="__main__":
   app = dashboard()
   app.mainloop()

    