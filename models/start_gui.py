from tkinter import *
from time import sleep
from random import randint

import utils.constants
from utils.constants import *
from models.club import *
from models.field import *
from models.club import *
from models.players import *
from models.footballer import *
from models.tv_company import *
from models.manager import Manager
from models.error import Error
from models.property import Property
from models.statistics import Statistics

class StartGame:
    def __init__(self):
        main_window.geometry("1600x800+160+115")
        main_window.resizable(width=False, height=False)
        main_window.title("FOOTBALL MANAGER")
        main_window.protocol("WM_DELETE_WINDOW", lambda: quit(0))
        self.__main_menu__()
        main_window.mainloop()

    def __main_menu__(self):
        clear()
        self.l_PL1 = Label(main_window, text="Имя первого игрока:", font="MiSans 40")
        self.l_PL1.place(x=50, y=250)
        self.f_PL1 = Entry(main_window, font="MiSans 30")
        self.f_PL1.place(x=800, y=265, width=500)
        self.l_PL2 = Label(main_window, text="Имя второго игрока:", font="MiSans 40")
        self.l_PL2.place(x=53, y=350)
        self.f_PL2 = Entry(main_window, font="MiSans 30")
        self.f_PL2.place(x=800, y=362, width=500)
        self.b_start = Button(main_window, text="НАЧАТЬ ИГРУ", font="MiSans 40", command=self.__start_game__)
        self.b_start.place(x=600, y=700, width=400, height=80)

    def __who_first__(self):
        if self.choice == 0:
            self.first = utils.constants.PL1
            self.l_first.config(text="Первым бросает игрок: " + utils.constants.PL1.name)
            utils.constants.next_player = utils.constants.PL2
        else:
            self.first = utils.constants.PL2
            self.l_first.config(text="Первым бросает игрок: " + utils.constants.PL2.name)
            utils.constants.next_player = utils.constants.PL1
        self.l_first.place(x=800 - (self.l_first.winfo_reqwidth() / 2), y=400 - (self.l_first.winfo_reqheight() / 2))
        """Statistics()
        return"""
        main_window.after(2000, lambda: NewMove(self.first))

    def __start_game__(self):
        self.PL1_name = self.f_PL1.get()
        self.PL2_name = self.f_PL2.get()
        if len(self.PL1_name) > 20 or len(self.PL1_name) == 0 or len(self.PL2_name) > 20 or len(self.PL2_name) == 0:
            Error(0)
            self.__main_menu__()
            return
        clear()
        utils.constants.PL1 = Player(self.PL1_name, 36000000, 12121)
        utils.constants.PL2 = Player(self.PL2_name, 10, 12121)
        clubs["Реал Мадрид"].buy(utils.constants.PL1)
        clubs["Барселона"].buy(utils.constants.PL1)
        managers["Пол Кругман"].buy(utils.constants.PL1, clubs["Реал Мадрид"])
        clubs["Атлетико"].buy(utils.constants.PL1)
        TVs["Setanta Sports"].buy(utils.constants.PL1)
        footballers["Messi"].buy(utils.constants.PL1, clubs["Барселона"])
        coaches["Tedesko"].buy(utils.constants.PL1, clubs["Барселона"])
        coaches["Malorian"].buy(utils.constants.PL1, clubs["Барселона"])
        managers["Фрэнк Лэмпард"].buy(utils.constants.PL1, clubs["Барселона"])
        clubs["Атлетико"].info()
        #self.choice = randint(0, 1)
        self.choice = 0
        self.l_first = Label(main_window, text="Первым бросает игрок: ....", font="MiSans 50")
        self.l_first.place(x=800 - (self.l_first.winfo_reqwidth() / 2), y=400 - (self.l_first.winfo_reqheight() / 2))
        main_window.after(2000, self.__who_first__)