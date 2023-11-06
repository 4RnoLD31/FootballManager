from tkinter import *
import os

main_window = None


def nothing():
    return f"\033[1m\033[37m[FAILED]\033[0m   \033[37mNothing\033[0m"


def clear():
    for widget in main_window.winfo_children():
        try:
            if widget["text"] != "FOOTBALL MANAGER" or not isinstance(widget, Menu):
                widget.destroy()
        except:
            pass


def text_on_center(text, font, window=main_window):
    clear()
    label = Label(window, text=text, font=font)
    label.place(x=800 - (label.winfo_reqwidth() / 2), y=400 - (label.winfo_reqheight() / 2))
    return label


game_loaded = False
PL1 = None
PL2 = None
next_player = None
working_directory = os.path.abspath(os.curdir).replace("utils", "")
path_to_settings = f"{working_directory}\\settings.ini"
property_window = {"Start": None, "TV": None, "Club": None, "Coach": None, "Footballer": None, "Manager": None}
used_in_video = {}
main_window = None
sum = 0

errorcodes = {0: "Значение превышает 20 символов или равно 0",
              1: "В клубе есть футболист/тренер/менеджер",
              2: "Футболист/тренер мертв/болеет/забастовка",
              3: "Футболист болеет",
              4: "Недостаточно средств",
              5: "Нет доступных клубов"}

gradual_income = [300000, 500000, 1000000, 2000000]

fines = {"Money": 9, "Dead": 2, "Strike": 2, "Coronavirus": 3}
bonuses = {"Money": 9, "Transfer Window": 2, "Vaccine": 2, "Revive": 1, "Charity Match": 1}

money_fines = {3000000: 2, 1500000: 3, 750000: 4}
money_bonuses = {1500000: 2, 1000000: 3, 500000: 4}

managers_price = 1000000
managers_count = 10
clubs = {}
TVs = {}
footballers = {}
coaches = {}
managers = {}

sheikh_level = former_footballer_level = economist_plus_level = economist_minus_level = {}
