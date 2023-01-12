import tkinter as tk
from help import absPath,dbcon
from tkinter import messagebox
from tkinter import ttk

class Login(tk.Frame):
    
    def __init__(self, parent, controller):
        
        super().__init__(parent)
        self.controller = controller
        self.resolution = "900x600"
        self.title= "Login"
        
    # Adding background image
        imagepath = absPath(__file__,"../pictures/loginwall1.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=802, height=887)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

    #Title 
        title_lbl = canvas.create_text(700,80,text="Login Page",fill="black",font=("Century",25,"bold"))
        
    # Email
        # Email Label
        email_lbl = canvas.create_text(700,180,text="Email",fill="black",font=("Century", 15))
        
        # Email Entry Box
        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=620, y=200, height=25, width=180)
        
    # Password
        # Password Label
        pass_lbl = canvas.create_text(700,280,text="Password",fill="black",font=("Century", 15))

        # Password Entry Box
        self.pass_txt = tk.Entry(canvas,show="*",font="Century 11")
        self.pass_txt.place(x=620, y=300, height=25, width=180)

    # User Type
        # User Label
        user_lbl = canvas.create_text(700,380,text="User Type",fill="black",font=("Century", 15))
        
        # User Combobox
        self.user_box = ttk.Combobox(canvas,state="readonly",
        values=["Customer","Driver"])
        self.user_box.place(x=620, y= 400,height=25,width=180)
        
    # Login Button
        login_btn = tk.Button(canvas, text="Login",command=self.logindb)
        login_btn.place(x=650, y=480, height=25, width=50)
        
    # Sign up Button
        signup_btn = tk.Button(
            canvas, text="Sign Up", command=lambda: controller.show_frame("Signup")
        )
        signup_btn.place(x=720, y=480, height=25, width=50)
        

# Database Connection        
    def logindb(self):
        try:
            con,cur = dbcon()
            query = "select * from user where User_Email = %s and User_Password = %s "
            query2 = "select * from driver where Driver_Email = %s and Driver_Password = %s"
            values = (self.email_txt.get(),self.pass_txt.get())
            
        # Validtaion
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
                        messagebox.showinfo("Info","Logged in Sucessful")
                        self.controller.show_frame("Dashboard")
                
            # Driver Dashboard
                else:
                    cur.execute(query2,values)
                    myresult = cur.fetchall() 
                
                    if len(myresult)<1:
                        messagebox.showerror("Error","Email or Password incorrect")
                    
                    elif len(myresult)>0:
                        self.controller.user_id = myresult[0][0]
                        self.controller.show_frame("DriverDash")
            
            cur.close()
            con.close()
        except Exception as e:
            print(e)
            messagebox.showerror("Error","Failed to connect to database")