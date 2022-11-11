import tkinter as tk
from help import absPath,dbcon
from tkinter import messagebox
import re

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.resolution = "750x600"
        self.title = "Sign Up"
        
        # Adding background image
        imagepath = absPath(__file__,"../pictures/wall3.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=700, height=500)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # First Name
        fname_lbl = canvas.create_text(35,25,text="First Name",fill="black",font=("Helvatica", 10))
        
        self.fname_txt = tk.Entry(canvas)
        self.fname_txt.place(x=110, y=10, height=25, width=150)
        
        # Last Name
        lname_lbl = canvas.create_text(35,70,text="Last Name",fill="black",font=("Helvatica", 10))

        self.lname_txt = tk.Entry(canvas)
        self.lname_txt.place(x=110, y=60, height=25, width=150)
        
        # Email
        email_lbl = canvas.create_text(25,125,text="Email",fill="black",font=("Helvatica", 10))

        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=110, y=110, height=25, width=150)

        # Password
        pass_lbl = canvas.create_text(35,170,text="Password",fill="black",font=("Helvatica", 10))
        
        self.pass_txt = tk.Entry(canvas)
        self.pass_txt.place(x=110, y=160, height=25, width=150)

        # Phone number
        phone_lbl = canvas.create_text(35,215,text="Phone No",fill="black",font=("Helvatica", 10))

        self.phone_txt = tk.Entry(canvas)
        self.phone_txt.place(x=110, y=210,height=25,width=150)
        
        # Address
        address_lbl = canvas.create_text(35,270,text="Address",fill="black",font=("Helvatica", 10))
        
        self.address_txt = tk.Entry(canvas)
        self.address_txt.place(x=110,y=260, height=25, width=150)

        # Payment Method
        payment_lbl = canvas.create_text(50,320,text="Payment method",fill="black",font=("Helvatica", 10))
        
        self.payment_txt = tk.Entry(canvas)
        self.payment_txt.place(x=110,y=310, height=25, width=150)
        
        #Confirm password 
        conpass_lbl = canvas.create_text(55,375,text="Confirm password",fill="black",font=("Helvatica", 10))
        self.conpass_txt = tk.Entry(canvas)
        self.conpass_txt.place(x=110,y=360,height=25,width=150)
        
        # Login Button
        sign_btn = tk.Button(canvas, text="Sign Up",command=self.signupdb)
        sign_btn.place(x=200, y=480, height=25, width=50)
        
        
    def signupdb(self):
        
    # Validation
        # Empty field Validation
             
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.pass_txt.get()=="" or self.conpass_txt.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = self)
        
        # Password and ConfirmPassword Validation
        elif self.pass_txt.get() != self.conpass_txt.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = self)
        
        # Email Validation
        elif not re.search(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}$', self.email_txt.get().strip()):
            messagebox.showerror("Error","invalid email address", parent = self)
        
        # First Name Validation
        elif not re.search(r'^[a-zA-Z]{3,50}$',self.fname_txt.get()):
            messagebox.showerror("Error","First name should be 6-20 letters")

        # Last Name Validation
        elif not re.search(r'^[a-zA-z]{3,50}$',self.lname_txt.get()):
            messagebox.showerror("Error","Last name should be 6-20 letters",parent= self)
        
        # Password Validation
        elif not re.search(r'^[a-zA-Z0-9_@#$%&!\-]{6,16}$',self.pass_txt.get()):
             messagebox.showerror("Error","Invalid Password",parent = self)
             
        # Phone Number Validation 
        elif not re.search(r'^\d{9}$',self.phone_txt.get()):
            messagebox.showerror("Error","Phone number must be 9 digits",parent = self)
        
        else:
        #Database Connection
            con,cur = dbcon()
            query = "insert into user (User_Id,User_Fname,User_Lname,User_Address,User_Email,User_Phone_Number,Payment_Method,User_Password) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (0,self.fname_txt.get(),self.lname_txt.get(),self.address_txt.get(),self.email_txt.get(),self.phone_txt.get(),self.payment_txt.get(),self.pass_txt.get())
            cur.execute(query,values)
            con.commit()
            cur.close()
            con.close()
            self.cleardata()
            self.controller.show_frame("Login")
        
    def cleardata(self):
        self.fname_txt.delete(0,tk.END)
        self.lname_txt.delete(0,tk.END)
        self.pass_txt.delete(0,tk.END)
        self.email_txt.delete(0,tk.END)
        self.address_txt.delete(0,tk.END)
        self.conpass_txt.delete(0,tk.END)
        self.phone_txt.delete(0,tk.END)
        self.payment_txt.delete(0,tk.END)
            