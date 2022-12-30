import tkinter as tk
from help import absPath,dbcon
from tkinter import messagebox
from tkinter import ttk
import re
from login import Login

class Signup(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.resolution = "772x960"
        self.title = "Sign Up"
        
    # Adding background image
        imagepath = absPath(__file__,"../pictures/register.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=772, height=975)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

    # First Name
        # First Name Label
        fname_lbl = canvas.create_text(200,170,text="First Name",fill="black",font=("Terminal", 12))
        
        # First Name Entry Box
        self.fname_txt = tk.Entry(canvas)
        self.fname_txt.place(x=350, y=160, height=25, width=150)
        
    # Last Name
        # Last Name Label   
        lname_lbl = canvas.create_text(200,220,text="Last Name",fill="black",font=("Terminal", 12))

        # Last Name Entry Box
        self.lname_txt = tk.Entry(canvas)
        self.lname_txt.place(x=350, y=210, height=25, width=150)
        
    # Email
        # Email Label
        email_lbl = canvas.create_text(200,270,text="Email",fill="black",font=("Terminal", 12))

        # Email Entry Box
        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=350, y=260, height=25, width=150)

    # Password
        # Password Label
        pass_lbl = canvas.create_text(200,320,text="Password",fill="black",font=("Terminal", 12))
        
        # Password Entry Box
        self.pass_txt = tk.Entry(canvas)
        self.pass_txt.place(x=350, y=310, height=25, width=150)

        #Confirm password 
        conpass_lbl = canvas.create_text(200,375,text="Confirm password",fill="black",font=("Terminal", 12))
        
        self.conpass_txt = tk.Entry(canvas)
        self.conpass_txt.place(x=350,y=360,height=25,width=150)
        
        # Address
        address_lbl = canvas.create_text(200,425,text="Address",fill="black",font=("Terminal", 12))
        
        self.address_txt = tk.Entry(canvas)
        self.address_txt.place(x=350,y=410, height=25, width=150)
        
        # User Type
        
        user_lbl = canvas.create_text(200,575,text="User Type",fill="black",font=("Terminal", 12))
        self.user_box = ttk.Combobox(canvas,state="readonly",
        values=["Customer","Driver"])
        self.user_box.place(x=350, y= 560,height=25,width=150)
        
        # Payment Method
        payment_lbl = canvas.create_text(200,475,text="Payment method",fill="black",font=("Terminal", 12))

        # Adding background text 
        def temp_text(e):
            self.payment_txt.delete(0,"end")
            
        self.payment_txt = tk.Entry(canvas)
        self.payment_txt.insert(0,"Only for User")
        self.payment_txt.bind("<FocusIn>",temp_text)
        self.payment_txt.place(x=350,y=460, height=25, width=150)
          
        # Phone number
        phone_lbl = canvas.create_text(200,525,text="Phone No",fill="black",font=("Terminal", 12))

        self.phone_txt = tk.Entry(canvas)
        self.phone_txt.place(x=350, y=510,height=25,width=150)
        
        # Vehcile Number 
        vechile_lbl = canvas.create_text(200,625,text="Vehcile ID",fill="black",font=("Terminal", 12))
        
        self.vechile_txt = tk.Entry(canvas)
        self.vechile_txt.place(x=350,y=610,height=25,width=150)
        
        # Login Button
        sign_btn = tk.Button(canvas, text="Sign Up",command=self.signupdb)
        sign_btn.place(x=360, y=660, height=30, width=80)
        
        # Back button 
        back_btn = tk.Button(canvas, text="Back",command=lambda: controller.show_frame("Login"))
        back_btn.place(x=25,y=30,height=30,width=60)
        
        
        
        
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
        elif not re.search(r'^\d{10}$',self.phone_txt.get()):
            messagebox.showerror("Error","Phone number must be 9 digits",parent = self)
        
        else:
            if self.user_box.get()=="Driver":
                con,cur = dbcon()
                query = "insert into driver (Driver_Id,Driver_Fname,Driver_Lname,Driver_Email,Driver_Phone_Number,Driver_Password,Vehicle_Id,Driver_Address) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (0,self.fname_txt.get(),self.lname_txt.get(),self.email_txt.get(),self.phone_txt.get(),self.pass_txt.get(),self.vechile_txt.get(),self.address_txt.get())
                cur.execute(query,values)
                con.commit()
                cur.close()
                con.close()
                self.cleardata()
                self.controller.show_frame("Login")
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
            