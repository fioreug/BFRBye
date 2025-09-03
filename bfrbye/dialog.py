import tkinter as tk
from tkinter import simpledialog

def show_input_dialog(prompt: str) -> str | None:
    root = tk.Tk() # needed?
    root.withdraw() # needed?
    return simpledialog.askstring("Hands up!", "Tell me why")