import tkinter as tk
from help import absPath,dbcon

class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.resolution = "300x400"
        self.title = "Login"
        
        # Adding background image
        imagepath = absPath(__file__,"../pictures/wall1.png")
        bg = tk.PhotoImage(file=imagepath)
        canvas = tk.Canvas(self, width=500, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.image = bg
        canvas.create_image(0, 0, image=bg, anchor="nw")

        # Email
        email_lbl = canvas.create_text(25,70,text="Email",fill="black",font=("Helvatica", 10))
        self.email_txt = tk.Entry(canvas)
        self.email_txt.place(x=100, y=60, height=25, width=150)
        
        # Password
        pass_lbl = canvas.create_text(35,125,text="Password",fill="black",font=("Helvatica", 10))

        self.pass_txt = tk.Entry(canvas)
        self.pass_txt.place(x=100, y=110, height=25, width=150)
   
        # Login Button
        login_btn = tk.Button(canvas, text="Login",command=self.logindb)
        login_btn.place(x=50, y=170, height=25, width=50)
        # Sign up Button
        signup_btn = tk.Button(
            canvas, text="Sign Up", command=lambda: controller.show_frame("Signup")
        )
        signup_btn.place(x=150, y=170, height=25, width=50)
        
        
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
       