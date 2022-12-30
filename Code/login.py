import tkinter as tk
from help import absPath,dbcon
from tkinter import messagebox
from tkinter import ttk

class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.resolution = "802x887+500+50"
        self.title= "Login"
        
        # Adding background image
        imagepath = absPath(__file__,"../pictures/login.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=802, height=887)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

        #Title 
        title_lbl = canvas.create_text(580,150,text="Login Page",fill="white",font=("Vladimir Script",25,"bold"))
        
        
        # Email
        email_lbl = canvas.create_text(580,270,text="Email",fill="white",font=("Terminal", 15))
        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=500, y=300, height=25, width=180)
        
        # Password
        pass_lbl = canvas.create_text(580,370,text="Password",fill="white",font=("Terminal", 15))

        self.pass_txt = tk.Entry(canvas,show="*",font="Terminal 11")
        self.pass_txt.place(x=500, y=400, height=25, width=180)

        # User Type
        user_lbl = canvas.create_text(580,470,text="User Type",fill="white",font=("Terminal", 15))
        
        self.user_box = ttk.Combobox(canvas,state="readonly",
        values=["Customer","Driver"])
        self.user_box.place(x=500, y= 500,height=25,width=180)
        
        # Login Button
        login_btn = tk.Button(canvas, text="Login",command=self.logindb)
        login_btn.place(x=500, y=630, height=25, width=50)
        # Sign up Button
        signup_btn = tk.Button(
            canvas, text="Sign Up", command=lambda: controller.show_frame("Signup")
        )
        signup_btn.place(x=600, y=630, height=25, width=50)
        
        # Database Connection
        
    def logindb(self):
        con,cur = dbcon()
        query = "select * from user where User_Email = %s and User_Password = %s "
        query2 = "select * from driver where Driver_Email = %s and Driver_Password = %s"
        values = (self.email_txt.get(),self.pass_txt.get())
        
        # Empty field validation
        if self.email_txt.get()=="" and self.pass_txt.get()=="":
                messagebox.showerror("Error","Fill the box")
         
        # Empty combobox validation        
        elif self.user_box.get()=="":
            messagebox.showerror("Error","Select User Type")
        
        else:
            # Customer Dashboardd
            if self.user_box.get() == "Customer":
                cur.execute(query,values)
                myresult = cur.fetchall()
               
                
                if len(myresult)<1:
                    messagebox.showerror("Error","Email or Password incorrect")
                
                elif len(myresult)>0:
                    self.controller.user_id = myresult[0][0]
                    self.controller.show_frame("dashboard")
            
            # Driver Dashboard
            else:
                cur.execute(query2,values)
                myresult = cur.fetchall() 
            
                if len(myresult)<1:
                    messagebox.showerror("Error","Email or Password incorrect")
                
                elif len(myresult)>0:
                    self.controller.driver_id = myresult[0]
                    self.controller.show_frame("driver_dash")
           
        cur.close()
        con.close()
      