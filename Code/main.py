import tkinter as tk
from login import Login
from signup import Signup


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Taxi Booking")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Signup, Login):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        self.geometry(frame.resolution)
        self.title(frame.title)
        frame.tkraise()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()