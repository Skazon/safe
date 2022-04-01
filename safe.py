import tkinter as tk
from tkinter import ttk
import sys

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x600+10+10')
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        # self.overrideredirect(True)
        self.resizable(False, False)
        self.title('Сейф')
        self.iconphoto(True, tk.PhotoImage(file=(r'image\safe-icon.png')))

        self.set_ui()

    def set_ui(self):
        exit_button = ttk.Button(self, text='Выход', command=self.app_exit)
        exit_button.pack(fill=tk.X)

    def app_exit(self):
        self.destroy()
        sys.exit()






root = Application()
root.mainloop()