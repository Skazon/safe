import tkinter as tk
from tkinter import ttk
import sys
import random

import code_generator


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        # self.geometry('370x600+10+10')
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        # self.overrideredirect(True)
        self.resizable(False, False)
        self.title('Сейф')
        self.iconphoto(True, tk.PhotoImage(file=r'image\safe-icon.png'))

        self.__up_button_image = tk.PhotoImage(file=r'image\up_button.png').subsample(21, 21)
        self.__down_button_image = tk.PhotoImage(file=r'image\down_button.png').subsample(21, 21)

        self.up_button_list = []
        self.down_button_list = []
        self.label_list = []
        self.safe_code, self.main_position = random_code()

        self.image_label()
        self.check_button()
        self.help1_label()
        self.help2_label()

        # self.grid_rowconfigure(0, minsize=80)

        for i in range(4):
            # self.set_ui(i)
            self.field_num(i, i)
            self.up_button(i, i)
            self.down_button(i, i)

    # def set_ui(self):
    #     exit_button = ttk.Button(self, text='Выход', command=self.app_exit)
    #     exit_button.grid(row=0, column=0)

    # def app_exit(self):
    #     self.destroy()
    #     sys.exit()

    def image_label(self):
        self.image1 = tk.PhotoImage(file=r'image\safe.png')
        self.label_image = tk.Label(self, image=self.image1)
        self.label_image.grid(rowspan=14, columnspan=18)

    def check_button(self):
        self.check_but = ttk.Button(self,
                                    text='Открыть',
                                    command=lambda: self.code_check()
                                    )
        self.check_but.grid(row=15, columnspan=18, sticky='WE')

    def help1_label(self):
        self.help1_lab = ttk.Label(self,
                                   text='Help1',
                                   background='#FFFFFF')
        self.help1_lab.grid(row=16, columnspan=18, sticky='WE')

    def help2_label(self):
        self.help2_lab = ttk.Label(self,
                                   text='Help2',
                                   background='#FFFFFF')
        self.help2_lab.grid_remove()

    def field_num(self, column_num, index_num):
        self.label_list.append(ttk.Label(self,
                                         text=0,
                                         background='#FFFFFF',
                                         padding='12 0 11 0',
                                         font='Arial 14')
                               )
        self.label_list[index_num].grid(row=5, column=column_num+7)

    def up_button(self, column_num, index_num):
        self.up_button_list.append(ttk.Button(self,
                                              image=self.__up_button_image,
                                              padding='-3 -3 -3 -3',
                                              command=lambda: self.change_num(index_num))
                                   )
        self.up_button_list[index_num].grid(row=4, column=column_num+7, sticky='S')

    def down_button(self, column_num, index_num):
        self.down_button_list.append(ttk.Button(self,
                                                image=self.__down_button_image,
                                                padding='-3 -3 -3 -3',
                                                command=lambda: self.change_num(index_num, increase=False))
                                     )
        self.down_button_list[index_num].grid(row=6, column=column_num+7, sticky='N')

    def change_num(self, index_num, increase=True):
        if increase:
            self.label_list[index_num]['text'] = (self.label_list[index_num]['text'] + 1) % 10
        else:
            self.label_list[index_num]['text'] = (self.label_list[index_num]['text'] - 1) % 10
        if self.label_list[self.main_position]['text'] == self.safe_code[self.main_position]:
            self.label_list[self.main_position]['background'] = '#00FF00'
            self.help2_lab.grid(row=17, columnspan=18, sticky='WE')
            if (self.label_list[(self.main_position + 1) % 4]['text'] == self.safe_code[(self.main_position + 1) % 4]
                    and self.label_list[(self.main_position - 1) % 4]['text'] == self.safe_code[(self.main_position - 1) % 4]):
                self.label_list[(self.main_position + 1) % 4]['background'] = '#00FF00'
                self.label_list[(self.main_position - 1) % 4]['background'] = '#00FF00'
            else:
                self.label_list[(self.main_position + 1) % 4]['background'] = '#FFFFFF'
                self.label_list[(self.main_position - 1) % 4]['background'] = '#FFFFFF'
        else:
            self.label_list[self.main_position]['background'] = '#FFFFFF'
            self.help2_lab.grid_remove()

    def code_check(self):
        # if all(self.safe_code[i] == self.label_list[i]['text'] for i in range(4)):
        if True:
            print(f'Yes')
            root2 = tk.Tk()
            root2.geometry('400x100')
            root2.attributes('-topmost', True)
            root2.overrideredirect(True)
            root2.resizable(False, True)
            root2.text_label = ttk.Label(root2, text='Удачно!')
            root2.text_label.pack(fill='both', expand=True, padx=20, pady=5,)
            root2.ok_button = tk.Button(root2, text='    OK    ', command=lambda: root2.destroy())
            root2.ok_button.pack(side='bottom', fill='none', expand=True, pady=5)
            root2.mainloop()

        else:
            print(f'No')



def random_code():
    code_list = [0, 0, 0, 0]
    main_position = random.randint(0, 3)
    code_list[main_position] = random.randint(0, 9)
    random_values = random.sample([(code_list[main_position] + 2) % 10, (code_list[main_position] - 1) % 10], 2)
    print(main_position + 1)
    print(code_list)
    if main_position != 3:
        code_list[main_position - 1], code_list[main_position + 1] = random_values
        last_value = abs(max(code_list) - (3 - main_position + (main_position % 2) * 2))  # Подумать, как лучше прописать
        code_list[main_position - 2] = last_value
    else:
        code_list[0], code_list[2] = random_values
        last_value = abs(max(code_list) - 2)
        code_list[1] = last_value
    print(code_list)
    return code_list, main_position

root = Application()
root.mainloop()