import tkinter as tk
from help import absPath,dbcon
from tkinter import messagebox
from tkinter import ttk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1045x800")
        self.title("Login")
        
    # Adding background image
        # imagepath = absPath(__file__,"../pictures/login.png")
        # bg = tk.PhotoImage(file=imagepath)
        # canvas = tk.Canvas(self, width=802, height=887)
        # canvas.pack(fill="both", expand=True)
        # canvas.image = bg
        # canvas.create_image(0, 0, image=bg, anchor="nw")

        frame = tk.Frame(self,highlightbackground="blue",highlightthickness=2,width=600, height=400, bd= 0)
        frame.pack(padx=10,pady=20)


if __name__ =="__main__":
    app = Login()
    app.mainloop()