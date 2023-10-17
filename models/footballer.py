from utils.constants import *


class Footballer:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
        self.type = "Footballer"
        self.resurrected = False
        self.dead = False
        self.flu = False
        self.club = None

    def buy(self, player, potential_club):
        self.player = player
        self.potential_club = potential_club
        if self.player.balance >= self.player.check_balance(self.price) and self.club is None and self.potential_club.owner == self.player:
            self.player.withdrawal(self.price)
            self.club = self.potential_club
            self.club.footballer = self
        else:
            print("Недостаточно средств")

    def sell(self, on_the_transfer_market):
        self.on_the_transfer_market = on_the_transfer_market
        if self.dead is not False:
            messagebox.showerror(title="Ошибка 2", message="Футболист " + self.name + " мертв. Вы не можете его продать")
            return
        elif self.flu is not False:
            messagebox.showerror(title="Ошибка 3", message=self.name + " болеет. Он выздоровеет через " + str(self.flu) + " ходов. Вы не можете его продать")
            return
        self.price_sold = self.club.owner.deposit((self.price // 100000 // self.on_the_transfer_market) * 100000)
        self.club.footballer = None
        self.club = None
        print("Футболист продан")
        return self.price_sold

    def die(self):
        self.dead = True
        self.club.footballer = None
        self.club = None
        self.flu = False

    def __getstate__(self) -> dict:
        state = {}
        state["Name"] = self.name
        state["Power"] = self.power
        state["Price"] = self.price
        state["Type"] = self.type
        state["Resurrected"] = self.resurrected
        state["Dead"] = self.dead
        state["Flu"] = self.flu
        state["Club"] = self.club
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.power = state["Power"]
        self.price = state["Price"]
        self.type = state["Type"]
        self.resurrected = state["Resurrected"]
        self.dead = state["Dead"]
        self.flu = state["Flu"]
        self.club = state["Club"]
