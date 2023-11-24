import models.highlighting as hg


class Manager:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price
        self.level = 1
        self.owner = None
        self.resurrected = False
        self.dead = False
        self.flu = None
        self.club = None

    def available(self):
        if self.flu is None and self.dead is False:
            return True
        else:
            return False

    def buy(self, player, potential_club=None):
        self.player = player
        self.potential_club = potential_club
        if self.player.balance >= self.player.summary_check(self.price) and self.club is None:
            self.show_price = self.player.withdrawal(self.price)
            self.club = self.potential_club
            self.owner = self.player
            if self.club is not None:
                self.club.manager = self
        else:
            print(hg.failed(f"Insufficient funds for purchase {self.name} | {self.price}"))
            return
        return self.show_price

    def sell(self, transfer_market):
        self.transfer_market = transfer_market
        self.price_sold = self.club.owner.deposit((self.price // 100000 // self.transfer_market) * 100000)
        print(hg.successful(f"{self.name} was sold by {self.owner.name} | {self.price_sold}"))
        self.club.manager = None
        self.club = None
        self.owner = None
        return self.price_sold

    def die(self):
        self.dead = True
        self.club.manager = None
        self.club = None
        self.flu = None

    def revive(self):
        self.dead = False
        self.resurrected = True

    def transfer(self, new_club):
        self.new_club = new_club
        if self.new_club.manager is not None and self.club is not None:
            self.club.manager = self.new_club.manager
            self.club.manager.club = self.club
            self.old_manager = self.new_club.manager
            self.new_club.manager = self
            self.club = self.new_club
            print(hg.successful(f"Double transfer: {self.old_manager.name} to {self.old_manager.club.name} | {self.name} to {self.club.name}"))
        elif self.new_club.manager is not None and self.club is None:
            self.new_club.manager.club = None
            self.old_manager = self.new_club.manager
            self.new_club.manager = self
            self.club = self.new_club
            print(hg.successful(f"Double transfer: {self.old_manager.name} to Inventory | {self.name} to {self.club.name}"))
        elif self.new_club.manager is None and self.club is None:
            self.new_club.manager = self
            self.club = self.new_club
            print(hg.successful(f"Transfer: {self.name} from Inventory to {self.club.name}"))
        elif self.new_club.manager is None and self.club is not None:
            self.club.manager = None
            self.new_club.manager = self
            self.old_club = self.club
            self.club = self.new_club
            print(hg.successful(f"Transfer: {self.name} from {self.old_club.name} to {self.club.name}"))

    def __getstate__(self) -> dict:
        state = {"Name": self.name, "Type Manager": self.type, "Price": self.price, "Level": self.level, "Type": self.type, "Resurrected": self.resurrected, "Dead": self.dead, "Flu": self.flu, "Club": self.club, "Owner": self.owner}
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
        self.owner = state["Owner"]
