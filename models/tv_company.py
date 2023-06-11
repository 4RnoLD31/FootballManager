from utils.constants import *


class TVCompany:
    def __init__(self, name):
        self.name = name
        self.price = 2000000
        self.potential_owner = None
        self.owner = None

    def buy(self, potential_owner):
        self.potential_owner = potential_owner
        if self.owner != self.potential_owner and self.owner is not None:
            print("TV куплен")
        elif self.potential_owner.balance >= self.potential_owner.check_balance(self.price):
            self.owner = self.potential_owner
            self.owner.payment_TVs_degree += 1
            self.owner.payment_TVs = gradual_income[self.owner.payment_TVs_degree - 1]
            print(self.owner.payment_TVs)
            self.owner.withdrawal(self.price)
            print("TV приобретен")
        else:
            print("Недостаточно средств")

    def change_owner(self, owner):
        self.owner = owner

    def sell(self):
        self.price_sold = self.owner.deposit(self.price // 2)
        self.owner.payment_TVs_degree -= 1
        self.owner.payment_TVs = gradual_income[self.owner.payment_TVs_degree - 1]
        self.owner = None
        return self.price_sold


    def get_fine(self, type_fine):
        self.type_fan = type_fine

    def stepped_on(self):
        pass
