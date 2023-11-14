import models.highlighting as hg
from tkinter import messagebox


class Coach:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
        self.resurrected = False
        self.dead = False
        self.owner = None
        self.flu = None
        self.club = None
        self.strike = None

    def buy(self, player, potential_club=None):
        self.player = player
        self.potential_club = potential_club
        if self.player.balance >= self.player.summary_check(self.price) and self.club is None:
            self.show_price = self.player.withdrawal(self.price)
            self.owner = self.player
            self.club = self.potential_club
            if self.club is not None:
                self.club.coach = self
                print(hg.successful(f'{self.name} was bought to {self.club.name} by {self.owner.name}'))
            else:
                print(hg.successful(f'{self.name} was bought by {self.owner.name}'))
        else:
            print(hg.failed(f"Insufficient funds for purchase {self.name} | {self.price}"))
            return
        return self.show_price

    def sell(self, transfer_market):
        self.transfer_market = transfer_market
        self.text = f"Тренер {self.name} "
        if self.strike is not None:
            self.text += f"устроил забастовку. Она продлится {self.strike} ходов. Также он"
        if self.flu is not None:
            self.text += f"заболел. Болезнь продлится {self.flu} ходов. Также он"
        if self.strike is not None or self.flu is not None:
            self.text = self.text[:-10]
            messagebox.showerror(title="Ошибка 2", message=self.text)
            return
        self.price_sold = self.club.owner.deposit(round(self.price // 100000 // self.transfer_market) * 100000)
        print(hg.successful(f"{self.name} was sold by {self.owner.name}"))
        self.club.coach = None
        self.club = None
        self.owner = None
        return self.price_sold

    def die(self):
        self.dead = True
        self.club.coach = None
        self.club = None
        self.flu = None
        self.strike = False

    def transfer(self, new_club):
        self.new_club = new_club
        if self.new_club.coach is not None and self.club is not None:
            self.club.coach = self.new_club.coach
            self.club.coach.club = self.club
            self.old_coach = self.new_club.coach
            self.new_club.coach = self
            self.club = self.new_club
            print(hg.successful(f"Double transfer: {self.old_coach.name} to {self.old_coach.club.name} | {self.name} to {self.club.name}"))
        elif self.new_club.coach is not None and self.club is None:
            self.new_club.coach.club = None
            self.old_coach = self.new_club.coach
            self.new_club.coach = self
            self.club = self.new_club
            print(hg.successful(f"Double transfer: {self.old_coach.name} to Inventory | {self.name} to {self.club.name}"))
        elif self.new_club.coach is None and self.club is None:
            self.new_club.coach = self
            self.club = self.new_club
            print(hg.successful(f"Transfer: {self.name} from Inventory to {self.club.name}"))
        elif self.new_club.coach is None and self.club is not None:
            self.club.coach = None
            self.new_club.coach = self
            self.old_club = self.club
            self.club = self.new_club
            print(hg.successful(f"Transfer: {self.name} from {self.old_club.name} to {self.club.name}"))

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Power": self.power, "Price": self.price, "Resurrected": self.resurrected, "Dead": self.dead, "Flu": self.flu, "Club": self.club, "Strike": self.strike, "Owner": self.owner}
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.power = state["Power"]
        self.price = state["Price"]
        self.resurrected = state["Resurrected"]
        self.dead = state["Dead"]
        self.flu = state["Flu"]
        self.club = state["Club"]
        self.strike = state["Strike"]
        self.owner = state["Owner"]
