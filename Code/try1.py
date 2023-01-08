
from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk

class Signin1(tk.Tk): 
    def __init__(self):
        super().__init__()
        #Creating window 
        self.geometry('800x500')
        self.title("SIGN IN PAGE")

        myFrame= tk.Frame()
        myFrame.pack()

        #Creating a frame
        self.frame1=tk.Frame(self,width=390,height=490, bg="#d9d9d9")
        self.frame1.place(x=404,y=5)

        #signin text label
        self.signin_lbl=tk.Label(text="SIGN IN PAGE",height=2, width=20,bg="#57a1f8",fg="White")
        self.signin_lbl.place(x=250 , y= 10)

        #type text 
        # self.dob = tk.list(["Driver","Customer","Admin"])
        # self.dob.insert(0,"User Type")

        # self.cb = ttk.Combobox(self.frame1, values=self.dob,state="readonly")
        # self.cb.current(0)
        # self.cb.place(x=180,y=30)

        #ID Label 
        self.ID_lbl= tk.Label(self.frame1,text="User ID",bg="#d9d9d9")
        self.ID_lbl.place(x=100,y=120)

        #ID text
        # self.ID_txt= tk.Entry(self.frame1,width=20,bg="white", border=0)
        # self.ID_txt.place(x=200,y=120)
        # self.ID_txt.insert(0,"Username")
        # self.ID_txt.bind('<FocusIn>',self.user_enter)

        #Password Label 
        self.Pass_lbl=tk. Label(self.frame1,text="Password",bg="#d9d9d9")
        self.Pass_lbl.place(x=100,y=170)

        #Password text
        # self.Pass_txt=tk.Entry(self.frame1,width=20,bg="white", border=0)
        # self.Pass_txt.place(x=200,y=170)
        # self.Pass_txt.insert(0,"Password")
        # self.Pass_txt.bind('<FocusIn>',self.pass_enter)

        #Sign in button
        self.Signin_btn=tk.Button(self.frame1,text="Sign in",fg="white",bg="#57a1f8",height=1,width=13,border=0)
        self.Signin_btn.place(x=120,y=220)

        #Sign up button
        self.Signup_btn=tk. Button(self.frame1,text="Sign up",fg="white",bg="#57a1f8",height=1,width=13,border=0)
        self.Signup_btn.place(x=250,y=220)

        #Forgot password
        self.Forgot_password= tk.Label(self.frame1,text="Forgot User ID or Password ?",fg="green",bg="#d9d9d9")
        self.Forgot_password.place(x=150,y=270)

# #Functioality part
#     def clear(self):
#         self.ID_txt.delete(0,tk.END)
#         self.Pass_txt.delete(0,tk.END)
        
#     def Login_User(self):
#         if self.ID_txt.get()=='' or self.Pass_txt.get()=='':
#             messagebox.showerror("Error","The feilds are empty")
#         else:
#             if self.cb.get()=="Customer": 
#                 try:
#                     self.mydb=mysql.connector.connect(host="localhost",user="root",password="root")
#                     self.mycursor=self.mydb.cursor()
#                 except:
#                     messagebox.showerror("Error","Connection is not instablished")
#                     return
#                 self.quary='use taxi'
#                 self.mycursor.execute(self.quary)
#                 self.quary='select * from Customer_Data where Cus_Email=%s and Cus_Pass=%s'
#                 self.mycursor.execute(self.quary,(self.ID_txt.get(),self.Pass_txt.get()))
#                 self.row=self.mycursor.fetchone()
#                 if self.row==None:
#                     messagebox.showerror("Error","Wrong user id or password")
#                 else:
#                     print(self.row[0])
#                     messagebox.showinfo("Success","Login successful")
#                     self.clear()
#                     self.destroy()
#                     import booking
#             elif self.cb.get()=="Driver":
#                 try:
#                     self.mydb=mysql.connector.connect(host="localhost",user="root",password="root")
#                     self.mycursor=self.mydb.cursor()
#                 except:
#                     messagebox.showerror("Error","Connection is not instablished")
#                     return
#                 self.quary='use taxi'
#                 self.mycursor.execute(self.quary)
#                 self.quary='select * from Driver_Data where D_Email=%s and D_Pass=%s'
#                 self.mycursor.execute(self.quary,(self.ID_txt.get(),self.Pass_txt.get()))
#                 self.row=self.mycursor.fetchone()
#                 if self.row==None:
#                     messagebox.showerror("Error","Wrong user id or password")
#                 else: 
#                     messagebox.showinfo("Success","Login successful")
#                     self.clear()
#                     self.destroy()
#                     import dashboard_driver
#             elif self.cb.get()=="Admin":
#                 messagebox.showinfo('Not Avilable','The usertype is not avilabe')
#             else:
#                 messagebox.showerror("abc",'abc')

#     def user_enter(self,event):
#         if self.ID_txt.get()=='Username':
#             self.ID_txt.delete(0,tk.END)
        
#     def pass_enter(self,event):
#         if self.Pass_txt.get()=='Password':
#             self.Pass_txt.delete(0,tk.END)
        
#     def clicker(self):
#         if self.cb.get()=="Customer":
#             self.destroy()
#             import registartion
#         elif self.cb.get()=="Driver":
#             self.destroy()
#             import driver_regs
#         else:
#             messagebox.showerror('Error','Please select user type')

#     def callback(self):
#         print(self.cb.get())
    
if __name__=="__main__":
    app=Signin1()
    app.mainloop()