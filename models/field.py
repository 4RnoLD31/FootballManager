import utils.constants
from utils.constants import *
from models.stepped import stepped_on_club, stepped_on_tv_company
from models.property import Sell
from random import choice, choices
from models.save_game import save_game
from models.transfer_window import TransferWindow
from models.highlighting import *


def field(player):
    if player.position == 0:
        start_pos(player)
    elif player.position == 1:
        stepped_on_club(player, clubs["Barcelona"])
    elif player.position == 2 or player.position == 20:
        random_bonus(player)
    elif player.position == 3:
        stepped_on_club(player, clubs["Real Madrid"])
    elif player.position == 4:
        stepped_on_tv_company(player, TVs["Setanta Sports"])
    elif player.position == 5:
        stepped_on_club(player, clubs["Валенсия"])
    elif player.position == 6:
        TransferWindow(player)
    elif player.position == 14 or player.position == 30:
        random_fine(player)


def new_move(player):
    save_game()
    if player == utils.constants.PL1:
        utils.constants.next_player = utils.constants.PL2
    elif player == utils.constants.PL2:
        utils.constants.next_player = utils.constants.PL1
    clear()
    # number = randint(2, 12)
    number = 6
    player.numbers_thrown += number
    player.throws += 1
    if player.position + number > 31:
        player.position = player.position + number - 31
    else:
        player.position += number
    text_on_center("Бросаю куб...", font="MiSans 50")
    utils.constants.main_window.after(2000, nothing)
    text_on_center(f"Игрок {player.name} выбил {number} и наступил на клетку {player.position}", "MiSans 40")
    utils.constants.main_window.after(4000, field, player)


def start_pos(player):
    text_on_center(f"Игрок {player.name} наступил на стартовую позицию", "MiSans 40")
    utils.constants.main_window.after(3000, new_move, utils.constants.next_player)


def random_bonus(player):
    clear()
    available_bonuses = 0
    for element in bonuses.keys():
        if bonuses[element] != 0:
            available_bonuses += bonuses[element]
    if available_bonuses == 0:
        utils.constants.fines["Money"] = 9
        utils.constants.fines["Transfer Window"] = 2
        utils.constants.fines["Vaccine"] = 2
        utils.constants.fines["Revive"] = 1
        utils.constants.fines["Charity Match"] = 1
    # chosen = choices(list(fines.keys()), weights=list(fines.values()))[0]
    chosen = "Money"
    if chosen == "Money":
        Money(player, type="Bonus")
    elif chosen == "Dead":
        Dead(player)


def random_fine(player):
    clear()
    available_fines = 0
    for element in fines.keys():
        if fines[element] != 0:
            available_fines += fines[element]
    if available_fines == 0:
        utils.constants.fines["Money"] = 9
        utils.constants.fines["Dead"] = 2
        utils.constants.fines["Strike"] = 2
        utils.constants.fines["Coronavirus"] = 3
    # chosen = choices(list(fines.keys()), weights=list(fines.values()))[0]
    chosen = "Money"
    if chosen == "Money":
        Money(player, type="Fine")
    elif chosen == "Dead":
        Dead(player)


class Dead:
    def __init__(self, player):
        self.player = player
        text_on_center(f'{self.player.name} выбил штраф "Смерть". Случайный поиск клуба...', "MiSans 40")
        utils.constants.main_window.after(5000, self.apply)

    def apply(self):
        self.clubs = self.player.search_owned_clubs()
        self.available_clubs = self.player.available_clubs("Dead")
        if not self.available_clubs:
            text_on_center("Нет доступных клубов. Штраф аннулируется", "MiSans 50")
            self.b_next_step = Button(utils.constants.main_window, text="Следующий ход", font="MiSans 30", command=lambda: new_move(utils.constants.next_player))
            self.b_next_step.place(x=800 - (self.b_next_step.winfo_reqwidth() / 2), y=700)
            return
        self.club = choice(self.available_clubs)
        text_on_center(f"Выбран клуб {self.club.name}", "MiSans 40")
        if self.club.manager is not None:
            text_on_center(f"В клубе {self.club.name} умирает менеджер {self.club.manager.name}", "MiSans 28")
            self.club.manager.die()
            self.b_info_personal = Button(utils.constants.main_window, text="Информация о менеджере", font="MiSans 30", command=nothing)
        elif self.club.coach is not None:
            text_on_center(f"В клубе {self.club.name} умирает тренер {self.club.coach.name}", "MiSans 30")
            self.club.coach.die()
            self.b_info_personal = Button(utils.constants.main_window, text="Информация о тренере", font="MiSans 30", command=nothing)
        elif self.club.footballer is not None:
            text_on_center(f"В клубе умирает футболист {self.club.footballer.name}", "MiSans 30")
            self.club.footballer.die()
            self.b_info_personal = Button(utils.constants.main_window, text="Информация о футболисте", font="MiSans 30", command=nothing)
        self.b_info_club = Button(utils.constants.main_window, text="Информация о клубе", font="MiSans 30", command=self.club.info)
        self.x_small = (1600 - self.b_info_personal.winfo_reqwidth()) // 2
        self.b_info_club.place(x=self.x_small // 2 - self.b_info_club.winfo_reqwidth() // 2, y=700)
        self.b_info_personal.place(x=800 - (self.b_info_personal.winfo_reqwidth() / 2), y=700)
        self.b_next_step = Button(utils.constants.main_window, text="Следующий ход", font="MiSans 30",
                                  command=lambda: new_move(utils.constants.next_player))
        self.b_next_step.place(x=(self.x_small + self.b_info_personal.winfo_reqwidth()) + (self.x_small - self.b_next_step.winfo_reqwidth()) // 2, y=700)


class Money:
    def __init__(self, player, type):
        self.player = player
        self.type = type
        self.available_items = False
        if self.type == "Fine":
            self.money_list = money_fines
        else:
            self.money_list = money_bonuses
        for element in self.money_list.keys():
            if self.money_list[element] != 0:
                self.available_items = True
        if not self.available_items and self.type == "Fine":
            utils.constants.money_fines[3000000] = 2
            utils.constants.money_fines[1500000] = 3
            utils.constants.money_fines[750000] = 4
        elif not self.available_items:
            utils.constants.money_bonuses[1500000] = 2
            utils.constants.money_bonuses[1000000] = 3
            utils.constants.money_bonuses[500000] = 4
        self.money = choices(list(self.money_list.keys()), weights=list(self.money_list.values()))[0]
        """self.money = 500000"""
        self.clear_money = self.money
        if self.type == "Fine":
            utils.constants.money_fines[self.money] -= 1
            self.money = self.player.summary_check(self.money, type="Minus")
            self.text = f"{self.player.name} попал на денежный штраф в размере {self.clear_money}. К оплате {self.money}"
        else:
            utils.constants.money_bonuses[self.money] -= 1
            self.money = self.player.summary_check(self.money, type="Plus")
            self.text = f"{self.player.name} попал на денежный бонус в размере {self.clear_money}. К пополнению {self.money}"
        text_on_center(self.text, "MiSans 30")
        utils.constants.main_window.after(4000, self.__apply__)

    def __apply__(self):
        if self.type == "Bonus":
            self.player.deposit(self.money, economist=False)
            text_on_center(f"Пополнение баланса. Баланс составляет {self.player.balance}", font="MiSans 40")
            utils.constants.main_window.after(4000, new_move, self.player)
            print(c_info(f"Cash bonus processed +{self.money}"))
        else:
            if self.player.balance >= self.money:
                self.player.withdrawal(self.money, economist=False)
                text_on_center(f"{self.player.name} оплатил штраф. Его баланс составляет {self.player.balance}", "MiSans 40")
                print(c_successful(f"Cash fine processed -{self.money}"))
                utils.constants.main_window.after(4000, new_move, self.player)
            else:
                text_on_center(f"{self.player.name} НЕ смог оплатить штраф. Ему не хватает {self.money - self.player.balance}", "MiSans 40")
                print(c_failed(f"The cash bonus has not been processed -{self.money}"))
                utils.constants.main_window.after(2000, Sell(self.player, False, False, self.__apply__, self.money))
