from utils.constants import *

class Footballer:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
        self.type = "Footballer"
        self.resurrected = False
        self.dead = False
        self.flu = None
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