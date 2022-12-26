import tkinter as tk
from tkinter import *
from help import absPath,dbcon
from tkinter import ttk

#class dashboard(tk.Tk):
class driver_dash(tk.Frame):
   #def __init__(self):
   def __init__(self,parent,controller):
      super().__init__(parent)
      self.controller = controller
      #self.geometry("900x800")
      self.resolution = "1000x800"
      #self.resizable(False,False)
      self.title = "Driver"
    