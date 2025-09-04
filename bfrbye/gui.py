import tkinter as tk
from tkinter import messagebox
from threading import Thread
from .config import load_config, save_config
from .tracker import HandTracker

def create_main_window():
    """
    Creates the main application window with Start and Configuration buttons.
    """
    root = tk.Tk()
    root.title("BFRBye")

    # Load config
    config = load_config()

    # Tracker instance

    tracker = HandTracker(config)

    def start_tracking():
        root.iconify()  # Minimiza ventana
        
        thread = Thread(target=tracker.run, daemon=True)
        thread.start()
        start_button.config(text="Running", state="disabled")

    # Buttons
    start_button = tk.Button(root, text="Start", command=start_tracking)
    start_button.pack(pady=10)

    config_button = tk.Button(root, text="Configuration", command=lambda: open_config_window(root, config))
    config_button.pack(pady=10)

    return root

def open_config_window(parent, config):
    win = tk.Toplevel(parent)
    win.title("Configuration")

    # Notion token
    tk.Label(win, text="Notion Token:").grid(row=0, column=0, sticky="w")
    token_entry = tk.Entry(win, width=40)
    token_entry.insert(0, config["notion"].get("token", ""))
    token_entry.grid(row=0, column=1, padx=5, pady=5)

    # Database ID
    tk.Label(win, text="Database ID:").grid(row=1, column=0, sticky="w")
    db_entry = tk.Entry(win, width=40)
    db_entry.insert(0, config["notion"].get("database_id", ""))
    db_entry.grid(row=1, column=1, padx=5, pady=5)

    # Storage methods (checkboxes)
    tk.Label(win, text="Storage methods:").grid(row=2, column=0, sticky="w")
    methods = {"csv": tk.BooleanVar(), "txt": tk.BooleanVar(), "notion": tk.BooleanVar()}
    for i, method in enumerate(methods):
        methods[method].set(method in config["storage"].get("methods", []))
        tk.Checkbutton(win, text=method.upper(), variable=methods[method]).grid(row=2, column=1+i, padx=5)

    # Save button
    def save_and_close():
        config["notion"]["token"] = token_entry.get().strip()
        config["notion"]["database_id"] = db_entry.get().strip()
        config["storage"]["methods"] = [m for m, var in methods.items() if var.get()]
        save_config(config)
        messagebox.showinfo("Saved", "Configuration saved successfully")
        win.destroy()

    tk.Button(win, text="Save", command=save_and_close).grid(row=3, column=0, columnspan=3, pady=10)