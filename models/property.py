import utils.constants
from utils.constants import *
from tkinter import messagebox
from models.error import error
from tkinter import ttk
from models.coach import Coach
from models.footballer import Footballer
from models.manager import Manager


def search_available_footballers(power):
    output = []
    for element in footballers.keys():
        if footballers[element].club is None and footballers[element].dead is False and footballers[element].power == int(power):
            output.append(footballers[element])
    return output


def search_available_coaches(power):
    output = []
    for element in coaches.keys():
        if coaches[element].club is None and coaches[element].dead is False and coaches[element].power == int(power):
            output.append(coaches[element])
    return output


def search_available_managers(type):
    output = []
    for element in managers.keys():
        if managers[element].club is None and managers[element].dead is False and managers[element].type == type:
            output.append(managers[element])
    return output


class LEnough:
    def __init__(self):
        self.window = Toplevel()
        self.window.geometry("360x60+780+940")
        self.window.title("НЕДОСТАТОЧНО")
        self.window.resizable(width=False, height=False)
        self.l_enough = Label(self.window, font="MiSans 40")
        self.window.protocol("WM_DELETE_WINDOW", self.__close__)
        self.switch_off()

    def switch_on(self):
        self.window.geometry("300x60+810+940")
        self.window.title("ДОСТАТОЧНО")
        self.l_enough.configure(text="Достаточно", bg="green")
        self.l_enough.pack()

    def switch_off(self):
        self.window.geometry("360x60+780+940")
        self.window.title("НЕДОСТАТОЧНО")
        self.l_enough.configure(text="Недостаточно", bg="c_failed")
        self.l_enough.pack()

    def __close__(self):
        pass


class Transfer:
    def __init__(self, player, back):
        self.back = back
        self.player = player
        clear()
        self.l_logo = Label(utils.constants.main_window, text=f"Трансфер для игрока {self.player.name}", font="MiSans 40")
        self.l_logo.place(x=800 - self.l_logo.winfo_reqwidth() // 2, y=0)
        self.b_manager = Button(utils.constants.main_window, text="Менеджеры", font="MiSans 35", command=lambda: self.__window__("Manager"))
        self.b_coach = Button(utils.constants.main_window, text="Тренеры", font="MiSans 35", command=lambda: self.__window__("Coach"))
        self.b_footballer = Button(utils.constants.main_window, text="Футболисты", font="MiSans 35", command=lambda: self.__window__("Footballer"))
        self.b_manager.place(x=100, y=170, width=452, height=100)
        self.b_coach.place(x=572, y=170, width=452, height=100)
        self.b_footballer.place(x=1044, y=170, width=452, height=100)
        self.b_back = Button(utils.constants.main_window, text="Назад", font="MiSans 20", command=self.back)
        self.b_back.place(x=20, y=730, height=50)

    def __window__(self, type):
        self.type = type
        self.window = Toplevel()
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)
        self.__menu__()

    def __menu__(self):
        for element in self.window.winfo_children():
            element.destroy()
        self.name_found = []
        if self.type == "Manager":
            self.window.geometry("500x800+160+115")
            self.found = self.player.search_bought_managers()
            self.l_logo = Label(self.window, text="Выберите менеджера для трансфера", font="MiSans 18")
            for element in self.found:
                if element.dead is True or element.flu is not None:
                    self.name_found.append(element)
        elif self.type == "Coach":
            self.window.geometry("500x800+710+115")
            self.found = self.player.search_bought_coaches()
            self.l_logo = Label(self.window, text="Выберите тренера для трансфера", font="MiSans 18")
            for element in self.found:
                if element.dead is True or element.flu is not None or element.strike is not None:
                    self.name_found.append(element)
        elif self.type == "Footballer":
            self.window.geometry("500x800+1260+115")
            self.found = self.player.search_bought_footballers()
            self.l_logo = Label(self.window, text="Выберите футболиста для трансфера", font="MiSans 18")
            for element in self.found:
                if element.dead is True or element.flu is not None:
                    self.name_found.append(element)
        for element in self.name_found:
            self.found.remove(element)
        for element in self.found:
            self.name_found.append(element.name)
        if not self.found:
            self.l_nothing = Label(self.window, text="Ничего не найдено", font="MiSans 40")
            self.l_nothing.place(x=250 - self.l_nothing.winfo_reqwidth() // 2, y=400 - self.l_nothing.winfo_reqheight() // 2)
            self.window.after(3000, self.window.destroy)
            return
        self.l_logo.place(x=250 - self.l_logo.winfo_reqwidth() // 2, y=0)
        self.cb_found = ttk.Combobox(self.window, values=self.name_found, font="MiSans 20", state="readonly")
        self.cb_found.bind("<<ComboboxSelected>>", lambda event, source="found": self.__show__(source))
        self.cb_found.place(x=50, y=640, height=50, width=400)
        self.b_confirm = Button(self.window, text="Подтвердить", font="MiSans 30", command=self.__to__)
        self.b_confirm.place(x=250 - (self.b_confirm.winfo_reqwidth() // 2), y=700)

    def __show__(self, event):
        if event == "found":
            self.picked_item = self.cb_found.get()
            self.__cb_found__()
        elif event == "clubs":
            self.picked_club = self.cb_clubs.get()
            self.__cb_clubs__()

    def __cb_found__(self):
        try:
            self.l_club.destroy()
        except:
            pass
        if self.type == "Manager":
            try:
                self.text = f"Клуб: {managers[self.picked_item].club.name}"
            except:
                self.text = "Клуб: Отсутствует"
        elif self.type == "Coach":
            try:
                self.text = f"Клуб: {coaches[self.picked_item].club.name}"
            except:
                self.text = "Клуб: Отсутствует"
        elif self.type == "Footballer":
            try:
                self.text = f"Клуб: {footballers[self.picked_item].club.name}"
            except:
                self.text = "Клуб: Отсутствует"
        self.l_club = Label(self.window, text=self.text, font="MiSans 20")
        self.l_club.place(x=250 - self.l_club.winfo_reqwidth() // 2, y=590)

    def __cb_clubs__(self):
        try:
            self.l_club.destroy()
        except:
            pass
        if self.type == "Manager":
            try:
                self.text = "Менеджер: " + clubs[self.picked_club].manager.name
            except:
                self.text = "Менеджер: Отсутствует"
        elif self.type == "Coach":
            try:
                self.text = "Тренер: " + clubs[self.picked_club].coach.name
            except:
                self.text = "Тренер: Отсутствует"
        elif self.type == "Footballer":
            try:
                self.text = "Футболист: " + clubs[self.picked_club].footballer.name
            except:
                self.text = "Футболист: Отсутствует"
        self.l_club = Label(self.window, text=self.text, font="MiSans 20")
        self.l_club.place(x=250 - self.l_club.winfo_reqwidth() // 2, y=590)

    def __to__(self):
        try:
            if self.picked_item == "":
                return
        except:
            return
        self.name_clubs = []
        for element in self.window.winfo_children():
            if element != self.l_logo:
                element.destroy()
        if self.type == "Manager":
            self.clubs = self.player.where_can_i_have_a_manager(False)
            for element in self.clubs:
                try:
                    if element.manager.name == self.picked_item:
                        self.name_clubs.append(element)
                except:
                    pass
        elif self.type == "Coach":
            self.clubs = self.player.where_can_i_have_a_coach(False)
            for element in self.clubs:
                try:
                    if element.coach.name == self.picked_item:
                        self.name_clubs.append(element)
                except:
                    pass
        elif self.type == "Footballer":
            self.clubs = self.player.where_can_i_have_a_footballer(False)
            for element in self.clubs:
                try:
                    if element.footballer.name == self.picked_item:
                        self.name_clubs.append(element)
                except:
                    pass
        for element in self.name_clubs:
            self.clubs.remove(element)
        self.name_clubs = []
        for element in self.clubs:
            self.name_clubs.append(element.name)
        if not self.clubs:
            self.l_nothing = Label(self.window, text="Нет доступных клубов", font="MiSans 30")
            self.l_nothing.place(x=250 - self.l_nothing.winfo_reqwidth() // 2, h=400 - self.l_nothing.winfo_reqheight() // 2)
            self.window.after(2000, self.window.destroy)
            return
        self.l_logo.configure(text="Выберите клуб", font="MiSans 30")
        self.l_logo.place(x=250 - self.l_logo.winfo_reqwidth() // 2, y=0)
        self.cb_clubs = ttk.Combobox(self.window, values=self.name_clubs, font="MiSans 20", state="readonly")
        self.cb_clubs.bind("<<ComboboxSelected>>", lambda event, type="clubs": self.__show__(type))
        self.cb_clubs.place(x=50, y=640, height=50, width=400)
        self.b_confirm = Button(self.window, text="Подтвердить", font="MiSans 30", command=self.__are_you_sure__)
        self.b_confirm.place(x=250 - (self.b_confirm.winfo_reqwidth() // 2), y=700)
        self.b_back = Button(self.window, text="Назад", font="MiSans 18", command=self.__menu__)
        self.b_back.place(x=7, y=730, height=50)

    def __are_you_sure__(self):
        self.window.protocol("WM_DELETE_WINDOW", nothing)
        try:
            if self.picked_club == "":
                return
        except:
            return
        for element in self.window.winfo_children():
            if element != self.l_logo:
                element.destroy()
        self.l_logo.configure(text="Вы уверены?")
        self.l_logo.place(x=250 - self.l_logo.winfo_reqwidth() // 2, y=0)
        if self.type == "Manager":
            self.text = "Менеджер " + self.picked_item + " переходит в клуб " + self.picked_club
            if clubs[self.picked_club].manager is not None:
                self.text += " вместо " + clubs[self.picked_club].manager.name
        elif self.type == "Coach":
            self.text = "Тренер " + self.picked_item + " переходит в клуб " + self.picked_club
            if clubs[self.picked_club].coach is not None:
                self.text += " вместо " + clubs[self.picked_club].coach.name
        elif self.type == "Footballer":
            self.text = "Футболист " + self.picked_item + " переходит в клуб " + self.picked_club
            if clubs[self.picked_club].footballer is not None:
                self.text += " вместо " + clubs[self.picked_club].footballer.name
        self.l_text = Label(self.window, text=self.text, font="MiSans 20", wraplength=500)
        self.l_text.place(x=250 - self.l_text.winfo_reqwidth() // 2, y=(400 - self.l_text.winfo_reqheight() // 2) - 50)
        self.b_back = Button(self.window, text="Назад", font="MiSans 20", command=self.__to__)
        self.b_back.place(x=50, y=680, width=190, height=100)
        self.b_confirm = Button(self.window, text="Подтвердить", font="MiSans 20", command=self.__confirm__)
        self.b_confirm.place(x=260, y=680, width=190, height=100)

    def __confirm__(self):
        if self.type == "Manager":
            managers[self.picked_item].transfer(clubs[self.picked_club])
        elif self.type == "Coach":
            coaches[self.picked_item].transfer(clubs[self.picked_club])
        elif self.type == "Footballer":
            footballers[self.picked_item].transfer(clubs[self.picked_club])
        for element in self.window.winfo_children():
            element.destroy()
        self.l_logo = Label(self.window, text="Успешно", font="MiSans 40")
        self.l_logo.place(x=250 - self.l_logo.winfo_reqwidth() // 2, y=400 - self.l_logo.winfo_reqheight() // 2)
        self.window.after(2000, self.window.destroy)


class BuyItems:
    def __init__(self, type, player):
        self.type = type
        self.player = player
        self.window = Toplevel()
        self.window.resizable(width=False, height=False)
        self.__next__()

    def __next__(self):
        try:
            for element in self.window.winfo_children():
                if element != self.l_logo:
                    element.destroy()
        except:
            pass
        if self.type == "Footballer":
            self.window.geometry("500x800+1260+115")
            self.window.title("Покупка футболистов")
            self.l_logo = Label(self.window, text="Выберите уровень футболиста", font="MiSans 25")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
            self.available_clubs = self.player.where_can_i_have_a_footballer()
            if self.available_clubs is None:
                error(5)
                self.window.destroy()
                return
            self.b_10_level = Button(self.window, text="10", font="MiSans 40", command=lambda: self.menu("Footballer", 10))
            self.b_10_level.place(x=20, y=150, width=460, height=80)
            self.b_8_level = Button(self.window, text="8", font="MiSans 40", command=lambda: self.menu("Footballer", 8))
            self.b_8_level.place(x=20, y=250, width=460, height=80)
            self.b_6_level = Button(self.window, text="6", font="MiSans 40", command=lambda: self.menu("Footballer", 6))
            self.b_6_level.place(x=20, y=350, width=460, height=80)
            self.b_4_level = Button(self.window, text="4", font="MiSans 40", command=lambda: self.menu("Footballer", 4))
            self.b_4_level.place(x=20, y=450, width=460, height=80)
            self.b_2_level = Button(self.window, text="2", font="MiSans 40", command=lambda: self.menu("Footballer", 2))
            self.b_2_level.place(x=20, y=550, width=460, height=80)
        elif self.type == "Coach":
            self.window.geometry("500x800+710+115")
            self.window.title("Покупка тренеров")
            self.l_logo = Label(self.window, text="Выберите уровень тренера", font="MiSans 25")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
            self.available_clubs = self.player.where_can_i_have_a_coach()
            if self.available_clubs is None:
                error(5)
                self.window.destroy()
                return
            self.b_3_level = Button(self.window, text="3", font="MiSans 40", command=lambda: self.menu("Coach", 3))
            self.b_3_level.place(x=20, y=150, width=460, height=80)
            self.b_2_level = Button(self.window, text="2", font="MiSans 40", command=lambda: self.menu("Coach", 2))
            self.b_2_level.place(x=20, y=250, width=460, height=80)
            self.b_1_level = Button(self.window, text="1", font="MiSans 40", command=lambda: self.menu("Coach", 1))
            self.b_1_level.place(x=20, y=350, width=460, height=80)
        elif self.type == "Manager":
            self.window.geometry("500x800+160+115")
            self.window.title("Покупка менеджеров")
            self.l_logo = Label(self.window, text="Выберите тип менеджера", font="MiSans 25")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
            self.available_clubs = self.player.where_can_i_have_a_manager()
            if not self.available_clubs:
                error(5)
                self.window.destroy()
                return
            self.b_sheikh = Button(self.window, text="Шейхи", font="MiSans 40", command=lambda: self.menu("Sheikh"))
            self.b_sheikh.place(x=20, y=150, width=460, height=80)
            self.b_former_footballer = Button(self.window, text="Бывшие футболисты", font="MiSans 30", command=lambda: self.menu("Former Footballer"))
            self.b_former_footballer.place(x=20, y=250, width=460, height=80)
            self.b_economist = Button(self.window, text="Экономисты", font="MiSans 40", command=lambda: self.menu("Economist"))
            self.b_economist.place(x=20, y=350, width=460, height=80)
        self.window.mainloop()

    def menu(self, type, power=None):
        if type == "Footballer":
            self.found = search_available_footballers(power)
            self.l_logo = Label(self.window, text="Футболисты " + str(power) + " уровня", font="MiSans 25")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        elif type == "Coach":
            self.found = search_available_coaches(power)
            self.l_logo = Label(self.window, text="Тренеры " + str(power) + " уровня", font="MiSans 25")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        elif type == "Former Footballer":
            self.found = search_available_managers(type)
            self.l_logo = Label(self.window, text="Бывшие футболисты", font="MiSans 30")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        elif type == "Economist":
            self.found = search_available_managers(type)
            self.l_logo = Label(self.window, text="Экономисты", font="MiSans 30")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        elif type == "Sheikh":
            self.found = search_available_managers(type)
            self.l_logo = Label(self.window, text="Шейхи", font="MiSans 30")
            self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        self.y = 55
        self.already_picked_bool = False
        self.picked = None
        self.picked_bool = []
        self.check_buttons = []
        for element in self.window.winfo_children():
            if element != self.l_logo:
                element.destroy()
        self.b_back = Button(self.window, text="Назад", font="MiSans 20", command=self.__next__)
        self.b_back.place(x=20, y=730, height=50)
        for element in range(0, len(self.found)):
            self.picked_bool.append(BooleanVar())
        for element in range(0, len(self.found)):
            self.check_buttons.append(
                Checkbutton(self.window, variable=self.picked_bool[element], text=self.found[element].name,
                            font="MiSans 25"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.y += 50
        self.b_buy = Button(self.window, text="Купить", font="MiSans 40", command=self.buy)
        self.b_buy.place(x=250 - (self.b_buy.winfo_reqwidth() / 2), y=710, height=80)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked_bool[element].get() is True and self.found[element] != self.picked:
                if not self.player.check_withdrawal(self.found[element].price):
                    error(4)
                    self.window.lift()
                    self.picked_bool[element].set(False)
                else:
                    if not self.already_picked_bool:
                        self.already_picked_bool = True
                        self.picked = self.found[element]
                    else:
                        self.picked_bool[element].set(False)
        for element in range(0, len(self.found)):
            if self.picked_bool[element].get() is False and self.found[element] == self.picked:
                if self.already_picked_bool:
                    self.already_picked_bool = False
                self.picked = None

    def buy(self):
        if self.picked is None:
            return
        for widget in self.window.winfo_children():
            if widget != self.l_logo:
                widget.destroy()
        self.window.protocol("WM_DELETE_WINDOW", nothing)
        self.price_bought = self.picked.buy(self.player)
        self.l_bought_first = Label(self.window, text=self.picked.name, font="MiSans 25")
        self.l_bought_first.place(x=250 - (self.l_bought_first.winfo_reqwidth() / 2), y=60)
        self.l_bought = Label(self.window, text="Куплен за " + str(self.price_bought), font="MiSans 30")
        self.l_bought.place(x=250 - (self.l_bought.winfo_reqwidth() / 2), y=110)
        self.window.after(3000, self.choice_club)

    def choice_club(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.window, text="В какой клуб?", font="MiSans 40")
        self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        self.text = ""
        self.club_names = []
        for element in self.available_clubs:
            self.club_names.append(element.name)
        self.list = ttk.Combobox(self.window, values=self.club_names, font="MiSans 20", state="readonly")
        self.list.place(x=250 - (self.list.winfo_reqwidth() // 2), y=640)
        self.b_confirm = Button(self.window, text="Подтвердить", font="MiSans 30", command=self.transfer)
        self.b_confirm.place(x=250 - (self.b_confirm.winfo_reqwidth() // 2), y=700)

    def transfer(self):
        self.selected = self.list.get()
        self.picked.transfer(clubs[self.selected])
        for widget in self.window.winfo_children():
            widget.destroy()
        self.l_logo = Label(self.window, text="Успешно", font="MiSans 40")
        self.l_logo.place(x=250 - (self.l_logo.winfo_reqwidth() // 2), y=0)
        if isinstance(self.picked, Footballer):
            self.l_successfully = Label(self.window, text="Футболист " + self.picked.name + " успешно перешел в клуб " + self.picked.club.name, font="MiSans 20", wraplength=500)
            self.available_clubs = self.player.where_can_i_have_a_footballer()
        elif isinstance(self.picked, Coach):
            self.l_successfully = Label(self.window, text="Тренер " + self.picked.name + " успешно перешел в клуб " + self.picked.club.name, font="MiSans 20", wraplength=500)
            self.available_clubs = self.player.where_can_i_have_a_coach()
        elif isinstance(self.picked, Manager):
            self.l_successfully = Label(self.window, text="Менеджер " + self.picked.name + " успешно перешел в клуб " + self.picked.club.name, font="MiSans 20", wraplength=500)
            self.available_clubs = self.player.where_can_i_have_a_manager()
        self.l_successfully.place(x=250 - self.l_successfully.winfo_reqwidth() // 2, y=80)
        self.available_clubs = []
        self.window.after(3000, self.window.destroy)


class Buy:
    def __init__(self, player, next_step):
        self.player = player
        self.next_step = next_step
        clear()
        self.window = utils.constants.main_window
        self.y = 170
        self.window.title(
            "FOOTBALL MANAGER | Трансферное окно игрока " + self.player.name)
        self.l_logo = Label(self.window,
                            text="Трансферное окно игрока " + self.player.name,
                            font="MiSans 35")
        self.b_back = Button(self.window, text="Назад", font="MiSans 20", command=next_step)
        self.b_back.place(x=20, y=730, height=50)
        self.l_logo.pack(side="top")
        self.buttons = []
        self.names = {"Менеджеры": 100, "Тренеры": 572, "Футболисты": 1044}
        self.index = 0
        for element in self.names.keys():
            self.buttons.append(Button(self.window, text=element, font="MiSans 35"))
            self.buttons[self.index].place(x=self.names[element], y=self.y, width=452, height=100)
            self.index += 1
        self.buttons[0].configure(command=lambda: BuyItems("Manager", self.player))
        self.buttons[1].configure(command=lambda: BuyItems("Coach", self.player))
        self.buttons[2].configure(command=lambda: BuyItems("Footballer", self.player))

    def __close__(self):
        self.window.destroy()
        utils.constants.main_window.after(1000, self.next_step)


class SellItems:
    def __init__(self, type, player, transfer_market, need_money, l_enough):
        self.transfer_market = transfer_market
        self.type = type
        self.player = player
        self.need_money = need_money
        self.l_enough = l_enough
        self.window = Toplevel()
        self.window.resizable(width=False, height=False)
        if self.type == "Footballer":
            self.window.geometry("300x900+1470+30")
            self.window.title("Футболисты игрока " + self.player.name)
            self.l_logo = Label(self.window, text="Футболисты", font="MiSans 30")
            self.found = self.player.search_bought_footballers()
        elif self.type == "Coach":
            self.window.geometry("300x900+1140+30")
            self.window.title("Тренеры игрока " + self.player.name)
            self.l_logo = Label(self.window, text="Тренеры", font="MiSans 30")
            self.found = self.player.search_bought_coaches()
        elif self.type == "Manager":
            self.window.geometry("300x900+810+30")
            self.window.title("Менеджеры игрока " + self.player.name)
            self.l_logo = Label(self.window, text="Менеджеры", font="MiSans 30")
            self.found = self.player.search_bought_managers()
        elif self.type == "TV":
            self.window.geometry("300x900+480+30")
            self.window.title("Телекомпании игрока " + self.player.name)
            self.l_logo = Label(self.window, text="Телекомпании", font="MiSans 30")
            self.found = self.player.search_owned_TVs()
        elif self.type == "Club":
            self.window.geometry("300x900+150+30")
            self.window.title("Клубы игрока " + self.player.name)
            self.l_logo = Label(self.window, text="Клубы", font="MiSans 30")
            self.found = self.player.search_owned_clubs()
        if self.l_enough is not None and self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        elif self.l_enough is not None:
            self.l_enough.switch_off()
        self.l_logo.pack(side="top")
        if not self.found:
            self.l_nothing = Label(self.window, text="Пусто", font="MiSans 50")
            self.l_nothing.place(x=150 - (self.l_nothing.winfo_reqwidth() / 2),
                                 y=400 - (self.l_nothing.winfo_reqheight() / 2))
            return
        self.b_sell = Button(self.window, text="Продать", font="MiSans 40", command=self.sell)
        self.b_sell.place(x=150 - (self.b_sell.winfo_reqwidth() / 2), y=800, height=80)
        self.x = 10
        self.y = 70
        self.will_sell = []
        self.picked = []
        self.check_buttons = []
        for element in range(0, len(self.found)):
            self.picked.append(BooleanVar())
        for element in range(0, len(self.found)):
            self.check_buttons.append(
                Checkbutton(self.window, variable=self.picked[element], text=self.found[element].name,
                            font="MiSans 20"))
            self.check_buttons[element].config(command=self.clicked)
            self.check_buttons[element].place(x=10, y=self.y, height=50)
            self.y += 35
        self.window.mainloop()

    def sell(self):
        self.available = self.will_sell
        if not self.will_sell:
            return
        self.y = 70
        for widget in self.window.winfo_children():
            if widget != self.l_logo:
                widget.destroy()
        if self.type == "Footballer":
            self.found = self.player.search_bought_footballers()
        elif self.type == "Coach":
            self.found = self.player.search_bought_coaches()
        elif self.type == "Manager":
            self.found = self.player.search_bought_managers()
        elif self.type == "TV":
            self.found = self.player.search_owned_TVs()
        elif self.type == "Club":
            self.found = self.player.search_owned_clubs()
        for element in self.will_sell:
            self.price_sold = element.sell(self.transfer_market)
            self.l_sold_first = Label(self.window, text=element.name, font="MiSans 15")
            self.l_sold_first.place(x=150 - (self.l_sold_first.winfo_reqwidth() / 2), y=self.y)
            self.y += 40
            self.l_sold = Label(self.window, text="Продан за " + str(self.price_sold), font="MiSans 20")
            utils.constants.sum -= self.price_sold
            self.l_sold.place(x=150 - (self.l_sold.winfo_reqwidth() / 2), y=self.y)
            self.y += 50
        self.window.after(3000, self.window.destroy)

    def clicked(self):
        for element in range(0, len(self.found)):
            if self.picked[element].get() is True and self.found[element] not in self.will_sell:
                if self.type != "TV" and self.type != "Coach" and self.type != "Club":
                    if self.found[element].dead is not False or self.found[element].flu is not None:
                        self.found[element].sell(self.transfer_market)
                        self.picked[element].set(False)
                    else:
                        self.will_sell.append(self.found[element])
                        utils.constants.sum += self.player.summary_check(
                            self.found[element].price, type="Plus") // self.transfer_market
                elif self.type == "Coach":
                    if self.found[element].dead is not False or self.found[element].flu is not None and self.found[element].strike is not None:
                        self.found[element].sell(self.transfer_market)
                        self.picked[element].set(False)
                    else:
                        self.will_sell.append(self.found[element])
                        utils.constants.sum += self.player.summary_check(
                            self.found[element].price, type="Plus") // self.transfer_market
                elif self.type == "Club":
                    if self.found[element].footballer is not None or self.found[element].coach is not None or self.found[element].manager is not None:
                        self.found[element].sell(self.transfer_market)
                        self.picked[element].set(False)
                    else:
                        self.will_sell.append(self.found[element])
                        utils.constants.sum += self.player.summary_check(self.found[element].price, type="Plus") // self.transfer_market
                else:
                    self.will_sell.append(self.found[element])
                    utils.constants.sum += self.player.summary_check(
                        self.found[element].price, type="Plus") // self.transfer_market
        for element in range(0, len(self.found)):
            if self.picked[element].get() is False and self.found[element] in self.will_sell:
                utils.constants.sum -= self.player.summary_check(
                    self.found[element].price, type="Plus") // self.transfer_market
                self.will_sell.remove(self.found[element])
        if self.l_enough is not None and self.player.balance + utils.constants.sum >= self.need_money:
            self.l_enough.switch_on()
        elif self.l_enough is not None:
            self.l_enough.switch_off()
        # messagebox.showinfo(message=str(self.will_sell))


class Sell:
    def __init__(self, player, next_step, full_screen=True, transfer_market=None, need_money=None):
        self.transfer_market = transfer_market
        self.full_screen = full_screen
        self.player = player
        self.need_money = need_money
        self.next_step = next_step
        utils.constants.sum = 0
        if not self.transfer_market:
            self.transfer_market = 2
        else:
            self.transfer_market = 1
        if self.full_screen:
            clear()
            self.window = utils.constants.main_window
            self.y = 170
        else:
            self.y = 80
            self.window = Toplevel()
            self.window.geometry("1600x200+160+0")
            self.window.protocol("WM_DELETE_WINDOW", self.__close__)
            self.window.resizable(width=False, height=False)
            self.l_logo = Label(self.window, text="FOOTBALL MANAGER", font="MiSans 50")
        if self.transfer_market == 1:
            self.window.title(
                "FOOTBALL MANAGER | Продажа имущества игрока " + self.player.name + " во время трансферного окна")
            self.l_logo = Label(self.window,
                                text="Продажа имущества игрока " + self.player.name + " во время трансферного окна",
                                font="MiSans 35")
            self.b_back = Button(self.window, text="Назад", font="MiSans 20", command=next_step)
            self.b_back.place(x=20, y=730, height=50)
        else:
            self.window.title(
                "FOOTBALL MANAGER | Продажа имущества игрока " + self.player.name)
            self.l_logo = Label(self.window,
                                text="Продажа имущества игрока " + self.player.name,
                                font="MiSans 50")
        self.l_logo.pack(side="top")
        if self.need_money is not None:
            self.l_enough = LEnough()
        else:
            self.l_enough = None
        self.buttons = []
        self.names = {"Клубы": 50, "Телекомпании": 250, "Менеджеры": 635, "Тренеры": 972, "Футболисты": 1230}
        self.index = 0
        for element in self.names.keys():
            self.buttons.append(Button(self.window, text=element, font="MiSans 35"))
            self.buttons[self.index].place(x=self.names[element], y=self.y)
            self.index += 1
        self.buttons[0].configure(command=lambda: SellItems("Club", self.player, self.transfer_market, self.need_money, self.l_enough))
        self.buttons[1].configure(command=lambda: SellItems("TV", self.player, self.transfer_market, self.need_money, self.l_enough))
        self.buttons[2].configure(command=lambda: SellItems("Manager", self.player, self.transfer_market, self.need_money, self.l_enough))
        self.buttons[3].configure(command=lambda: SellItems("Coach", self.player, self.transfer_market, self.need_money, self.l_enough))
        self.buttons[4].configure(command=lambda: SellItems("Footballer", self.player, self.transfer_market, self.need_money, self.l_enough))

    def __close__(self):
        if self.need_money is not None:
            if self.player.balance < self.need_money:
                messagebox.showerror(title="Нужно еще " + str(self.need_money - self.player.balance),
                                     message="Проданного имущества не хватает! Нужно продать еще на " + str(
                                         self.need_money - self.player.balance))
                return
        self.window.destroy()
        try:
            self.l_enough.frame.destroy()
        except:
            pass
        utils.constants.main_window.after(1000, self.next_step)
