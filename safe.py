import tkinter as tk
from tkinter import ttk
import sys
import random

# import code_generator


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('+10+10')
        self.attributes('-alpha', 1)
        # self.attributes('-topmost', True)
        self.resizable(False, False)
        self.title('Сейф')
        self.iconphoto(True, tk.PhotoImage(file=r'image\safe-icon.png'))

        self._up_button_image = tk.PhotoImage(file=r'image\up_button.png').subsample(21, 21)
        self._down_button_image = tk.PhotoImage(file=r'image\down_button.png').subsample(21, 21)

        self.message_dict = {
            'start': 'В «РТСофт» настали трудные времена,\nплатить зарплату стало нечем…\n'
                     'На помощь пришел СО, они положили все необходимые\nсредства в этот сейф, но '
                     'не сказали точный код от него.\n'
                     'Твоя задача по подсказкам вскрыть сейф и\nне оставить бедных сотрудников без гроша!\n'
                     'У тебя есть всего одна попытка!',
            'help1': 'Методом перебора подбери одну случайную цифру в коде',
            'help2': 'Теперь подбери две соседних цифры.\nЗнай, что одна из них больше первого числа на два,\n'
                     'а вторая - меньше на один',
            'help3': 'Осталась последняя.\nОна равна модулю разности самого большого из\n'
                     'подобранных чисел и позиции подбираемой цифры',
            'succes attempt': 'Поздравляю! У тебя получилось!\n'
                              'Отдать деньги в бухгалтерию или\nзабрать себе - решать уже тебе',
            'unsucces attempt': 'Не получилось, не фартануло!\nОпять остались без зарплаты('
        }

        self.up_button_list = []
        self.down_button_list = []
        self.label_list = []
        self.safe_code, self.main_position = random_code()

        self._image_label()
        self._check_button()
        self._help1_label()
        self._help2_label()
        self._help3_label()

        for i in range(4):
            self._field_num(i, i)
            self._up_button(i, i)
            self._down_button(i, i)

        self._code_check(greetings=True)

    # def set_ui(self):
    #     exit_button = ttk.Button(self, text='Выход', command=self.app_exit)
    #     exit_button.grid(row=0, column=0)

    # def app_exit(self):
    #     self.destroy()
    #     sys.exit()

    def _image_label(self):
        self.image1 = tk.PhotoImage(file=r'image\safe.png')
        self.label_image = tk.Label(self, image=self.image1)
        self.label_image.grid(rowspan=14, columnspan=18)

    def _check_button(self):
        self.check_but = ttk.Button(self,
                                    text='Открыть',
                                    padding='0 5 0 5',
                                    command=lambda: self._code_check()
                                    )
        self.check_but.grid(row=15, columnspan=18, sticky='WE')

    def _help1_label(self):
        self.help1_lab = ttk.Label(self,
                                   text=self.message_dict.get('help1'),
                                   padding='0 5 0 5',
                                   background='#FFFFFF')
        self.help1_lab.grid(row=16, columnspan=18, sticky='WE')

    def _help2_label(self):
        self.help2_lab = ttk.Label(self,
                                   text=self.message_dict.get('help2'),
                                   padding='0 5 0 5',
                                   background='#FFFFFF')
        self.help2_lab.grid_remove()

    def _help3_label(self):
        self.help3_lab = ttk.Label(self,
                                   text=self.message_dict.get('help3'),
                                   padding='0 5 0 5',
                                   background='#FFFFFF')
        self.help3_lab.grid_remove()

    def _field_num(self, column_num, index_num):
        self.label_list.append(ttk.Label(self,
                                         text=0,
                                         background='#FFFFFF',
                                         padding='12 0 11 0',
                                         font='Arial 14')
                               )
        self.label_list[index_num].grid(row=5, column=column_num+7)

    def _up_button(self, column_num, index_num):
        self.up_button_list.append(ttk.Button(self,
                                              image=self._up_button_image,
                                              padding='-3 -3 -3 -3',
                                              command=lambda: self._change_num(index_num))
                                   )
        self.up_button_list[index_num].grid(row=4, column=column_num+7, sticky='S')

    def _down_button(self, column_num, index_num):
        self.down_button_list.append(ttk.Button(self,
                                                image=self._down_button_image,
                                                padding='-3 -3 -3 -3',
                                                command=lambda: self._change_num(index_num, increase=False))
                                     )
        self.down_button_list[index_num].grid(row=6, column=column_num+7, sticky='N')

    def _change_num(self, index_num, increase=True):
        if increase:
            self.label_list[index_num]['text'] = (self.label_list[index_num]['text'] + 1) % 10
        else:
            self.label_list[index_num]['text'] = (self.label_list[index_num]['text'] - 1) % 10
        if self.label_list[self.main_position]['text'] == self.safe_code[self.main_position]:
            self.label_list[self.main_position]['background'] = '#00FF7F'
            self.help2_lab.grid(row=17, columnspan=18, sticky='WE')
            if (self.label_list[(self.main_position + 1) % 4]['text'] == self.safe_code[(self.main_position + 1) % 4]
                    and self.label_list[(self.main_position - 1) % 4]['text'] == self.safe_code[(self.main_position - 1) % 4]):
                self.label_list[(self.main_position + 1) % 4]['background'] = '#00FF7F'
                self.label_list[(self.main_position - 1) % 4]['background'] = '#00FF7F'
                self.help3_lab.grid(row=18, columnspan=18, sticky='WE')
            else:
                self.label_list[(self.main_position + 1) % 4]['background'] = '#FFFFFF'
                self.label_list[(self.main_position - 1) % 4]['background'] = '#FFFFFF'
        else:
            self.label_list[self.main_position]['background'] = '#FFFFFF'
            self.label_list[(self.main_position + 1) % 4]['background'] = '#FFFFFF'
            self.label_list[(self.main_position - 1) % 4]['background'] = '#FFFFFF'
            self.help2_lab.grid_remove()
            self.help3_lab.grid_remove()

    def _code_check(self, greetings=False):
        root2 = tk.Toplevel()
        # root2_width = self.winfo_width()
        root2.minsize(368, 10)
        root2.geometry(f'+18+200')
        root2.attributes('-topmost', True)
        root2.overrideredirect(True)
        root2.resizable(False, True)
        root2.text_label = tk.Label(root2)
        root2.text_label.pack(fill='both', expand=True, padx=10, pady=5)
        root2.ok_button = tk.Button(root2, text='    OK    ', command=lambda: self._code_restart(root2))
        root2.ok_button.pack(side='bottom', fill='none', expand=True, pady=5)
        if greetings:
            root2.text_label['text'] = self.message_dict.get('start')
        elif all(self.safe_code[i] == self.label_list[i]['text'] for i in range(4)):
            root2.text_label['text'] = self.message_dict.get('succes attempt')
        else:
            root2.text_label['text'] = self.message_dict.get('unsucces attempt')
        root2.mainloop()

    def _code_restart(self, window):
        self.safe_code, self.main_position = random_code()
        window.destroy()



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