from tkinter import *
from tkinter import messagebox
import os
main_window = Tk()


def nothing():
    print("Nothing")


def clear():
    for widget in main_window.winfo_children():
        widget.destroy()
    l_logo = Label(main_window, text="FOOTBALL MANAGER", font="MiSans 50")
    l_logo.pack(side="top")


def text_on_center(text, font, window=main_window):
    clear()
    label = Label(window, text=text, font=font)
    label.place(x=800 - (label.winfo_reqwidth() / 2), y=400 - (label.winfo_reqheight() / 2))
    return label


PL1 = None
PL2 = None
next_player = None
working_directory = os.path.abspath(os.curdir).replace("utils", "")
print(working_directory)
property_window = {"Start": 0, "TV": 0, "Club": 0, "Coach": 0, "Footballer": 0, "Manager": 0}
statistics_window = 0
statistics_club_window = 0
statistics_club_canvas = 0
personal_y = 0
plus_basic = None
plus_personal = None
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
                "#0060ff", "#0060ff", "#0060ff",
                "#0060ff", "#0060ff", "#0060ff",
                "#0060ff", "#0060ff", "#0060ff"]

name_TV = ["Setanta Sports", "Euro Sports", "Rai Uno", "ESPN"]
gradual_income = [300000, 500000, 1000000, 2000000]

fines = {"Money": 9, "Dead": 2, "Strike": 2, "Coronavirus": 3}

money_fines = {3000000: 2, 1500000: 3, 750000: 4}
money_fines_chances = [2, 3, 4]

pp_footballers = {2: 1000000, 4: 2000000, 6: 4000000, 8: 6500000, 10: 10000000}
name_footballers = {"Cristiano Ronaldo": 10, "Messi": 4}

pp_coaches = {1: 1000000, 2: 2200000, 3: 4000000}
name_coaches = {"Tedesko": 1, "Malorian": 1}

managers_price = 1000000
managers_count = 10
clubs = {}
TVs = {}
footballers = {}
coaches = {}
managers = {}

nt_managers = {"Мансура бен Заида": "Sheikh", "Фрэнк Лэмпард": "Former Footballer",
               "Пол Кругман": "Economist"}
sheikh_level = {1: 1000000, 2: 2500000, 3: 5000000}
former_footballer_level = {1: 1, 2: 2, 3: 3}
economist_plus_level = {1: 0.1, 2: 0.2, 3: 0.4}
economist_minus_level = {1: 0.15, 2: 0.3, 3: 0.6}
