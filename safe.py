import tkinter as tk
from tkinter import ttk
import sys

import code_generator


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('200x280+10+10')
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        # self.overrideredirect(True)
        self.resizable(False, False)
        self.title('Сейф')
        self.iconphoto(True, tk.PhotoImage(file=r'image\safe-icon.png'))
        self.__up_button_image = tk.PhotoImage(file=r'image\up_button.png').subsample(40, 40)
        self.__down_button_image = tk.PhotoImage(file=r'image\down_button.png').subsample(40, 40)

        # self.grid_rowconfigure(0, minsize=80)
        for i in range(4):
            self.grid_columnconfigure(i, minsize=50)
            self.up_button(0, i)
            self.down_button(2, i)

    # def set_ui(self):
    #     exit_button = ttk.Button(self, text='Выход', command=self.app_exit)
    #     exit_button.grid(row=0, column=2)

    # def app_exit(self):
    #     self.destroy()
    #     sys.exit()

    def up_button(self, row_number: int, column_number: int):
        up_button = ttk.Button(self,
                               image=self.__up_button_image,
                               command=self.up_number,
                               padding='-2 -2 -2 -2'
                               )
        up_button.grid(row=row_number, column=column_number)

    def up_number(self):
        pass

    def down_button(self, row_number: int, column_number: int):
        down_button = ttk.Button(self,
                                 image=self.__down_button_image,
                                 command=self.down_number,
                                 padding='-2 -2 -2 -2',
                                 )
        down_button.grid(row=row_number, column=column_number)

    def down_number(self):
        pass






root = Application()
root.mainloop()