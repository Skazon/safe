import tkinter as tk
from tkinter import ttk
import sys
import random

class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x600+10+10')
        self.grid_rowconfigure(2, minsize=100)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        # self.overrideredirect(True)
        self.resizable(False, True)
        self.title('Сейф')
        self.iconphoto(True, tk.PhotoImage(file=(r'image\safe-icon.png')))

        self.up_button_list = []
        self.down_button_list = []
        self.label_list = []
        self.safe_code, self.main_position = random_code()

        self.image_label()
        self.check_button()
        self.help1_label()
        self.help2_label()

        for i in range(4):
            # self.set_ui(i)
            self.field_num(i, i)
            self.down_button(i, i)
            self.up_button(i, i)

    # def set_ui(self):
    #     exit_button = ttk.Button(self, text='Выход', command=self.app_exit)
    #     exit_button.grid(row=0, column=0)

    #
    # def app_exit(self):
    #     self.destroy()
    #     sys.exit()

    def image_label(self):
        self.image1 = tk.PhotoImage(file='safe_PNG56.png')
        self.label_image = tk.Label(self, image=self.image1)
        self.label_image.grid(rowspan=4, columnspan=4)

    def check_button(self):
        self.check_but = ttk.Button(self,
                                    text='Открыть',
                                    command=lambda: self.code_check()
                                    )
        self.check_but.grid(row=4, columnspan=4, sticky='WE')

    def help1_label(self):
        self.help1_lab = ttk.Label(self,
                                   text='Help1',
                                   background='white')
        self.help1_lab.grid(row=5, columnspan=4, sticky='WE')

    def help2_label(self):
        self.help2_lab = ttk.Label(self,
                                   text='Help2',
                                   background='white')
        self.help2_lab.grid_remove()

    def field_num(self, column_num, index_num):
        self.label_list.append(ttk.Label(self,
                                        text=0,
                                        background='white')
                               )
        self.label_list[index_num].grid(row=1, column=column_num)

    def up_button(self, column_num, index_num):
        self.up_button_list.append(ttk.Button(self,
                                              text='Up',
                                              command=lambda: self.change_num(index_num))
                                   )
        self.up_button_list[index_num].grid(row=0, column=column_num)

    def down_button(self, column_num, index_num):
        self.down_button_list.append(ttk.Button(self,
                                                text='Down',
                                                command=lambda: self.change_num(index_num, increase=False))
                                     )
        self.down_button_list[index_num].grid(row=2, column=column_num)

    def change_num(self, index_num, increase=True):
        if increase:
            self.label_list[index_num]['text'] = (self.label_list[index_num]['text'] + 1) % 10
        else:
            self.label_list[index_num]['text'] = (self.label_list[index_num]['text'] - 1) % 10
        if self.label_list[self.main_position]['text'] == self.safe_code[self.main_position]:
            self.label_list[self.main_position]['background'] = 'green'
            self.help2_lab.grid(row=6, columnspan=4, sticky='WE')
            if (self.label_list[(self.main_position + 1) % 4]['text'] == self.safe_code[(self.main_position + 1) % 4]
                    and self.label_list[(self.main_position - 1) % 4]['text'] == self.safe_code[(self.main_position - 1) % 4]):
                self.label_list[(self.main_position + 1) % 4]['background'] = 'green'
                self.label_list[(self.main_position - 1) % 4]['background'] = 'green'
            else:
                self.label_list[(self.main_position + 1) % 4]['background'] = 'white'
                self.label_list[(self.main_position - 1) % 4]['background'] = 'white'
        else:
            self.label_list[self.main_position]['background'] = 'white'
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