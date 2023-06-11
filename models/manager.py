from utils.constants import *

class Manager:
    def __init__(self, name, type_manager):
        self.name = name
        self.type_manager = type_manager
        self.price = 8000000
        self.level = 1
        self.type = "Manager"
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