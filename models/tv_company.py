from utils.constants import *
from models.highlighting import *


class TVCompany:
    def __init__(self, name):
        self.name = name
        self.price = 2000000
        self.potential_owner = None
        self.owner = None

    def buy(self, potential_owner):
        self.potential_owner = potential_owner
        if self.potential_owner.balance >= self.potential_owner.summary_check(self.price):
            self.owner = self.potential_owner
            self.owner.payment_TVs_degree += 1
            self.owner.payment_TVs = gradual_income[self.owner.payment_TVs_degree - 1]
            self.owner.withdrawal(self.price)
            print(c_successful(f'{self.name} was bought by "{self.owner.name}"'))
        else:
            print(c_failed(f"Insufficient funds for purchase {self.name} | {self.price}"))

    def change_owner(self, owner):
        self.owner = owner

    def sell(self, *args):
        self.price_sold = self.owner.deposit(self.price // 2)
        self.owner.payment_TVs_degree -= 1
        self.owner.payment_TVs = gradual_income[self.owner.payment_TVs_degree - 1]
        self.owner = None
        return self.price_sold

    def get_fine(self, type_fine):
        self.type_fan = type_fine

    def stepped_on(self):
        pass

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Price": self.price, "Potential Owner": self.potential_owner, "Owner": self.owner}
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.price = state["Price"]
        self.potential_owner = state["Potential Owner"]
        self.owner = state["Owner"]
