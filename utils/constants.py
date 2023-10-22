from tkinter import *
from tkinter import messagebox
import os

main_window = None


def nothing():
    print("Nothing")


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
path_to_settings = working_directory + "\\settings.ini"
print(path_to_settings)
property_window = {"Start": None, "TV": None, "Club": None, "Coach": None, "Footballer": None, "Manager": None}
used_in_video = {}
main_window = None
sum = 0

errorcodes = {0: "Значение превышает 20 символов или равно 0",
              1: "В клубе есть футболист/тренер/менеджер",
              2: "Футболист/тренер мертв/болеет/забастовка",
              3: "Футболист болеет"}

names_clubs = ["Манчестер Сити", "Арсенал", "Ливерпуль",
               "Барселона", "Реал Мадрид", "Атлетико",
               "Интер", "Милан", "Ювентус",
               "Бавария", "Боруссия", "Лейпциг",
               "Спартак", "ЦСКА", "Краснодар"]
codenames_clubs = ["City", "Arsenal", "Liverpool",
                   "Barca", "Real", "Atletico",
                   "Inter", "Milan", "Juventus",
                   "Bayern", "Borussia", "Leipzig",
                   "Spartak", "CSKA", "Krasnodar"]
leagues_clubs = ["АПЛ", "АПЛ", "АПЛ",
                 "Ла Лига", "Ла Лига", "Ла Лига",
                 "Серия А", "Серия А", "Серия А",
                 "Бундеслига", "Бундеслига", "Бундеслига",
                 "РПЛ", "РПЛ", "РПЛ"]
prices_clubs = [5000000, 4600000, 4400000,
                4600000, 4500000, 4200000,
                4600000, 4400000, 4000000,
                4400000, 4200000, 3800000,
                3800000, 3700000, 3500000]
colors_clubs = ["#0080ff", "#c1ae67", "#ff0000",
                "#0060ff", "#ffd700", "#0030ff",
                "#0048ff", "#ff0000", "#ffffff",
                "#0080ff", "#fff000", "#ff0000",
                "#ff0000", "#0030ff", "#007a4d"]

name_TV = ["Setanta Sports", "Euro Sports", "Rai Uno", "ESPN"]
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

nt_managers = {"Мансура бен Заида": "Sheikh", "Фрэнк Лэмпард": "Former Footballer",
               "Пол Кругман": "Economist"}
sheikh_level = former_footballer_level = economist_plus_level = economist_minus_level = {}
