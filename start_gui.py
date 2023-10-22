from tkinter import *
from time import sleep
from random import randint
import utils.constants
from utils.constants import *
from models.club import *
from models.field import *
from models.club import *
from models.player import *
from models.footballer import *
from models.tv_company import *
from models.manager import Manager
from models.error import error
from models.info import Info
from models.property import Property
from models.statistics import Statistics, ShowBalance
from models.panels import panels_initialize
from utils.initialize import *
from configparser import ConfigParser


def create_main_window():
    try:
        utils.constants.main_window.destroy()
    except:
        pass
    utils.constants.main_window = Tk()
    utils.constants.main_window.geometry("1600x800+160+115")
    utils.constants.main_window.resizable(width=False, height=False)
    utils.constants.main_window.title("FOOTBALL MANAGER")
    utils.constants.main_window.protocol("WM_DELETE_WINDOW", lambda: quit(0))
    l_logo = Label(utils.constants.main_window, text="FOOTBALL MANAGER", font="MiSans 50")
    l_logo.pack(side="top")
    panels_initialize()
    cascade()
    utils.constants.main_window.mainloop()


def cascade():
    global f_PL1, f_PL2
    l_PL1 = Label(utils.constants.main_window, text="Имя первого игрока:", font="MiSans 40")
    l_PL1.place(x=50, y=250)
    f_PL1 = Entry(utils.constants.main_window, font="MiSans 30")
    f_PL1.place(x=800, y=265, width=500)
    l_PL2 = Label(utils.constants.main_window, text="Имя второго игрока:", font="MiSans 40")
    l_PL2.place(x=53, y=350)
    f_PL2 = Entry(utils.constants.main_window, font="MiSans 30")
    f_PL2.place(x=800, y=362, width=500)
    b_start = Button(utils.constants.main_window, text="НАЧАТЬ ИГРУ", font="MiSans 40", command=process)
    b_start.place(x=600, y=700, width=400, height=80)


def process():
    if not utils.constants.game_loaded:
        PL1_name = f_PL1.get()
        PL2_name = f_PL2.get()
        if len(PL1_name) > 20 or len(PL1_name) == 0 or len(PL2_name) > 20 or len(PL2_name) == 0:
            error(0)
            process()
            return
        clear()
        utils.constants.PL1 = Player(PL1_name, 36000000, 12121)
        utils.constants.PL2 = Player(PL2_name, 10, 12121)
        clubs["Реал Мадрид"].buy(utils.constants.PL1)
        clubs["Барселона"].buy(utils.constants.PL1)
        managers["Пол Кругман"].buy(utils.constants.PL1, clubs["Реал Мадрид"])
        clubs["Атлетико"].buy(utils.constants.PL1)
        TVs["Setanta Sports"].buy(utils.constants.PL1)
        footballers["Лионель Месси"].buy(utils.constants.PL1, clubs["Реал Мадрид"])
        coaches["Тони Моубрэй"].buy(utils.constants.PL1, clubs["Барселона"])
        coaches["Дейв Джонс"].buy(utils.constants.PL1, clubs["Барселона"])
        managers["Фрэнк Лэмпард"].buy(utils.constants.PL1, clubs["Барселона"])
        l_first = Label(utils.constants.main_window, text="Первым бросает игрок: ....", font="MiSans 50")
        l_first.place(x=800 - (l_first.winfo_reqwidth() / 2), y=400 - (l_first.winfo_reqheight() / 2))
        choice = 0
        if choice == 0:
            first = utils.constants.PL1
            l_first.config(text="Первым бросает игрок: " + utils.constants.PL1.name)
            utils.constants.next_player = utils.constants.PL2
        else:
            first = utils.constants.PL2
            l_first.config(text="Первым бросает игрок: " + utils.constants.PL2.name)
            utils.constants.next_player = utils.constants.PL1
        l_first.place(x=800 - (l_first.winfo_reqwidth() / 2), y=400 - (l_first.winfo_reqheight() / 2))
        """Statistics()
        return"""
        utils.constants.main_window.after(2000, lambda: new_move(first))
    panels_initialize()


initialize()
create_main_window()
