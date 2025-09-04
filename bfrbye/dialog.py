import tkinter as tk
from tkinter import simpledialog

def show_input_dialog(response):
    newWin = tk.Tk()
    newWin.attributes('-alpha', 0)  # make the window invisible, withdraw doesn't allow to show on top
    newWin.lift()
    newWin.attributes('-topmost',True)
    
    res = simpledialog.askstring("Hands up!", "Tell me why",parent=newWin)
    response.append(res)
    newWin.destroy() 
