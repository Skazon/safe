import tkinter as tk
from tkinter import ttk
import random


def image_label(root: tk.Tk):
    """Загружает картинку сейфа и размещает ее."""
    label_image = tk.Label(root, image=image1)
    label_image.grid(rowspan=14, columnspan=18)


def check_button(root: tk.Tk):
    """Создает кнопку "Открыть" и размещает ее."""
    check_but = ttk.Button(root,
                           text='Открыть',
                           padding='0 5 0 5',
                           command=lambda: second_window(root))
    check_but.grid(row=15, columnspan=18, sticky='WE')


def help1_label(root: tk.Tk):
    """Создает виджет первой подсказки и размещает его."""
    root.help1_lab = ttk.Label(root,
                               text=message_dict.get('help1'),
                               padding='0 5 0 5',
                               background='#FFFFFF')
    root.help1_lab.grid(row=16, columnspan=18, sticky='WE')


def help2_label(root: tk.Tk):
    """Создает виджет второй подсказки и скрывает его."""
    root.help2_lab = ttk.Label(root,
                               text=message_dict.get('help2'),
                               padding='0 5 0 5',
                               background='#FFFFFF')
    root.help2_lab.grid_remove()


def help3_label(root: tk.Tk):
    """Создает виджет третьей подсказки и скрывает его."""
    root.help3_lab = ttk.Label(root,
                               text=message_dict.get('help3'),
                               padding='0 5 0 5',
                               background='#FFFFFF')
    root.help3_lab.grid_remove()


def field_num(root: tk.Tk, column_num: int, index_num: int):
    """Создает виджет отображения цифр кода и размещает его."""
    label_list.append(ttk.Label(root,
                                text=0,
                                background='#FFFFFF',
                                padding='12 0 11 0',
                                font='Arial 14')
                      )
    label_list[index_num].grid(row=5, column=column_num + 7)


def up_button(root: tk.Tk, column_num: int, index_num: int):
    """Создает кнопку "Up" и размещает ее."""
    up_button_list.append(ttk.Button(root,
                                     image=up_button_image,
                                     padding='-3 -3 -3 -3',
                                     command=lambda: change_num(index_num))
                          )
    up_button_list[index_num].grid(row=4, column=column_num + 7, sticky='S')


def down_button(root: tk.Tk, column_num: int, index_num: int):
    """Создает кнопку "Down" и размещает ее."""
    down_button_list.append(ttk.Button(root,
                                       image=down_button_image,
                                       padding='-3 -3 -3 -3',
                                       command=lambda: change_num(index_num, increase=False))
                            )
    down_button_list[index_num].grid(row=6, column=column_num + 7, sticky='N')


def change_num(index_num: int, increase: bool = True):
    """Изменяет цифру кода.

    Подсвечивает "главную" цифру, если она подобрана верно.
    Подсвечивает две соседних цифры от "главной", если все они подобраны верно.
    Args:
        index_num: Порядок цифры
        increase: True если увеличение цифры, False - если уменьшение
    """
    if increase:
        label_list[index_num]['text'] = (label_list[index_num]['text'] + 1) % 10
    else:
        label_list[index_num]['text'] = (label_list[index_num]['text'] - 1) % 10
    if label_list[root.main_position]['text'] == root.safe_code[root.main_position]:
        label_list[root.main_position]['background'] = '#00FF7F'
        root.help2_lab.grid(row=17, columnspan=18, sticky='WE')
        if (label_list[(root.main_position + 1) % 4]['text'] == root.safe_code[(root.main_position + 1) % 4]
                and label_list[(root.main_position - 1) % 4]['text'] == root.safe_code[(root.main_position - 1) % 4]):
            label_list[(root.main_position + 1) % 4]['background'] = '#00FF7F'
            label_list[(root.main_position - 1) % 4]['background'] = '#00FF7F'
            root.help3_lab.grid(row=18, columnspan=18, sticky='WE')
        else:
            label_list[(root.main_position + 1) % 4]['background'] = '#FFFFFF'
            label_list[(root.main_position - 1) % 4]['background'] = '#FFFFFF'
    else:
        label_list[root.main_position]['background'] = '#FFFFFF'
        label_list[(root.main_position + 1) % 4]['background'] = '#FFFFFF'
        label_list[(root.main_position - 1) % 4]['background'] = '#FFFFFF'
        root.help2_lab.grid_remove()
        root.help3_lab.grid_remove()


def second_window(parent: tk.Tk, greetings: bool = False):
    """Создает второе окно с кнопкой "ОК".

    Выводит сообщение в зависимости от игровой ситуации.
    Args:
        parent: Родительское окно - возможно можно убрать
        greetings: True только при первом запуске игры
    """
    child_window = tk.Toplevel()
    # root2_width = self.winfo_width()
    child_window.minsize(368, 10)
    child_window.geometry(f'+18+200')
    child_window.attributes('-topmost', True)
    child_window.overrideredirect(True)
    child_window.resizable(False, True)
    child_window.text_label = tk.Label(child_window)
    child_window.text_label.pack(fill='both', expand=True, padx=10, pady=5)
    child_window.ok_button = tk.Button(child_window,
                                       text='    OK    ',
                                       command=lambda: code_restart(parent, child_window))
    child_window.ok_button.pack(side='bottom', fill='none', expand=True, pady=5)
    if greetings:
        child_window.text_label['text'] = message_dict.get('start')
    elif all(root.safe_code[i] == label_list[i]['text'] for i in range(4)):
        child_window.text_label['text'] = message_dict.get('succes attempt')
        root.life_points = 2
    else:
        root.life_points -= 1
        if root.life_points == 1:
            child_window.text_label['text'] = message_dict.get('first unsucces attempt')
        else:
            child_window.text_label['text'] = message_dict.get('second unsucces attempt')
            root.life_points = 2
    child_window.mainloop()


def code_restart(parent: tk.Tk, window: tk.Toplevel):
    """Закрывает второе окно и обновляет искомый код, если это начало игры или закончились жизни."""
    parent.attributes('-topmost', True)  # Возможно можно только один раз задать приоритет основного окна
    window.destroy()
    if root.life_points == 2:
        root.safe_code, root.main_position = random_code()
        root.help2_lab.grid_remove()
        root.help3_lab.grid_remove()
        for i in range(4):
            label_list[i]['text'] = 0
            label_list[i]['background'] = '#FFFFFF'


def initiate_interface():
    """Размещает все виджеты на главном окне и запускает окно приветствия"""
    image_label(root)
    check_button(root)
    help1_label(root)
    help2_label(root)
    help3_label(root)
    for i in range(4):
        field_num(root, i, i)
        up_button(root, i, i)
        down_button(root, i, i)
    second_window(root, greetings=True)


def random_code():
    """Генерирует рандомный код.

    Выбирается случайная цифра в коде. От нее определяются две соседних цифры -
    одна из них всегда больше на 2, а другая всегда меньше на 1.
    Последняя цифра определяется модулем разности порядка последней цифры и максимальной из подобранных цифр.
    """
    code_list = [0, 0, 0, 0]
    main_position = random.randint(0, 3)
    code_list[main_position] = random.randint(0, 9)
    random_values = random.sample([(code_list[main_position] + 2) % 10, (code_list[main_position] - 1) % 10], 2)
    if main_position != 3:
        code_list[main_position - 1], code_list[main_position + 1] = random_values
        last_value = abs(
            max(code_list) - (3 - main_position + (main_position % 2) * 2))  # Подумать, как лучше прописать
        code_list[main_position - 2] = last_value
    else:
        code_list[0], code_list[2] = random_values
        last_value = abs(max(code_list) - 2)
        code_list[1] = last_value
    print(code_list)
    return code_list, main_position


root = tk.Tk()
root.geometry('+10+10')
root.attributes('-alpha', 1)
root.resizable(False, False)
root.title('Сейф')
root.iconphoto(True, tk.PhotoImage(file=r'image\safe-icon.png'))
image1 = tk.PhotoImage(file=r'image\safe.png')
up_button_image = tk.PhotoImage(file=r'image\up_button.png').subsample(21, 21)
down_button_image = tk.PhotoImage(file=r'image\down_button.png').subsample(21, 21)
root.life_points = 2
message_dict = {
    'start': 'В «РТСофт» настали трудные времена,\nплатить зарплату стало нечем…\n'
             'На помощь пришел СО, они положили все необходимые\nсредства в этот сейф, но '
             'не сказали точный код от него.\n'
             'Твоя задача по подсказкам вскрыть сейф и\nне оставить бедных сотрудников без гроша!\n'
             'У тебя есть две попытки!',
    'help1': 'Методом перебора подбери одну случайную цифру в коде',
    'help2': 'Теперь подбери две соседних цифры.\nЗнай, что одна из них больше первого числа на два,\n'
             'а вторая - меньше на один',
    'help3': 'Осталась последняя.\nОна равна модулю разности самого большого из\n'
             'подобранных чисел и позиции подбираемой цифры',
    'succes attempt': 'Поздравляю! У тебя получилось!\n'
                      'Отдать деньги в бухгалтерию или\nзабрать себе - решать уже тебе',
    'first unsucces attempt': 'Будь внимательнее! Осталась всего одна попытка!',
    'second unsucces attempt': 'Не получилось, не фартануло!\nОпять остались без зарплаты('
}
up_button_list = []
down_button_list = []
label_list = []
initiate_interface()
root.mainloop()
