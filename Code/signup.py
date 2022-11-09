import tkinter as tk
from logindb import dbcon
import os

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.resolution = "750x600"
        self.title = "Sign Up"
        
        # Adding background image
        bg = tk.PhotoImage(file="../pictures/wall1.png")
        canvas = tk.Canvas(self, width=700, height=500)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # First Name
        fname_lbl = tk.Label(canvas, text="First Name")
        fname_lbl.place(x=10, y=10)
        
        self.fname_txt = tk.Entry(canvas)
        self.fname_txt.place(x=100, y=10, height=25, width=150)
        
        # Last Name
        lname_lbl = tk.Label(canvas, text="Last Name")
        lname_lbl.place(x=10, y=300)

        self.lname_txt = tk.Entry(canvas)
        self.lname_txt.place(x=100, y=300, height=25, width=150)
        # Email
        email_lbl = tk.Label(canvas, text="Email")
        email_lbl.place(x=10, y=60)

        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=100, y=60, height=25, width=150)

        # Password
        pass_lbl = tk.Label(canvas, text="Password")
        pass_lbl.place(x=10, y=110)

        self.pass_txt = tk.Entry(canvas)
        self.pass_txt.place(x=100, y=110, height=25, width=150)

        # Phone number
        phone_lbl = tk.Label(canvas, text="Phone No")
        phone_lbl.place(x=10, y=160)

        self.phone_txt = tk.Entry(canvas)
        self.phone_txt.place(x=100, y=160)
        
        # Address
        address_lbl = canvas.create_text(100,100,text="Address",fill="white")
        
        self.address_txt = tk.Entry(canvas)
        self.address_txt.place(x=100,y=380)

        # Payment Method
        payment_lbl = canvas.create_text(100,200,text="Payment method",fill="white")
        
        self.payment_txt = tk.Entry(canvas)
        self.payment_txt.place(x=100,y=430)
        # Login Button
        sign_btn = tk.Button(canvas, text="Sign Up",command=self.signupdb)
        sign_btn.place(x=200, y=210, height=25, width=50)
        
        
    
    def signupdb(self):
        con,cur = dbcon()
        query = "insert into user (User_Id,User_Fname,User_Lname,User_Address,User_Email,User_Phone_Number,Payment_Method,User_Password) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (0,self.fname_txt.get(),self.lname_txt.get(),self.address_txt.get(),self.email_txt.get(),self.phone_txt.get(),self.payment_txt.get(),self.pass_txt.get())
        cur.execute(query,values)
        con.commit()
        cur.close()
        con.close()
        self.controller.show_frame("Login")
        
        
        
        