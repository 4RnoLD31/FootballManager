from tkinter import *
import utils.constants
from models.property import Sell, Buy, Transfer


class TransferWindow:
    def __init__(self, player, bonus=False):
        self.bonus = bonus
        self.player = player
        self.first_player = self.player
        self.first_time = True
        if self.bonus:
            self.window = Toplevel()
            self.window.resizable(False, False)
            self.window.geometry("1000x800")
        else:
            utils.constants.text_on_center(f"Игрок {self.player.name} наступил на трансферное окно", "MiSans 40")
            utils.constants.main_window.after(4000, self.__main__)

    def __back__(self):
        self.first_time = True
        self.__main__()

    def __main__(self):
        if not self.bonus:
            utils.constants.clear()
            self.l_title = Label(utils.constants.main_window, text=f"Что вы хотите сделать, {self.player.name}?", font="MiSans 50")
            self.l_title.place(x=800 - self.l_title.winfo_reqwidth() / 2, y=0)
            self.b_sell = Button(utils.constants.main_window, text="Продать", font="MiSans 40", command=lambda: Sell(self.player, self.__back__, True, True))
            self.b_sell.place(x=100, y=200, width=1400, height=100)
            self.b_buy = Button(utils.constants.main_window, text="Купить", font="MiSans 40", command=lambda: Buy(self.player, self.__back__))
            self.b_buy.place(x=100, y=320, width=1400, height=100)
            self.b_transfer = Button(utils.constants.main_window, text="Переместить", font="MiSans 40", command=lambda: Transfer(self.player, self.__back__))
            self.b_transfer.place(x=100, y=440, width=1400, height=100)
            if self.first_time:
                if self.player == self.first_player:
                    self.b_player = Button(utils.constants.main_window, text="Следующий игрок", font="MiSans 40", command=self.__next_player__)
                else:
                    self.b_player = Button(utils.constants.main_window, text="Предыдущий игрок", font="MiSans 40", command=self.__next_player__)
                self.b_player.place(x=100, y=560, width=1400, height=100)

    def __next_player__(self):
        self.first_time = False
        if self.player == utils.constants.PL1:
            self.player = utils.constants.PL2
        else:
            self.player = utils.constants.PL1
        self.l_title.configure(text=f"Что вы хотите сделать, {self.player.name}?")
        if self.player == self.first_player:
            self.b_player.configure(text="Следующий игрок")
        else:
            self.b_player.configure(text="Предыдущий игрок")

