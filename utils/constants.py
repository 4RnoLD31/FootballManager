import os
import tkinter as tk

main_window = None


def nothing():
    return f"\033[1m\033[37m[FAILED]\033[0m   \033[37mNothing\033[0m"


def clear(list=None):
    for widget in main_window.winfo_children():
        try:
            if widget["text"] != "FOOTBALL MANAGER" or not isinstance(widget, tk.Menu):
                if list is None:
                    widget.destroy()
                elif widget not in list:
                    widget.destroy()
        except:
            pass


def text_on_center(text, font, window=main_window):
    clear()
    label = tk.Label(window, text=text, font=font, wraplength=1600)
    label.place(x=800 - (label.winfo_reqwidth() / 2), y=400 - (label.winfo_reqheight() / 2))
    return label


game_loaded = False
PL1 = None
PL2 = None
next_player = None
number = None
after_saving = False
working_directory = os.path.abspath(os.curdir).replace("utils", "")
used_in_video = {}
queue = []
version = "0.0.4"
date_of_build = "11/29/2023 2:44 PM"
sum = 0

errorcodes = {0: "Значение превышает 20 символов или равно 0",
              1: "В клубе есть футболист/тренер/менеджер",
              2: "Футболист/тренер мертв/болеет/забастовка",
              3: "Футболист болеет",
              4: "Недостаточно средств",
              5: "Нет доступных клубов",
              6: "Битое сохранение",
              7: "Невозможно загрузить сохранение во время игры",
              8: "Файл configs/database.cfg битый",
              9: "Нет файлов сохранения",
              10: "Неверный путь сохранения"}

gradual_income = [300000, 500000, 1000000, 2000000]

fines = {"Money": 9, "Dead": 2, "Strike": 2, "Coronavirus": 3}
bonuses = {"Money": 9, "Transfer Window": 2, "Vaccine": 2, "Revive": 1, "Charity Match": 1}

money_fines = {3000000: 2, 1500000: 3, 750000: 4}
money_bonuses = {1500000: 2, 1000000: 3, 500000: 4}

clubs = {}
TVs = {}
footballers = {}
coaches = {}
managers = {}

sheikh_level = {}
former_footballer_level = {}
economist_plus_level = {}
economist_minus_level = {}
