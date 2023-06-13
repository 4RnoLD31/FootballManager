import utils.constants
from utils.constants import *
from tkinter import messagebox


class LEnough:
    def __init__(self):
        self.frame = Toplevel()
        self.frame.geometry("360x60+780+940")
        self.frame.title("НЕДОСТАТОЧНО")
        self.frame.resizable(width=False, height=False)
        self.l_enough = Label(self.frame, font="MiSans 40")
        self.frame.protocol("WM_DELETE_WINDOW", self.__close__)
        self.switch_off()

    def switch_on(self):
        self.frame.geometry("300x60+810+940")
        self.frame.title("ДОСТАТОЧНО")
        self.l_enough.configure(text="Достаточно", bg="green")
        self.l_enough.pack()

    def switch_off(self):
        self.frame.geometry("360x60+780+940")
        self.frame.title("НЕДОСТАТОЧНО")
        self.l_enough.configure(text="Недостаточно", bg="red")
        self.l_enough.pack()

    def __close__(self):
        pass


class SearchManagers:
    def __init__(self, player, on_the_transfer_market, need_money, l_enough):
        self.on_the_transfer_market = on_the_transfer_market
        self.player = player
        self.need_money = need_money
        self.l_enough = l_enough
        utils.constants.property_window["Manager"] = Toplevel()
        self.frame = utils.constants.property_window["Manager"]
        self.frame.geometry("300x900+810+30")
        self.frame.resizable(width=False, height=False)
        self.frame.title("Менеджеры игрока " + self.player.name)
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        self.l_logo = Label(self.frame, text="Менеджеры", font="MiSans 30")
        self.l_logo.pack(side="top")
        self.found = self.player.search_managers_in_clubs()
        if not self.found:
            self.l_nothing = Label(self.frame, text="Пусто", font="MiSans 50")
            self.l_nothing.place(x=150 - (self.l_nothing.winfo_reqwidth() / 2),
                                 y=400 - (self.l_nothing.winfo_reqheight() / 2))
            print("Нет Менеджеров")
            return
        self.b_sell = Button(self.frame, text="Продать", font="MiSans 40", command=self.sell)
        self.b_sell.place(x=150 - (self.b_sell.winfo_reqwidth() / 2), y=800, height=80)
        self.x = 10
        self.y = 70
        self.will_sell = []
        self.picked = []
        self.check_buttons = []
        for element in range(0, len(self.found)):
            self.picked.append(BooleanVar())
        for element in range(0, len(self.found)):
            print(self.picked)
            self.check_buttons.append(
                Checkbutton(self.frame, variable=self.picked[element], text=self.found[element].name,
                            font="MiSans 14"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.y += 35
        self.frame.mainloop()

    def sell(self):
        self.available = self.will_sell
        if not self.will_sell: return
        self.y = 70
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.frame, text="Менеджеры", font="MiSans 30")
        self.l_logo.pack(side="top")
        for element in self.will_sell:
            self.price_sold = element.sell(self.on_the_transfer_market)
            self.l_sold_first = Label(self.frame, text=element.name, font="MiSans 15")
            self.l_sold_first.place(x=150 - (self.l_sold_first.winfo_reqwidth() / 2), y=self.y)
            self.y += 40
            self.l_sold = Label(self.frame, text="Продан за " + str(self.price_sold), font="MiSans 20")
            utils.constants.sum -= self.price_sold
            self.l_sold.place(x=150 - (self.l_sold.winfo_reqwidth() / 2), y=self.y)
            self.y += 50
        self.frame.after(3000, self.__reinitialization__)

    def __reinitialization__(self):
        utils.constants.property_window["Manager"].destroy()
        utils.constants.property_window["Manager"] = 0
        self.__init__(self.player, self.on_the_transfer_market, self.need_money, self.l_enough)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked[element].get() is True and self.found[element] not in self.will_sell:
                if self.found[element].dead is not False or self.found[element].flu is not False:
                    self.found[element].sell(self.on_the_transfer_market)
                    self.picked[element].set(False)
                else:
                    self.will_sell.append(self.found[element])
                    utils.constants.sum += self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
        for element in range(0, len(self.found)):
            if self.picked[element].get() is False and self.found[element] in self.will_sell:
                utils.constants.sum -= self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
                self.will_sell.remove(self.found[element])
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        # messagebox.showinfo(message=str(self.will_sell))

    def delete(self):
        self.frame.destroy()


class SearchCoaches:
    def __init__(self, players, on_the_transfer_market, need_money, l_enough):
        self.on_the_transfer_market = on_the_transfer_market
        self.player = players
        self.need_money = need_money
        self.l_enough = l_enough
        utils.constants.property_window["Coach"] = Toplevel()
        self.frame = utils.constants.property_window["Coach"]
        self.frame.geometry("300x900+1140+30")
        self.frame.resizable(width=False, height=False)
        self.frame.title("Тренеры игрока " + self.player.name)
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        self.l_logo = Label(self.frame, text="Тренеры", font="MiSans 30")
        self.l_logo.pack(side="top")
        self.found = self.player.search_coaches_in_clubs()
        if not self.found:
            self.l_nothing = Label(self.frame, text="Пусто", font="MiSans 50")
            self.l_nothing.place(x=150 - (self.l_nothing.winfo_reqwidth() / 2),
                                 y=400 - (self.l_nothing.winfo_reqheight() / 2))
            print("Нет тренеров")
            return
        self.b_sell = Button(self.frame, text="Продать", font="MiSans 40", command=self.sell)
        self.b_sell.place(x=150 - (self.b_sell.winfo_reqwidth() / 2), y=800, height=80)
        self.x = 10
        self.y = 70
        self.will_sell = []
        self.picked = []
        self.check_buttons = []
        for element in range(0, len(self.found)):
            self.picked.append(BooleanVar())
        for element in range(0, len(self.found)):
            print(self.picked)
            self.check_buttons.append(
                Checkbutton(self.frame, variable=self.picked[element], text=self.found[element].name,
                            font="MiSans 30"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.y += 50
        self.frame.mainloop()

    def sell(self):
        self.available = self.will_sell
        if not self.will_sell: return
        self.y = 70
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.frame, text="Тренеры", font="MiSans 40")
        self.l_logo.pack(side="top")
        for element in self.will_sell:
            self.price_sold = element.sell(self.on_the_transfer_market)
            self.l_sold_first = Label(self.frame, text=element.name, font="MiSans 40")
            self.l_sold_first.place(x=150 - (self.l_sold_first.winfo_reqwidth() / 2), y=self.y)
            self.y += 70
            self.l_sold = Label(self.frame, text="Продан за " + str(self.price_sold), font="MiSans 20")
            utils.constants.sum -= self.price_sold
            self.l_sold.place(x=150 - (self.l_sold.winfo_reqwidth() / 2), y=self.y)
            self.y += 55
        self.frame.after(3000, self.__reinitialization__)

    def __reinitialization__(self):
        utils.constants.property_window["Coach"].destroy()
        utils.constants.property_window["Coach"] = 0
        self.__init__(self.player, self.on_the_transfer_market, self.need_money, self.l_enough)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked[element].get() is True and self.found[element] not in self.will_sell:
                if self.found[element].strike is not False or self.found[element].flu is not False:
                    self.found[element].sell(self.on_the_transfer_market)
                    self.picked[element].set(False)
                else:
                    self.will_sell.append(self.found[element])
                    utils.constants.sum += self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
        for element in range(0, len(self.found)):
            if self.picked[element].get() is False and self.found[element] in self.will_sell:
                utils.constants.sum -= self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
                self.will_sell.remove(self.found[element])
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        # messagebox.showinfo(message=str(self.will_sell))

    def delete(self):
        self.frame.destroy()


class SearchFootballers:
    def __init__(self, player, on_the_transfer_market, need_money, l_enough):
        self.on_the_transfer_market = on_the_transfer_market
        self.player = player
        self.need_money = need_money
        self.l_enough = l_enough
        utils.constants.property_window["Footballer"] = Toplevel()
        self.frame = utils.constants.property_window["Footballer"]
        self.frame.geometry("300x900+1470+30")
        self.frame.resizable(width=False, height=False)
        self.frame.title("Футболисты игрока " + self.player.name)
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        self.l_logo = Label(self.frame, text="Футболисты", font="MiSans 30")
        self.l_logo.pack(side="top")
        self.found = self.player.search_footballers_in_clubs()
        if not self.found:
            self.l_nothing = Label(self.frame, text="Пусто", font="MiSans 50")
            self.l_nothing.place(x=150 - (self.l_nothing.winfo_reqwidth() / 2),
                                 y=400 - (self.l_nothing.winfo_reqheight() / 2))
            print("Нет клубов")
            return
        self.b_sell = Button(self.frame, text="Продать", font="MiSans 40", command=self.sell)
        self.b_sell.place(x=150 - (self.b_sell.winfo_reqwidth() / 2), y=800, height=80)
        self.x = 10
        self.y = 70
        self.will_sell = []
        self.picked = []
        self.check_buttons = []
        for element in range(0, len(self.found)):
            self.picked.append(BooleanVar())
        for element in range(0, len(self.found)):
            print(self.picked)
            self.check_buttons.append(
                Checkbutton(self.frame, variable=self.picked[element], text=self.found[element].name,
                            font="MiSans 30"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.y += 50
        self.frame.mainloop()

    def sell(self):
        self.available = self.will_sell
        if not self.will_sell: return
        self.y = 70
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.frame, text="Футболисты", font="MiSans 30")
        self.l_logo.pack(side="top")
        for element in self.will_sell:
            self.price_sold = element.sell(self.on_the_transfer_market)
            self.l_sold_first = Label(self.frame, text=element.name, font="MiSans 40")
            self.l_sold_first.place(x=150 - (self.l_sold_first.winfo_reqwidth() / 2), y=self.y)
            self.y += 70
            self.l_sold = Label(self.frame, text="Продан за " + str(self.price_sold), font="MiSans 20")
            utils.constants.sum -= self.price_sold
            self.l_sold.place(x=150 - (self.l_sold.winfo_reqwidth() / 2), y=self.y)
            self.y += 55
        self.frame.after(3000, self.__reinitialization__)

    def __reinitialization__(self):
        utils.constants.property_window["Footballer"].destroy()
        utils.constants.property_window["Footballer"] = 0
        self.__init__(self.player, self.on_the_transfer_market, self.need_money, self.l_enough)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked[element].get() is True and self.found[element] not in self.will_sell:
                if self.found[element].dead is not False or self.found[element].flu is not False:
                    self.found[element].sell(self.on_the_transfer_market)
                    self.picked[element].set(False)
                else:
                    self.will_sell.append(self.found[element])
                    utils.constants.sum += self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
        for element in range(0, len(self.found)):
            if self.picked[element].get() is False and self.found[element] in self.will_sell:
                utils.constants.sum -= self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
                self.will_sell.remove(self.found[element])
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        # messagebox.showinfo(message=str(self.will_sell))

    def delete(self):
        self.frame.destroy()


class SearchClubs:
    def __init__(self, player, on_the_transfer_market, need_money, l_enough):
        self.on_the_transfer_market = on_the_transfer_market
        self.player = player
        self.need_money = need_money
        self.l_enough = l_enough
        utils.constants.property_window["Club"] = Toplevel()
        self.frame = utils.constants.property_window["Club"]
        self.frame.geometry("300x900+150+30")
        self.frame.resizable(width=False, height=False)
        self.frame.title("Клубы игрока " + self.player.name)
        self.canvas = Canvas(self.frame, height=400, width=400)
        self.canvas.place(x=-2, y=0)
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        self.l_logo = Label(self.frame, text="Клубы", font="MiSans 40")
        self.l_logo.pack(side="top")
        self.found = self.player.search_owned_clubs()
        if not self.found:
            self.l_nothing = Label(self.frame, text="Пусто", font="MiSans 50")
            self.l_nothing.place(x=150 - (self.l_nothing.winfo_reqwidth() / 2),
                                 y=400 - (self.l_nothing.winfo_reqheight() / 2))
            print("Нет клубов")
            return
        self.b_sell = Button(self.frame, text="Продать", font="MiSans 40", command=self.sell)
        self.b_sell.place(x=150 - (self.b_sell.winfo_reqwidth() / 2), y=800, height=80)
        self.x = 10
        self.y = 70
        self.will_sell = []
        self.picked = []
        self.check_buttons = []
        for element in range(0, len(self.found)):
            self.picked.append(BooleanVar())
        for element in range(0, len(self.found)):
            print(self.picked)
            self.check_buttons.append(
                Checkbutton(self.frame, variable=self.picked[element], text=self.found[element].name,
                            font="MiSans 25"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.img = PhotoImage(file=self.found[element].img_25x25)
            self.image = self.canvas.create_image(15 + self.check_buttons[element].winfo_reqwidth(), self.y + 17, anchor='nw', image=self.img)
            self.y += 45
        self.frame.mainloop()

    def sell(self):
        self.available = self.will_sell
        if not self.will_sell: return
        self.y = 70
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.frame, text="Клубы", font="MiSans 40")
        self.l_logo.pack(side="top")
        for element in self.will_sell:
            self.price_sold = element.sell(None, self.on_the_transfer_market)
            self.l_sold_first = Label(self.frame, text=element.name, font="MiSans 40")
            self.l_sold_first.place(x=150 - (self.l_sold_first.winfo_reqwidth() / 2), y=self.y)
            self.y += 70
            self.l_sold = Label(self.frame, text="Продан за " + str(self.price_sold), font="MiSans 20")
            utils.constants.sum -= self.price_sold
            self.l_sold.place(x=150 - (self.l_sold.winfo_reqwidth() / 2), y=self.y)
            self.y += 55
        self.frame.after(3000, self.__reinitialization__)

    def __reinitialization__(self):
        utils.constants.property_window["Club"].destroy()
        utils.constants.property_window["Club"] = 0
        self.__init__(self.player, self.on_the_transfer_market, self.need_money, self.l_enough)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked[element].get() is True and self.found[element] not in self.will_sell:
                if self.found[element].footballer is not None or self.found[element].coach is not None or self.found[
                    element].manager is not None:
                    print(1)
                    self.found[element].sell(None, self.on_the_transfer_market)
                    self.picked[element].set(False)
                else:
                    self.will_sell.append(self.found[element])
                    utils.constants.sum += self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
        for element in range(0, len(self.found)):
            if self.picked[element].get() is False and self.found[element] in self.will_sell:
                utils.constants.sum -= self.player.check_balance(
                    self.found[element].price, type="Plus") // self.on_the_transfer_market
                self.will_sell.remove(self.found[element])
        print(utils.constants.sum)
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        # messagebox.showinfo(message=str(self.will_sell))

    def delete(self):
        self.frame.destroy()


class SearchTVs:
    def __init__(self, player, need_money, l_enough):
        self.player = player
        self.need_money = need_money
        self.l_enough = l_enough
        utils.constants.property_window["TV"] = Toplevel()
        self.frame = utils.constants.property_window["TV"]
        self.frame.geometry("300x900+480+30")
        self.frame.resizable(width=False, height=False)
        self.frame.title("ТВ-Компании игрока " + self.player.name)
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        self.l_logo = Label(self.frame, text="ТВ-Компании", font="MiSans 29")
        self.l_logo.pack(side="top")
        self.found = self.player.search_owned_TVs()
        if not self.found:
            self.l_nothing = Label(self.frame, text="Пусто", font="MiSans 50")
            self.l_nothing.place(x=150 - (self.l_nothing.winfo_reqwidth() / 2),
                                 y=400 - (self.l_nothing.winfo_reqheight() / 2))
            print("Нет ТВ-Компаний")
            return
        self.b_sell = Button(self.frame, text="Продать", font="MiSans 40", command=self.sell)
        self.b_sell.place(x=150 - (self.b_sell.winfo_reqwidth() / 2), y=800, height=80)
        self.x = 10
        self.y = 70
        self.will_sell = []
        self.picked = []
        self.check_buttons = []
        for element in range(0, len(self.found)):
            self.picked.append(BooleanVar())
        for element in range(0, len(self.found)):
            print(self.picked)
            self.check_buttons.append(
                Checkbutton(self.frame, variable=self.picked[element], text=self.found[element].name,
                            font="MiSans 20"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.y += 50
        self.frame.mainloop()

    def sell(self):
        self.available = self.will_sell
        if not self.will_sell: return
        self.y = 70
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.frame, text="ТВ-Компании", font="MiSans 29")
        self.l_logo.pack(side="top")
        for element in self.will_sell:
            self.price_sold = element.sell()
            self.l_sold_first = Label(self.frame, text=element.name, font="MiSans 30")
            self.l_sold_first.place(x=150 - (self.l_sold_first.winfo_reqwidth() / 2), y=self.y)
            self.y += 65
            self.l_sold = Label(self.frame, text="Продана за " + str(self.price_sold), font="MiSans 20")
            utils.constants.sum -= self.price_sold
            self.l_sold.place(x=150 - (self.l_sold.winfo_reqwidth() / 2), y=self.y)
            self.y += 55
        self.frame.after(3000, self.__reinitialization__)

    def __reinitialization__(self):
        utils.constants.property_window["TV"].destroy()
        utils.constants.property_window["TV"] = 0
        self.__init__(self.player, self.need_money, self.l_enough)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked[element].get() is True and self.found[element] not in self.will_sell:
                self.will_sell.append(self.found[element])
                utils.constants.sum += self.player.check_balance(
                    self.found[element].price, type="Plus") // 2
        for element in range(0, len(self.found)):
            if self.picked[element].get() is False and self.found[element] in self.will_sell:
                utils.constants.sum -= self.player.check_balance(
                    self.found[element].price, type="Plus") // 2
                self.will_sell.remove(self.found[element])
        if self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        else:
            self.l_enough.switch_off()
        # messagebox.showinfo(message=str(self.will_sell))

    def delete(self):
        self.frame.destroy()


class Property:
    def __init__(self, player, full_screen, on_the_transfer_market, need_money, next_step):
        self.on_the_transfer_market = on_the_transfer_market
        self.full_screen = full_screen
        self.player = player
        self.need_money = need_money
        self.next_step = next_step
        utils.constants.sum = 0
        if full_screen is True:
            clear()
            self.window = utils.constants.main_window
            self.y = 170
        else:
            self.y = 80
            utils.constants.property_window["Start"] = Toplevel()
            self.window = utils.constants.property_window["Start"]
            self.window.geometry("1600x200+160+0")
            self.window.protocol("WM_DELETE_WINDOW", self.__close__)
            self.window.resizable(width=False, height=False)
            self.l_logo = Label(self.window, text="FOOTBALL MANAGER", font="MiSans 50")
        if self.on_the_transfer_market == 1:
            self.window.title(
                "FOOTBALL MANAGER | Продажа имущества игрока " + self.player.name + " во время трансферного окна")
            self.l_logo = Label(self.window,
                                text="Продажа имущества игрока " + self.player.name + " во время трансферного окна",
                                font="MiSans 35")
        else:
            if self.on_the_transfer_market == 1:
                self.window.title(
                    "FOOTBALL MANAGER | Продажа имущества игрока " + self.player.name)
                self.l_logo = Label(self.window,
                                    text="Продажа имущества игрока " + self.player.name,
                                    font="MiSans 50")
        self.l_logo.pack(side="top")
        self.l_enough = LEnough()
        self.buttons = []
        self.names = {"Клубы": 50, "Телекомпании": 250, "Менеджеры": 635, "Тренеры": 972, "Футболисты": 1230}
        self.index = 0
        for element in self.names.keys():
            self.buttons.append(Button(self.window, text=element, font="MiSans 35"))
            self.buttons[self.index].place(x=self.names[element], y=self.y)
            self.index += 1
        self.buttons[0].configure(
            command=lambda: SearchClubs(self.player, self.on_the_transfer_market, self.need_money,
                                        self.l_enough))
        self.buttons[1].configure(command=lambda: SearchTVs(self.player, self.need_money, self.l_enough))
        self.buttons[2].configure(
            command=lambda: SearchManagers(self.player, self.on_the_transfer_market, self.need_money,
                                           self.l_enough))
        self.buttons[3].configure(
            command=lambda: SearchCoaches(self.player, self.on_the_transfer_market, self.need_money,
                                          self.l_enough))
        self.buttons[4].configure(
            command=lambda: SearchFootballers(self.player, self.on_the_transfer_market, self.need_money,
                                              self.l_enough))
        if self.full_screen is False: self.window.mainloop()

    def __close__(self):
        if self.player.balance < self.need_money:
            messagebox.showerror(title="Нужно еще " + str(self.need_money - self.player.balance),
                                 message="Проданного имущества не хватает! Нужно продать еще на " + str(
                                     self.need_money - self.player.balance))
            return
        self.l_enough.frame.destroy()
        for element in utils.constants.property_window.values():
            try:
                element.destroy()
            except:
                pass
        utils.constants.property_window = {"Start": None, "TV": None, "Club": None, "Coach": None, "Footballer": None, "Manager": None}
        main_window.after(1000, self.next_step())
