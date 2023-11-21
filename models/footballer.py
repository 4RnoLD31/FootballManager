import models.highlighting as hg


class Footballer:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
        self.owner = None
        self.resurrected = False
        self.dead = False
        self.flu = None
        self.club = None

    def transfer(self, new_club):
        self.new_club = new_club
        if self.new_club.footballer is not None and self.club is not None:
            self.club.footballer = self.new_club.footballer
            self.club.footballer.club = self.club
            self.old_footballer = self.new_club.footballer
            self.new_club.footballer = self
            self.club = self.new_club
            print(hg.successful(f"Double transfer: {self.old_footballer.name} to {self.old_footballer.club.name} | {self.name} to {self.club.name}"))
        elif self.new_club.footballer is not None and self.club is None:
            self.new_club.footballer.club = None
            self.old_footballer = self.new_club.footballer
            self.new_club.footballer = self
            self.club = self.new_club
            print(hg.successful(f"Double transfer: {self.old_footballer.name} to Inventory | {self.name} to {self.club.name}"))
        elif self.new_club.footballer is None and self.club is None:
            self.new_club.footballer = self
            self.club = self.new_club
            print(hg.successful(f"Transfer: {self.name} from Inventory to {self.club.name}"))
        elif self.new_club.footballer is None and self.club is not None:
            self.club.footballer = None
            self.new_club.footballer = self
            self.old_club = self.club
            self.club = self.new_club
            print(hg.successful(f"Transfer: {self.name} from {self.old_club.name} to {self.club.name}"))

    def buy(self, player, potential_club=None):
        self.player = player
        self.potential_club = potential_club
        if self.player.balance >= self.player.summary_check(self.price) and self.club is None:
            self.show_price = self.player.withdrawal(self.price)
            self.owner = self.player
            self.club = self.potential_club
            if self.club is not None:
                self.club.footballer = self
                print(hg.successful(f'{self.name} was bought to {self.club.name} by {self.owner.name}'))
            else:
                print(hg.successful(f'{self.name} was bought by {self.owner.name}'))
        else:
            print(hg.failed(f"Insufficient funds for purchase {self.name} | {self.price}"))
            return
        return self.show_price

    def sell(self, transfer_market):
        self.transfer_market = transfer_market
        self.price_sold = self.club.owner.deposit((self.price // 100000 // self.transfer_market) * 100000)
        print(hg.successful(f"{self.name} was sold by {self.owner.name}"))
        self.club.footballer = None
        self.club = None
        self.owner = None
        return self.price_sold

    def die(self):
        self.dead = True
        self.club.footballer = None
        self.club = None
        self.flu = None

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Power": self.power, "Price": self.price, "Resurrected": self.resurrected, "Dead": self.dead, "Flu": self.flu, "Club": self.club, "Owner": self.owner}
        return state

    def __setstate__(self, state: dict):
        self.name = state["Name"]
        self.power = state["Power"]
        self.price = state["Price"]
        self.resurrected = state["Resurrected"]
        self.dead = state["Dead"]
        self.flu = state["Flu"]
        self.club = state["Club"]
        self.owner = state["Owner"]
