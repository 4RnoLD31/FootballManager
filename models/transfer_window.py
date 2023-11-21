import tkinter as tk
import utils.constants as const
import models.property as property
import models.field as field
import models.panels as panels


class TransferWindow:
    def __init__(self, player, bonus=False, queue=False):
        self.bonus = bonus
        self.player = player
        self.queue = queue
        self.player.bonuses["Transfer Window"] -= 1
        self.first_player = self.player
        self.first_time = True
        if self.bonus:
            const.text_on_center(f"Специальное трансферное окно для игрока {self.player.name}", "MiSans 40")
        else:
            const.text_on_center(f"Игрок {self.player.name} наступил на трансферное окно", "MiSans 40")
        const.main_window.after(4000, self.__main__)

    def __back__(self):
        self.first_time = True
        self.__main__()

    def __main__(self):
        const.clear()
        self.l_title = tk.Label(const.main_window, text=f"Что вы хотите сделать, {self.player.name}?", font="MiSans 50")
        self.l_title.place(x=800 - self.l_title.winfo_reqwidth() / 2, y=0)
        self.b_sell = tk.Button(const.main_window, text="Продать", font="MiSans 40", command=lambda: property.Sell(self.player, self.__back__, True, True))
        self.b_sell.place(x=100, y=170, width=1400, height=100)
        self.b_buy = tk.Button(const.main_window, text="Купить", font="MiSans 40", command=lambda: property.Buy(self.player, self.__back__))
        self.b_buy.place(x=100, y=290, width=1400, height=100)
        self.b_transfer = tk.Button(const.main_window, text="Переместить", font="MiSans 40", command=lambda: property.Transfer(self.player, self.__back__))
        self.b_transfer.place(x=100, y=410, width=1400, height=100)
        self.b_next_step = tk.Button(const.main_window, text="Закончить трансферное окно", font="MiSans 40", command=self.__stop__)
        self.b_next_step.place(x=100, y=410, width=1400, height=100)
        if self.first_time and not self.bonus:
            if self.player == self.first_player:
                self.b_player = tk.Button(const.main_window, text="Следующий игрок", font="MiSans 40", command=self.__next_player__)
            else:
                self.b_player = tk.Button(const.main_window, text="Предыдущий игрок", font="MiSans 40", command=self.__next_player__)
            self.b_player.place(x=100, y=530, width=1400, height=100)

    def __stop__(self):
        if self.queue:
            del const.queue[0]
            panels.panels_initialize()
        field.Field.new_move()
        return

    def __next_player__(self):
        if not self.bonus:
            self.first_time = False
            if self.player == const.PL1:
                self.player = const.PL2
            else:
                self.player = const.PL1
            self.l_title.configure(text=f"Что вы хотите сделать, {self.player.name}?")
            if self.player == self.first_player:
                self.b_player.configure(text="Следующий игрок")
            else:
                self.b_player.configure(text="Предыдущий игрок")

