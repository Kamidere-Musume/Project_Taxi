import tkinter as tk
from logindb import dbcon
import os 

class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.resolution = "500x300"
        self.title = "Login"
        # Adding background image
        
        #imagepath = os.path.abspath("../pictures/wall3.png")
        bg = tk.PhotoImage(file="../pictures/wall3.png")
        canvas = tk.Canvas(self, width=500, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # Email
        email_lbl = tk.Label(canvas, text="Email")
        email_lbl.place(x=10, y=10)

        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=100, y=10, height=25, width=150)
        
        # Password
        pass_lbl = tk.Label(canvas, text="Password")
        pass_lbl.place(x=10, y=60)

        self.pass_txt = tk.Entry(canvas)
        self.pass_txt.place(x=100, y=60, height=25, width=150)

        # Login Button
        login_btn = tk.Button(canvas, text="Login",command=self.logindb)
        login_btn.place(x=200, y=100, height=25, width=50)

        # Sign up Button
        signup_btn = tk.Button(
            canvas, text="Sign Up", command=lambda: controller.show_frame("Signup")
        )
        signup_btn.place(x=300, y=100, height=25, width=50)
        
        
    def logindb(self):
        con,cur = dbcon()
        query = "select * from user where User_Email = %s and User_Password = %s "
        values = (self.email_txt.get(),self.pass_txt.get())
        print(values)
        cur.execute(query,values)
        myresult = cur.fetchall()
        
        if len(myresult)>0:
           self.controller.show_frame("Signup")

        cur.close()
        con.close()
       
        