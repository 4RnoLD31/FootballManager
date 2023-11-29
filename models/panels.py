import os
import sys
import functools
import tkinter as tk
import models.info as info
import models.property as property
import utils.constants as const
import models.load_game as load_game
import models.statistics as statistics
import models.debug as debug
import models.transfer_window as ts
import models.vaccine as vaccine
import models.revive as revive
import models.charity_match as cm
import models.save_game as save_game
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog


class ChangeName:
    def __init__(self, player):
        self.player = player
        self.window = const.Toplevel()
        self.window.custom_geometry("600x300")
        self.l_name = const.Label(self.window, text=f"Старое имя: {self.player.name}", font="MiSans 25", wraplength=600)
        self.l_name.custom_place(x=300 - (self.l_name.winfo_reqwidth() / 2), y=0)
        self.l_new_name = const.Label(self.window, text="Новое имя", font="MiSans 30")
        self.l_new_name.custom_place(x=30, y=100)
        self.f_new_name = const.Entry(self.window, font="MiSans 30")
        self.f_new_name.custom_place(x=255, y=105, width=300, height=50)
        self.b_new_name = const.Button(self.window, text="Применить", font="MiSans 20", command=lambda: self.__set_name__(self.f_new_name.get()))
        self.b_new_name.custom_place(x=300 - (self.b_new_name.winfo_reqwidth() / 2), y=200)

    def __set_name__(self, name):
        self.name = name
        if self.player == const.PL1:
            const.PL1.name = self.name
        else:
            const.PL2.name = self.name
        panels_initialize()
        self.l_new_name.destroy()
        self.f_new_name.destroy()
        self.b_new_name.destroy()
        self.l_name.configure(text=f"Имя изменено на {self.player.name}", font="MiSans 30")
        self.l_name.custom_place(x=300 - (self.l_name.winfo_reqwidth() / 2), y=150 - (self.l_name.winfo_reqheight() / 2))
        self.window.after(3000, self.window.destroy)


def panels_initialize():
    menu = tk.Menu(const.main_window, tearoff=0)
    file_menu = tk.Menu(const.main_window, tearoff=0)
    change_menu = tk.Menu(const.main_window, tearoff=0)
    statistic_menu = tk.Menu(const.main_window, tearoff=0)
    change_avatar = tk.Menu(const.main_window, tearoff=0)
    change_name = tk.Menu(const.main_window, tearoff=0)
    load_menu = tk.Menu(const.main_window, tearoff=0)
    debug_menu = tk.Menu(const.main_window, tearoff=0)
    property_menu = tk.Menu(const.main_window, tearoff=0)
    objects_menu = tk.Menu(const.main_window, tearoff=0)
    bonus_menu = tk.Menu(const.main_window, tearoff=0)
    sell = tk.Menu(const.main_window, tearoff=0)
    p1_bonus_menu = tk.Menu(const.main_window, tearoff=0)
    p2_bonus_menu = tk.Menu(const.main_window, tearoff=0)
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Изменить", menu=change_menu)
    menu.add_cascade(label="Бонусы", menu=bonus_menu)
    menu.add_cascade(label="Имущество", menu=property_menu)
    menu.add_cascade(label="Статистика", menu=statistic_menu)
    menu.add_cascade(label="Дебаг-Меню", menu=debug_menu)
    const.main_window.configure(menu=menu)
    property_menu.add_cascade(label="Продажа", menu=sell)
    change_menu.add_cascade(label="Поменять имя", menu=change_name)
    debug_menu.add_cascade(label="Все объекты", menu=objects_menu)
    objects_menu.add_command(label="Футболисты", command=lambda: debug.AllObjects("Footballers"))
    objects_menu.add_command(label="Тренеры", command=lambda: debug.AllObjects("Coaches"))
    objects_menu.add_command(label="Менеджеры", command=lambda: debug.AllObjects("Managers"))
    file_menu.add_command(label="Информация о версии", command=lambda: info.Info("Build"))
    file_menu.add_command(label="Сохранить игру в файл", command=pre_save_game)
    file_menu.add_cascade(label="Загрузить игру", menu=load_menu)
    file_menu.add_command(label="Выход", command=sys.exit)
    load_menu.add_command(label="Последнее сохранение", command=lambda: pre_load_game(True))
    load_menu.add_command(label="Выбрать файл сохранения", command=lambda: pre_load_game(False))
    if const.PL1 is not None:
        debug_menu.add_command(label="Изменить баланс", command=debug.ChangeBalance)
        statistic_menu.add_command(label="Баланс", command=statistics.ShowBalance)
        statistic_menu.add_command(label="Основная статистика", command=statistics.Statistics)
        sell.add_command(label=f"Игрок 1 - {const.PL1.name}", command=lambda: property.Sell(const.PL1, None, None, None, None))
        sell.add_command(label=f"Игрок 2 - {const.PL2.name}", command=lambda: property.Sell(const.PL2, None, None, None, None))
        bonus_menu.add_cascade(label=f"Игрок 1 - {const.PL1.name}", menu=p1_bonus_menu)
        bonus_menu.add_cascade(label=f"Игрок 2 - {const.PL2.name}", menu=p2_bonus_menu)
        for element in const.PL1.bonuses:
            if element == "Transfer Window":
                if const.PL1.bonuses[element] != 0:
                    p1_bonus_menu.add_command(label=f"Трансферное окно ({const.PL1.bonuses[element]})", command=lambda: f_transfer_window(const.PL1))
                else:
                    p1_bonus_menu.add_command(label=f"Трансферное окно ({const.PL1.bonuses[element]})")
            elif element == "Vaccine":
                if const.PL1.bonuses[element] != 0:
                    p1_bonus_menu.add_command(label=f"Вакцина ({const.PL1.bonuses[element]})", command=lambda: f_vaccine(const.PL1))
                else:
                    p1_bonus_menu.add_command(label=f"Вакцина ({const.PL1.bonuses[element]})")
            elif element == "Revive":
                if const.PL1.bonuses[element] != 0:
                    p1_bonus_menu.add_command(label=f"Воскрешение ({const.PL1.bonuses[element]})", command=lambda: f_revive(const.PL1))
                else:
                    p1_bonus_menu.add_command(label=f"Воскрешение ({const.PL1.bonuses[element]})")
            elif element == "Charity Match":
                if const.PL1.bonuses[element] != 0:
                    p1_bonus_menu.add_command(label=f"Благотворительный матч ({const.PL1.bonuses[element]})", command=lambda: f_charity_match(const.PL1))
                else:
                    p1_bonus_menu.add_command(label=f"Благотворительный матч ({const.PL1.bonuses[element]})")
        for element in const.PL2.bonuses:
            if element == "Transfer Window":
                if const.PL2.bonuses[element] != 0:
                    p2_bonus_menu.add_command(label=f"Трансферное окно ({const.PL2.bonuses[element]})", command=lambda: f_transfer_window(const.PL2))
                else:
                    p2_bonus_menu.add_command(label=f"Трансферное окно ({const.PL2.bonuses[element]})")
            elif element == "Vaccine":
                if const.PL2.bonuses[element] != 0:
                    p2_bonus_menu.add_command(label=f"Вакцина ({const.PL2.bonuses[element]})", command=lambda: f_vaccine(const.PL2))
                else:
                    p2_bonus_menu.add_command(label=f"Вакцина ({const.PL2.bonuses[element]})")
            elif element == "Revive":
                if const.PL2.bonuses[element] != 0:
                    p2_bonus_menu.add_command(label=f"Воскрешение ({const.PL2.bonuses[element]})", command=lambda: f_revive(const.PL2))
                else:
                    p2_bonus_menu.add_command(label=f"Воскрешение ({const.PL2.bonuses[element]})")
            elif element == "Charity Match":
                if const.PL2.bonuses[element] != 0:
                    p2_bonus_menu.add_command(label=f"Благотворительный матч ({const.PL2.bonuses[element]})", command=lambda: f_charity_match(const.PL2))
                else:
                    p2_bonus_menu.add_command(label=f"Благотворительный матч ({const.PL2.bonuses[element]})")
        change_name.add_command(label=f"Игрок 1 - {const.PL1.name}", command=lambda: ChangeName(const.PL1))
        change_name.add_command(label=f"Игрок 2 - {const.PL2.name}", command=lambda: ChangeName(const.PL2))


def f_transfer_window(player):
    const.queue.append(functools.partial(ts.TransferWindow, player, True, True))
    tk.messagebox.showinfo(title="Очередь", message="Задание трансферное окно добавлено в очередь")


def f_vaccine(player):
    const.queue.append(functools.partial(vaccine.Vaccine, player))
    tk.messagebox.showinfo(title="Очередь", message="Задание вакцина добавлено в очередь")


def f_revive(player):
    const.queue.append(functools.partial(revive.Revive, player))
    tk.messagebox.showinfo(title="Очередь", message="Задание возрождение добавлено в очередь")


def f_charity_match(player):
    const.queue.append(functools.partial(cm.CharityMatch, player))
    tk.messagebox.showinfo(title="Очередь", message="Задание благотворительный матч добавлено в очередь")


def pre_save_game():
    if const.PL1 is None:
        return
    const.queue.insert(0, functools.partial(save_game.save_game, False))
    tk.messagebox.showinfo(title="Очередь", message="Задание сохранение игры добавлено в очередь")


def pre_load_game(bool):
    load_game.LoadGame(bool)
    panels_initialize()
