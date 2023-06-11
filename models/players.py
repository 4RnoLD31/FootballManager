from utils.constants import *
from tkinter import messagebox


class Player:
    def __init__(self, name, balance, income):
        self.name = str(name)
        self.balance = balance
        self.income = income
        self.payment_TVs_degree = 0
        self.payment_TVs = 0
        self.position = 0
        self.bonuses = {"Vaccine": 0, "Resurrection": 0}
        # Statistics
        self.throws = 0
        self.numbers_thrown = 0
        self.money_earned = 0
        self.money_spent = 0

    def available_clubs(self, for_what="Match"):
        self.for_what = for_what
        self.result = []
        if self.for_what == "Match":
            for element in self.search_owned_clubs():
                if element.cooldown is None and element.footballer is not None and element.footballer.flu is None:
                    self.result.append(element)
        elif self.for_what == "Dead":
            for element in self.search_owned_clubs():
                if element.footballer is not None:
                    self.result.append(element)
        return self.result

    def economist_level(self):
        self.level = 0
        self.economists = self.search_managers_in_clubs()
        for element in self.economists:
            if element.type_manager == "Economist" and element.level > self.level:
                self.level = element.level
        return self.level

    def check_balance(self, summary_old, type="Minus", economist=True):
        self.economist = economist
        self.summary_old = summary_old
        self.type = type
        if self.economist_level() != 0 and self.type == "Minus" and self.economist is True:
            self.summary = round(self.summary_old - self.summary_old * economist_minus_level[self.economist_level()]) // 10000 * 10000
        elif self.economist_level() != 0 and self.type == "Plus" and self.economist is True:
            self.summary = round(self.summary_old + self.summary_old * economist_plus_level[self.economist_level()]) // 10000 * 10000
        else:
            self.summary = round(self.summary_old // 10000 * 10000)
        print("Проверка. Было", self.summary_old, "стало", self.summary)
        return self.summary

    def withdrawal(self, summary, type="Balance", economist=True):
        self.economist = economist
        self.type = type
        self.summary = summary
        if self.economist_level() != 0 and self.economist is True:
            self.summary -= round(self.summary * economist_minus_level[self.economist_level()] // 10000 * 10000)
        if self.type == "Balance":
            if self.summary > self.balance:
                print("Недостаточно средств")
                return
            self.balance -= self.summary
        elif self.type == "Income":
            self.income -= self.summary
        print("Успешный вывод -" + str(self.summary) +" TYPE " + self.type)
        self.money_spent += self.summary
        return self.summary

    def deposit(self, summary, type="Balance", economist=True):
        self.economist = economist
        self.type = type
        self.summary = summary
        if self.economist_level() != 0 and self.economist is True:
            self.summary += round(self.summary * economist_plus_level[self.economist_level()] // 10000 * 10000)
        if self.type == "Balance":
            self.balance += self.summary
        elif self.type == "Income":
            self.income += self.summary
        print("Успешное пополнение +" + str(self.summary) +" TYPE " + self.type)
        self.money_earned += self.summary
        return self.summary

    def search_owned_clubs(self):
        self.found_clubs = []
        for element in clubs.values():
            try:
                if element.owner.name == self.name:
                    self.found_clubs.append(element)
            except:
                pass
        return self.found_clubs

    def search_owned_TVs(self):
        self.found_TVs = []
        for element in TVs.values():
            try:
                if element.owner.name == self.name:
                    self.found_TVs.append(element)
            except:
                pass
        return self.found_TVs

    def search_footballers_in_clubs(self):
        self.found_footballers = []
        for element in footballers.values():
            try:
                if element.club.owner.name == self.name:
                    self.found_footballers.append(element)
            except:
                pass
        return self.found_footballers

    def search_coaches_in_clubs(self):
        self.found_coaches = []
        for element in coaches.values():
            try:
                if element.club.owner.name == self.name:
                    self.found_coaches.append(element)
            except:
                pass
        return self.found_coaches

    def search_managers_in_clubs(self):
        self.found_managers = []
        for element in managers.values():
            try:
                if element.club.owner.name == self.name:
                    self.found_managers.append(element)
            except:
                pass
        return self.found_managers

    def cliched(self):
        self.text = ""
        for element in range(0, len(self.switch_club)):
            if self.switch_club[element].get() == 1:
                self.text += self.list_available_clubs[element].name
        messagebox.showinfo(message=self.text)

    def need_money(self, need):
        clear()
        self.need = need
        self.available_clubs = []
        self.switch_club = []
        self.x = 50
        self.y = 150
        self.names = {"Клубы": 50, "Телекомпании": 240, "Менеджеры": 640, "Тренеры": 980, "Футболисты": 1230}
        for element in self.names.keys():
            self.label = Label(main_window, text=element, font="MiSans 40")
            self.label.place(x=self.names[element], y=200)
        self.l_property = Label(main_window, text="Имущество игрока " + self.name, font="MiSans 50")
        self.l_property.place(x=800 - (self.l_property.winfo_reqwidth() / 2), y=100)
        self.list_available_clubs = self.search_owned_clubs()
        self.list_available_TVs = self.search_owned_TVs()
        self.list_available_managers = self.search_managers_in_clubs()
        self.list_available_coaches = self.search_coaches_in_clubs()
        self.list_available_footballers = self.search_footballers_in_clubs()
        for element in self.list_available_clubs:
            self.switch_club.append(0)
        for element in range(0, len(self.list_available_clubs)):
            print(element)
            self.switch_club[element] = IntVar()
            self.available_clubs.append(
                Checkbutton(main_window, text=self.list_available_clubs[element].name, font="MiSans 50",
                            variable=self.switch_club[element], command=self.cliched))
            self.available_clubs[element].place(x=self.x, y=self.y)
            self.y += 100
