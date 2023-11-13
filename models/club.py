import utils.constants as const
import models.highlighting as hg
from tkinter import messagebox


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
        self.img_bg = f"{const.working_directory}/assets/const.clubs/{self.codename}/background.mp4"
        self.img_title = f"{const.working_directory}/assets/const.clubs/{self.codename}//title.png"
        self.img_emblem = f"{const.working_directory}/assets/const.clubs/{self.codename}//emblem.png"

    def buy(self, potential_owner):
        self.potential_owner = potential_owner
        if self.potential_owner.balance >= self.potential_owner.summary_check(self.price):
            self.owner = self.potential_owner
            self.owner.withdrawal(self.price)
            self.owner.deposit(self.income, "Income")
            print(hg.c_successful(f'{self.name} was bought by "{self.owner.name}"'))
        else:
            print(hg.c_failed(f"Insufficient funds for purchase {self.name} | {self.price}"))

    def change_owner(self, owner):
        self.owner = owner

    def current_win(self):
        self.result = 0
        if self.manager is not None:
            self.result = self.win_manager
            if self.manager.type == "Sheikh":
                self.result += const.sheikh_level[self.manager.level]
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
            self.result += const.former_footballer_level[self.manager.level]
        except AttributeError:
            pass
        return self.result

    def sell(self, transfer_market):
        self.transfer_market = transfer_market
        self.reason_error = []
        self.reason_error.append(self.footballer)
        self.reason_error.append(self.coach)
        self.reason_error.append(self.manager)
        if self.reason_error[0] is not None or self.reason_error[1] is not None or self.reason_error[2] is not None:
            self.text = f"Ошибка 1: В клубе {self.name} присутствуют: "
            for element in self.reason_error:
                if element is not None:
                    self.text += f"{element.name}, "
            self.text = self.text[:-2]
            messagebox.showerror(title="Ошибка 1", message=self.text)
            return
        self.price_sold = self.owner.deposit(round(self.price // 100000 // self.transfer_market) * 100000)
        self.owner.withdrawal(self.income, "Income")
        print(hg.c_successful(f"{self.name} was sold by {self.owner.name}"))
        self.owner = None
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
            pass

    def lose(self, club):
        self.club = club
        self.summary = self.club.current_win()
        if self.owner.balance >= self.summary:
            self.owner.withdrawal(self.summary, economist=False)
            self.club.owner.deposit(self.summary, economist=False)
        else:
            pass

    def available(self):
        self.result = False
        if self.cooldown is None and self.footballer is not None and self.footballer.flu is None:
            self.result = True
        return self.result

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Price": self.price, "League": self.league, "Color Font": self.color_font, "Codename": self.codename, "Income": self.income, "Win Footballer": self.win_footballer, "Win Coach": self.win_coach, "Win Manager": self.win_manager, "Cooldown": self.cooldown, "Footballer": self.footballer, "Coach": self.coach, "Manager": self.manager, "Potential Owner": self.potential_owner, "Owner": self.owner, "Image Background": self.img_bg, "Image Title": self.img_title, "Image Emblem": self.img_emblem}
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
