import threading
import time
import tkinter as tk
import utils.constants as const


class Statistics:
    def __init__(self):
        self.element_statistic = ["Бросков сделано: ", "Сумма выбитых чисел: "]
        self.element_fonts = ["MiSans 30", "MiSans 25"]
        self.element_y = [125, 175]
        self.element_values_pl1 = [const.PL1.throws, const.PL1.numbers_thrown]
        self.element_values_pl2 = [const.PL2.throws, const.PL2.numbers_thrown]
        self.window = const.Toplevel()
        self.window.custom_geometry("900x900+510+70")
        self.window.resizable(width=False, height=False)
        self.window.title("FOOTBALL MANAGER | Статистика")
        self.canvas = const.Canvas(self.window, width=100, height=900)
        self.canvas.pack()
        self.canvas.create_line(50, 0, 50, 900, width=5)
        self.l_logo = const.Label(self.window, text="Статистика", font="MiSans 40")
        self.l_logo.custom_place(x=450 - (self.l_logo.winfo_reqwidth() / 2), y=1)
        self.__reshow__()

    def __reshow__(self):
        self.element_values_pl1 = [const.PL1.throws, const.PL1.numbers_thrown]
        self.element_values_pl2 = [const.PL2.throws, const.PL2.numbers_thrown]
        self.l_name_pl1 = const.Label(self.window, text=const.PL1.name, font="MiSans 40")
        self.l_name_pl1.custom_place(x=(450 - self.l_name_pl1.winfo_reqwidth()) / 2, y=60)
        self.l_name_pl2 = const.Label(self.window, text=const.PL2.name, font="MiSans 40")
        self.l_name_pl2.custom_place(x=(450 - self.l_name_pl2.winfo_reqwidth()) / 2 + 450, y=60)
        self.y = 150
        for element in range(0, len(self.element_statistic)):
            self.l_pl1 = const.Label(self.window, text=f"{self.element_statistic[element]} {self.element_values_pl1[element]}", font=self.element_fonts[element])
            self.l_pl1.custom_place(x=(450 - self.l_pl1.winfo_reqwidth()) / 2, y=self.element_y[element])
            self.l_pl2 = const.Label(self.window, text=f"{self.element_statistic[element]} {self.element_values_pl2[element]}", font=self.element_fonts[element])
            self.l_pl2.custom_place(x=(450 - self.l_pl2.winfo_reqwidth()) / 2 + 450, y=self.element_y[element])

    def __thread__(self):
        self.refresh_bool = True
        self.refresh = threading.Thread(target=self.__update__, daemon=True)
        self.refresh.start()

    def __update__(self):
        while self.refresh_bool:
            self.__reshow__()
            self.window.after(2000, const.nothing)


class ShowBalance:
    def __init__(self):
        self.window = const.Toplevel()
        self.window.custom_geometry("250x150+0+0")
        self.window.protocol("WM_DELETE_WINDOW", self.__destroy__)
        self.window.lift()
        try:
            self.p1 = const.Label(self.window, text=const.PL1.name, font="MiSans 20")
            self.p1.custom_place(x=125 - (self.p1.winfo_reqwidth() / 2), y=0)
            self.first_balance = const.Label(self.window, text=const.PL1.balance, font="MiSans 20")
            self.first_balance.custom_place(x=125 - (self.first_balance.winfo_reqwidth() / 2), y=35)
            self.p2 = const.Label(self.window, text=const.PL2.name, font="MiSans 20")
            self.p2.custom_place(x=125 - (self.p2.winfo_reqwidth() / 2), y=80)
            self.second_balance = const.Label(self.window, text=const.PL2.balance, font="MiSans 20")
            self.second_balance.custom_place(x=125 - (self.second_balance.winfo_reqwidth() / 2), y=115)
        except:
            self.window.destroy()
            return
        self.refresh = True
        threading.Thread(target=self.__update__, daemon=True).start()

    def __reshow__(self):
        try:
            self.first_balance.configure(text=const.PL1.balance)
            self.second_balance.configure(text=const.PL2.balance)
            self.first_balance.custom_place(x=125 - (self.first_balance.winfo_reqwidth() / 2), y=35)
            self.second_balance.custom_place(x=125 - (self.second_balance.winfo_reqwidth() / 2), y=115)
            self.window.lift()
        except:
            pass

    def __update__(self):
        while self.refresh:
            self.__reshow__()
            time.sleep(1)

    def __destroy__(self):
        self.window.destroy()
        self.refresh = False
