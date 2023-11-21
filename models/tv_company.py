import utils.constants as const
import models.highlighting as hg
import models.field as field
import models.property as property

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
            self.owner.payment_TVs = const.gradual_income[self.owner.payment_TVs_degree - 1]
            self.owner.withdrawal(self.price)
            print(hg.successful(f'{self.name} was bought by "{self.owner.name}"'))
        else:
            print(hg.failed(f"Insufficient funds for purchase {self.name} | {self.price}"))

    def change_owner(self, owner):
        self.owner = owner

    def sell(self, *args):
        self.price_sold = self.owner.deposit(self.price // 2)
        self.owner.payment_const.TVs_degree -= 1
        self.owner.payment_const.TVs = const.gradual_income[self.owner.payment_const.TVs_degree - 1]
        self.owner = None
        return self.price_sold

    def get_fine(self, type_fine):
        self.type_fan = type_fine

    def get_gain(self, stepped_player):
        const.text_on_center(f"Игрок {stepped_player.name} должен выплатить {self.owner.payment_TVs} игроку {self.owner.name}", "MiSans 40")
        const.main_window.after(4000, self.__gg_first__, stepped_player)

    def __gg_first__(self, stepped_player):
        if stepped_player.balance >= stepped_player.check_withdrawal(self.owner.payment_TVs):
            stepped_player.withdrawal(self.owner.payment_TVs)
            self.owner.deposit(self.owner.payment_TVs)
            const.text_on_center(f"{stepped_player.name} успешно перевел {self.owner.payment_TVs}", "MiSans 40")
            const.main_window.after(4000, field.Field.new_move)
        else:
            const.text_on_center(f"{stepped_player.name} не смог перевести {self.owner.payment_TVs}. Ему не хватает {stepped_player.balance - stepped_player.check_withdrawal(self.owner.payment_TVs)}", "MiSans 40")
            const.main_window.after(4000, lambda: property.Sell(stepped_player, lambda: self.__gg_first__(stepped_player), need_money=stepped_player.check_withdrawal(self.owner.payment_TVs)))

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Price": self.price, "Potential Owner": self.potential_owner, "Owner": self.owner}
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.price = state["Price"]
        self.potential_owner = state["Potential Owner"]
        self.owner = state["Owner"]
