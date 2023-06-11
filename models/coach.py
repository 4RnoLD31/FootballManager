import utils.constants
from utils.constants import *

class Coach:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
        self.type = "Coach"
        self.resurrected = False
        self.dead = False
        self.flu = False
        self.club = None
        self.strike = False


    def buy(self, player, potential_club):
        self.player = player
        self.potential_club = potential_club
        if self.player.balance >= self.player.check_balance(
                self.price) and self.club is None and self.potential_club.owner == self.player:
            self.player.withdrawal(self.price)
            self.club = self.potential_club
            self.club.coach = self
        else:
            print("Недостаточно средств")

    def sell(self, on_the_transfer_market):
        self.on_the_transfer_market = on_the_transfer_market
        self.text = "Тренер " + self.name + " "
        if self.strike is not False:
            self.text += "устроил забастовку. Она продлится " + str(self.strike) + " ходов. Также он"
        if self.flu is not False:
            self.text += "заболел. Болезнь продлится " + str(self.flu) + " ходов. Также он"
        if self.strike is not False or self.flu is not False:
            self.text = self.text[:-10]
            messagebox.showerror(title="Ошибка 2", message=self.text)
            return
        self.price_sold = self.club.owner.deposit(round(self.price // 100000 // self.on_the_transfer_market) * 100000)
        self.club.coach = None
        self.club = None
        print("Тренер продан")
        return self.price_sold

    def die(self):
        self.dead = True
        self.club.coach = None
        self.club = None
        self.flu = False
        self.strike = False