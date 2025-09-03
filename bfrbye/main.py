import tkinter as tk
from bfrbye.config import load_config, save_config
from bfrbye.tracker import HandTracker

class BFRByeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BFRBye")
        self.config = load_config()
        
        self.btn_config = tk.Button(self.root, text="Configuration", command=self.open_config)
        self.btn_config.pack(pady=10)

        self.btn_start = tk.Button(self.root, text="Start", command=self.start_tracking)
        self.btn_start.pack(pady=10)

        self.tracker = None

    def open_config(self):
        # TODO: open a simple config dialog
        pass

    def start_tracking(self):
        # TODO: run in a separate thread? - can't use tkinter after minimizing

        self.root.iconify()  # minimize
        self.tracker = HandTracker(self.config)
        self.tracker.run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BFRByeApp()
    app.run()
