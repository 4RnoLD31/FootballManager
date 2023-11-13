import tkinter as tk
import utils.constants as const
import models.highlighting as hg
from tkinter import messagebox


class Player:
    def __init__(self, name, balance, income):
        self.name = str(name)
        self.balance = balance
        self.income = income
        self.payment_TVs_degree = 0
        self.payment_TVs = 0
        self.position = 0
        self.avatar = None
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
        self.economists = self.search_bought_managers()
        for element in self.economists:
            if element.type == "Economist" and element.level > self.level:
                self.level = element.level
        return self.level

    def check_withdrawal(self, summary, economist=True):
        self.summary = summary
        self.economist = economist
        if self.economist_level() != 0:
            self.summary = round(self.summary - self.summary * const.economist_minus_level[self.economist_level()]) // 10000 * 10000
        if self.balance >= self.summary:
            return True
        else:
            return False

    def summary_check(self, summary_old, type="Minus", economist=True):
        self.economist = economist
        self.summary_old = summary_old
        self.type = type
        if self.economist_level() != 0 and self.type == "Minus" and self.economist is True:
            self.summary = round(self.summary_old - self.summary_old * const.economist_minus_level[self.economist_level()]) // 10000 * 10000
        elif self.economist_level() != 0 and self.type == "Plus" and self.economist is True:
            self.summary = round(self.summary_old + self.summary_old * const.economist_plus_level[self.economist_level()]) // 10000 * 10000
        else:
            self.summary = round(self.summary_old // 10000 * 10000)
        # print(hg.c_info(f"Check for {self.name}: before {self.summary_old} after {self.summary}"))
        return self.summary

    def withdrawal(self, summary, type="Balance", economist=True):
        self.economist = economist
        self.type = type
        self.summary = summary
        if self.economist_level() != 0 and self.economist is True:
            self.summary -= round(self.summary * const.economist_minus_level[self.economist_level()] // 10000 * 10000)
        if self.type == "Balance":
            if self.summary > self.balance:
                print(hg.c_failed(f"{self.name} was unable to withdraw {self.summary} from {self.type}"))
                return False
            self.balance -= self.summary
        elif self.type == "Income":
            self.income -= self.summary
        # print(hg.c_successful(f"{self.name} withdrew {self.summary} from {self.type}"))
        self.money_spent += self.summary
        return self.summary

    def deposit(self, summary, type="Balance", economist=True):
        self.economist = economist
        self.type = type
        self.summary = summary
        if self.economist_level() != 0 and self.economist is True:
            self.summary += round(self.summary * const.economist_plus_level[self.economist_level()] // 10000 * 10000)
        if self.type == "Balance":
            self.balance += self.summary
        elif self.type == "Income":
            self.income += self.summary
        # print(hg.c_info(f"{self.name}'s balance has been deposited by {self.summary} to {self.type}"))
        self.money_earned += self.summary
        return self.summary

    def full_leagues(self):
        self.leagues = []
        self.apl = self.la_liga = self.seria_a = self.bundesleague = self.rpl = 0
        for element in const.clubs.keys():
            if const.clubs[element].owner == self:
                if const.clubs[element].league == "EPL":
                    self.apl += 1
                elif const.clubs[element].league == "La Liga":
                    self.la_liga += 1
                elif const.clubs[element].league == "Seria A":
                    self.seria_a += 1
                elif const.clubs[element].league == "Bundesliga":
                    self.bundesleague += 1
                elif const.clubs[element].league == "RPL":
                    self.rpl += 1
        if self.apl == 3:
            self.leagues.append("EPL")
        if self.la_liga == 3:
            self.leagues.append("La Liga")
        if self.seria_a == 3:
            self.leagues.append("Seria A")
        if self.bundesleague == 3:
            self.leagues.append("Bundesliga")
        if self.rpl == 3:
            self.leagues.append("RPL")
        return self.leagues

    def search_owned_clubs(self):
        self.found_clubs = []
        for element in const.clubs.values():
            try:
                if element.owner == self:
                    self.found_clubs.append(element)
            except:
                pass
        return self.found_clubs

    def search_owned_TVs(self):
        self.found_TVs = []
        for element in const.TVs.values():
            try:
                if element.owner == self:
                    self.found_TVs.append(element)
            except:
                pass
        return self.found_TVs

    def search_bought_footballers(self, type="Sell"):
        self.found_footballers = []
        for element in const.footballers.values():
            try:
                if element.owner == self:
                    self.found_footballers.append(element)
                if type == "Sell" and element.club.coach is not None or element.club.manager is not None:
                    self.found_footballers.remove(element)
            except:
                pass
        return self.found_footballers

    def search_bought_coaches(self, type="Sell"):
        self.found_coaches = []
        for element in const.coaches.values():
            try:
                if element.owner == self:
                    self.found_coaches.append(element)
                if type == "Sell" and element.club.manager is not None:
                    self.found_coaches.remove(element)
            except:
                pass
        return self.found_coaches

    def search_bought_managers(self):
        self.found_managers = []
        for element in const.managers.values():
            try:
                if element.owner == self:
                    self.found_managers.append(element)
            except:
                pass
        return self.found_managers

    def clicked(self):
        self.text = ""
        for element in range(0, len(self.switch_club)):
            if self.switch_club[element].get() == 1:
                self.text += self.list_available_clubs[element].name
        messagebox.showinfo(message=self.text)

    def need_money(self, need):
        const.clear()
        self.need = need
        self.available_clubs = []
        self.switch_club = []
        self.x = 50
        self.y = 150
        self.names = {"Клубы": 50, "Телекомпании": 240, "Менеджеры": 640, "Тренеры": 980, "Футболисты": 1230}
        for element in self.names.keys():
            self.label = tk.Label(const.main_window, text=element, font="MiSans 40")
            self.label.place(x=self.names[element], y=200)
        self.l_property = tk.Label(const.main_window, text=f"Имущество игрока {self.name}", font="MiSans 50")
        self.l_property.place(x=800 - (self.l_property.winfo_reqwidth() / 2), y=100)
        self.list_available_clubs = self.search_owned_clubs()
        self.list_available_TVs = self.search_owned_TVs()
        self.list_available_managers = self.search_bought_managers()
        self.list_available_coaches = self.search_bought_coaches()
        self.list_available_footballers = self.search_bought_footballers()
        for element in self.list_available_clubs:
            self.switch_club.append(0)
        for element in range(0, len(self.list_available_clubs)):
            self.switch_club[element] = tk.IntVar()
            self.available_clubs.append(tk.Checkbutton(const.main_window, text=self.list_available_clubs[element].name, font="MiSans 50", variable=self.switch_club[element], command=self.clicked))
            self.available_clubs[element].place(x=self.x, y=self.y)
            self.y += 100

    def where_can_i_have_a_footballer(self, without=True):
        self.clubs = []
        self.to_delete = []
        for element in const.clubs.keys():
            if const.clubs[element].owner == self:
                self.clubs.append(const.clubs[element])
        if without:
            for element in self.clubs:
                if element.footballer is not None:
                    self.to_delete.append(element)
            for element in self.to_delete:
                self.clubs.remove(element)
        if not self.clubs:
            return None
        else:
            return self.clubs

    def where_can_i_have_a_coach(self, without=True):
        self.clubs = []
        self.l_full_leagues = self.full_leagues()
        for element in const.clubs.keys():
            if const.clubs[element].owner == self and const.clubs[element].footballer is not None and const.clubs[element].league in self.l_full_leagues:
                self.clubs.append(const.clubs[element])
        if len(self.clubs) < 3:
            return None
        while len(self.clubs) % 3 != 0 or len(self.l_full_leagues) * 3 > len(self.clubs):
            self.impostor_league = None
            self.to_delete = []
            for element in const.clubs.keys():
                if const.clubs[element].owner == self and const.clubs[element].footballer is None and const.clubs[element].league in self.l_full_leagues:
                    self.impostor_league = const.clubs[element].league
                    break
            for element in self.clubs:
                if element.league == self.impostor_league:
                    self.to_delete.append(element)
            for element in self.to_delete:
                self.clubs.remove(element)
            self.l_full_leagues.remove(self.impostor_league)
        self.to_delete = []
        for element in self.clubs:
            if element.coach is not None:
                self.to_delete.append(element)
        if without:
            for element in self.to_delete:
                self.clubs.remove(element)
        if not self.clubs:
            return None
        else:
            return self.clubs

    def where_can_i_have_a_manager(self, without=True):
        self.clubs = []
        self.l_full_leagues = self.full_leagues()
        for element in const.clubs.keys():
            if const.clubs[element].owner == self and const.clubs[element].footballer is not None and const.clubs[element].coach is not None and const.clubs[element].league in self.l_full_leagues:
                self.clubs.append(const.clubs[element])
        if len(self.clubs) < 3:
            return None
        while len(self.clubs) % 3 != 0 or len(self.l_full_leagues) * 3 > len(self.clubs):
            self.impostor_league = None
            self.to_delete = []
            for element in const.clubs.keys():
                if const.clubs[element].owner == self and const.clubs[element].coach is None and const.clubs[element].league in self.l_full_leagues:
                    self.impostor_league = const.clubs[element].league
                    break
            for element in self.clubs:
                if element.league == self.impostor_league:
                    self.to_delete.append(element)
            for element in self.to_delete:
                self.clubs.remove(element)
            self.l_full_leagues.remove(self.impostor_league)
        self.to_delete = []
        for element in self.clubs:
            if element.manager is not None:
                self.to_delete.append(element)
        if without:
            for element in self.to_delete:
                self.clubs.remove(element)
        if not self.clubs:
            return None
        else:
            return self.clubs

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Balance": self.balance, "Income": self.income, "Payment const.TVs Degree": self.payment_TVs_degree, "Payment const.TVs": self.payment_TVs, "Position": self.position, "Avatar": self.avatar, "Bonuses": self.bonuses, "Throws": self.throws, "Numbers Thrown": self.numbers_thrown, "Money Earned": self.money_earned, "Money Spent": self.money_spent}
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.balance = state["Balance"]
        self.income = state["Income"]
        self.payment_TVs_degree = state["Payment const.TVs Degree"]
        self.payment_TVs = state["Payment const.TVs"]
        self.position = state["Position"]
        self.avatar = state["Avatar"]
        self.bonuses = state["Bonuses"]
        self.throws = state["Throws"]
        self.numbers_thrown = state["Numbers Thrown"]
        self.money_earned = state["Money Earned"]
        self.money_spent = state["Money Spent"]
