import tkinter as tk
from tkinter import simpledialog

def show_input_dialog(response):
    newWin = tk.Tk() 
    newWin.withdraw() 
    res = simpledialog.askstring("Hands up!", "Tell me why",parent=newWin)
    response.append(res)
    newWin.destroy() 