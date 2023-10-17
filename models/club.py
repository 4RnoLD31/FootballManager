from utils.constants import *


class Club:
    def __init__(self, name, price, league, color_font, codename):
        self.name = name
        self.price = price
        self.league = league
        self.color_font = color_font
        self.codename = codename
        self.income = round(self.price // 100000 // 10) * 100000
        self.win_footballer = round(self.price // 100000 // 3) * 100000
        self.win_coach = round(self.price // 100000 // 1.5) * 100000
        self.win_manager = round(self.price // 100000 * 2) * 100000
        self.cooldown = None
        self.footballer = None
        self.coach = None
        self.manager = None
        self.potential_owner = None
        self.owner = None
        self.img_bg = working_directory + "/assets/clubs/" + self.codename + "/background.mp4"
        self.img_title = working_directory + "/assets/clubs/" + self.codename + "/title.png"
        self.img_emblem = working_directory + "/assets/clubs/" + self.codename + "/emblem.png"

    def buy(self, potential_owner):
        self.potential_owner = potential_owner
        if self.owner != self.potential_owner and self.owner is not None:
            print("Клуб куплен")
        elif self.potential_owner.balance >= self.potential_owner.check_balance(self.price):
            self.owner = self.potential_owner
            self.owner.withdrawal(self.price)
            self.owner.deposit(self.income, "Income")
            print("Клуб приобретен")
        else:
            print("Недостаточно средств")

    def change_owner(self, owner):
        self.owner = owner

    def current_win(self):
        self.result = 0
        if self.manager is not None:
            self.result = self.win_manager
            if self.manager.type_manager == "Sheikh":
                self.result += sheikh_level[self.manager.level]
        elif self.coach is not None:
            self.result = self.win_coach
        elif self.footballer is not None:
            self.result = self.win_footballer
        return self.result

    def power(self):
        self.result = 0
        try:
            self.result += self.footballer.power
            self.result += self.coach.power
            self.result += former_footballer_level[self.manager.level]
        except:
            pass
        return self.result

    def sell(self, new_owner, on_the_transfer_market):
        self.on_the_transfer_market = on_the_transfer_market
        self.new_owner = new_owner
        self.reason_error = []
        self.reason_error.append(self.footballer)
        self.reason_error.append(self.coach)
        self.reason_error.append(self.manager)
        if self.reason_error[0] is not None or self.reason_error[1] is not None or self.reason_error[2] is not None:
            self.text = "Ошибка 1: В клубе " + self.name + " присутствуют: "
            for element in self.reason_error:
                if element is not None:
                    self.text += element.name + ", "
            self.text = self.text[:-2]
            messagebox.showerror(title="Ошибка 1", message=self.text)
            return
        self.price_sold = self.owner.deposit(round(self.price // 100000 // self.on_the_transfer_market) * 100000)
        self.owner.withdrawal(self.income, "Income")
        self.owner = self.new_owner
        print("Клуб продан", self.owner)
        return self.price_sold

    def get_fine(self, type_fine):
        self.type_fan = type_fine

    def win(self, club):
        self.club = club
        self.summary = self.current_win()
        if self.club.owner.balance >= self.summary:
            self.club.owner.withdrawal(self.summary, economist=False)
            self.owner.deposit(self.summary, economist=False)
        else:
            print("Не удалось выплатить деньги за поражение")

    def lose(self, club):
        self.club = club
        self.summary = self.club.current_win()
        if self.owner.balance >= self.summary:
            self.owner.withdrawal(self.summary, economist=False)
            self.club.owner.deposit(self.summary, economist=False)
        else:
            print("Не удалось выплатить деньги за поражение")

    def available(self):
        self.result = False
        if self.cooldown is None and self.footballer is not None and self.footballer.flu is None:
            self.result = True
        return self.result

    def __getstate__(self) -> dict:
        state = {}
        state["Name"] = self.name
        state["Price"] = self.price
        state["League"] = self.league
        state["Color Font"] = self.color_font
        state["Codename"] = self.codename
        state["Income"] = self.income
        state["Win Footballer"] = self.win_footballer
        state["Win Coach"] = self.win_coach
        state["Win Manager"] = self.win_manager
        state["Cooldown"] = self.cooldown
        state["Footballer"] = self.footballer
        state["Coach"] = self.coach
        state["Manager"] = self.manager
        state["Potential Owner"] = self.potential_owner
        state["Owner"] = self.owner
        state["Image Background"] = self.img_bg
        state["Image Title"] = self.img_title
        state["Image Emblem"] = self.img_emblem
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.price = state["Price"]
        self.league = state["League"]
        self.color_font = state["Color Font"]
        self.codename = state["Codename"]
        self.income = state["Income"]
        self.win_footballer = state["Win Footballer"]
        self.win_coach = state["Win Coach"]
        self.win_manager = state["Win Manager"]
        self.cooldown = state["Cooldown"]
        self.footballer = state["Footballer"]
        self.coach = state["Coach"]
        self.manager = state["Manager"]
        self.potential_owner = state["Potential Owner"]
        self.owner = state["Owner"]
        self.img_bg = state["Image Background"]
        self.img_title = state["Image Title"]
        self.img_emblem = state["Image Emblem"]



