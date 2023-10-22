from utils.constants import *

class Manager:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
        self.level = 1
        self.resurrected = False
        self.dead = False
        self.flu = 20
        self.club = None

    def buy(self, player, potential_club):
        self.player = player
        self.potential_club = potential_club
        if self.player.balance >= self.player.check_balance(self.price) and self.club is None and self.potential_club.owner == self.player:
            self.player.withdrawal(self.price)
            self.club = self.potential_club
            self.club.manager = self
        else:
            print("Недостаточно средств")

    def sell(self, on_the_transfer_market):
        self.on_the_transfer_market = on_the_transfer_market
        if self.dead is not False:
            messagebox.showerror(title="Ошибка 2",
                                 message="Менеджер " + self.name + " мертв. Вы не можете его продать")
            return
        elif self.flu is not False:
            messagebox.showerror(title="Ошибка 3", message=self.name + " болеет. Он выздоровеет через " + str(
                self.flu) + " ходов. Вы не можете его продать")
            return
        self.price_sold = self.club.owner.deposit((self.price // 100000 // self.on_the_transfer_market) * 100000)
        self.club.manager = None
        self.club = None
        print("Менеджер продан")
        return self.price_sold

    def die(self):
        self.dead = True
        self.club.manager = None
        self.club = None
        self.flu = False

    def __getstate__(self) -> dict:
        state = {}
        state["Name"] = self.name
        state["Type Manager"] = self.type
        state["Price"] = self.price
        state["Level"] = self.level
        state["Type"] = self.type
        state["Resurrected"] = self.resurrected
        state["Dead"] = self.dead
        state["Flu"] = self.flu
        state["Club"] = self.club
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.type = state["Type Manager"]
        self.price = state["Price"]
        self.level = state["Level"]
        self.type = state["Type"]
        self.resurrected = state["Resurrected"]
        self.dead = state["Dead"]
        self.flu = state["Flu"]
        self.club = state["Club"]
