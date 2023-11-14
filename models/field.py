import random
import utils.constants as const
import tkinter as tk
import models.stepped as stepped
import models.property as property
import models.save_game as save_game
import models.transfer_window as transfer_window
import models.highlighting as hg


def field(player):
    if player.position == 0:
        start_pos(player)
    elif player.position == 1:
        stepped.stepped_on_club(player, const.clubs["Barcelona"])
    elif player.position == 2 or player.position == 20:
        random_bonus(player)
    elif player.position == 3:
        stepped.stepped_on_club(player, const.clubs["Real Madrid"])
    elif player.position == 4:
        stepped.stepped_on_tv_company(player, const.TVs["Setanta Sports"])
    elif player.position == 5:
        stepped.stepped_on_club(player, const.clubs["Atletico Madrid"])
    elif player.position == 6 or player.position == 16 or player.position == 22:
        transfer_window.TransferWindow(player)
    elif player.position == 7:
        stepped.stepped_on_club(player, const.clubs["Arsenal"])
    elif player.position == 8:
        player.disqualified = True
        print(hg.info(f"Player {player.name} has been disqualified"))
        const.text_on_center(f"Игрок {player.name} наступил на дисквалификацию. Он пропустит 1 ход", font="MiSans 40")
        const.main_window.after(4000, new_move)
    elif player.position == 9:
        stepped.stepped_on_club(player, const.clubs["Liverpool"])
    elif player.position == 10:
        stepped.stepped_on_club(player, const.clubs["Manchester City"])
    elif player.position == 11:
        stepped.stepped_on_tv_company(player, const.TVs["Euro Sports"])
    elif player.position == 12:
        stepped.stepped_on_club(player, const.clubs["Bayern"])
    elif player.position == 13:
        stepped.stepped_on_club(player, const.clubs["Borussia"])
    elif player.position == 14 or player.position == 30:
        random_fine(player)
    elif player.position == 15:
        stepped.stepped_on_club(player, const.clubs["Leipzig"])
    elif player.position == 17:
        stepped.stepped_on_club(player, const.clubs["Juventus"])
    elif player.position == 18:
        stepped.stepped_on_tv_company(player, const.TVs["Rai Uno"])
    elif player.position == 19:
        stepped.stepped_on_club(player, const.clubs["Inter"])
    elif player.position == 21:
        stepped.stepped_on_club(player, const.clubs["Milan"])
    elif player.position == 23:
        stepped.stepped_on_club(player, const.clubs["Krasnodar"])
    elif player.position == 24:
        if player.balance >= player.summary_check(1000000):
            const.text_on_center(f"Игрок {player.name} наступил на налоговую. Штраф 1000000", font="MiSans 40")
            const.main_window.after(4000, new_move)
        else:
            const.text_on_center(f"Игрок {player.name} наступил на налоговую. Штраф 1000000\nОн не может выплатить штраф. Ему нехватает {player.summary_check(1000000) - player.balance}", font="MiSans 40")
            const.main_window.after(4000, lambda: property.Sell(player, new_move, need_money=1000000))



def new_move(*args):
    player = None
    save_game.save_game()
    if const.next_player == const.PL1:
        player = const.next_player
        const.next_player = const.PL2
    elif const.next_player == const.PL2:
        player = const.next_player
        const.next_player = const.PL1
    if player.disqualified and const.next_player.disqualified:
        print(hg.info("Both players have disqualified already. Canceling disqualifications"))
        player.disqualified = False
        const.next_player.disqualified = False
    elif player.disqualified:
        player.disqualified = False
        player = const.next_player
    const.clear()
    # number = randint(2, 12)
    number = 24
    player.numbers_thrown += number
    player.throws += 1
    if player.position + number > 31:
        player.position = player.position + number - 31
    else:
        player.position += number
    const.text_on_center("Бросаю куб...", font="MiSans 50")
    const.main_window.after(2000, const.nothing)
    const.text_on_center(f"Игрок {player.name} выбил {number} и наступил на клетку {player.position}", "MiSans 35")
    const.main_window.after(4000, field, player)


def start_pos(player):
    const.text_on_center(f"Игрок {player.name} наступил на стартовую позицию", "MiSans 40")
    const.main_window.after(4000, new_move, const.next_player)


def random_bonus(player):
    const.clear()
    available_bonuses = 0
    for element in const.bonuses.keys():
        if const.bonuses[element] != 0:
            available_bonuses += const.bonuses[element]
    if available_bonuses == 0:
        const.fines["Money"] = 9
        const.fines["Transfer Window"] = 2
        const.fines["Vaccine"] = 2
        const.fines["Revive"] = 1
        const.fines["Charity Match"] = 1
    # chosen = choices(list(const.fines.keys()), weights=list(const.fines.values()))[0]
    chosen = "Money"
    if chosen == "Money":
        Money(player, type="Bonus")
    elif chosen == "Dead":
        Dead(player)


def random_fine(player):
    const.clear()
    available_fines = 0
    for element in const.fines.keys():
        if const.fines[element] != 0:
            available_fines += const.fines[element]
    if available_fines == 0:
        const.fines["Money"] = 9
        const.fines["Dead"] = 2
        const.fines["Strike"] = 2
        const.fines["Coronavirus"] = 3
    # chosen = choices(list(const.fines.keys()), weights=list(const.fines.values()))[0]
    chosen = "Money"
    if chosen == "Money":
        Money(player, type="Fine")
    elif chosen == "Dead":
        Dead(player)


class Dead:
    def __init__(self, player):
        self.player = player
        const.text_on_center(f'{self.player.name} выбил штраф "Смерть". Случайный поиск клуба...', "MiSans 40")
        const.main_window.after(5000, self.apply)

    def apply(self):
        self.clubs = self.player.search_owned_const.clubs()
        self.available_clubs = self.player.available_const.clubs("Dead")
        if not self.available_clubs:
            const.text_on_center("Нет доступных клубов. Штраф аннулируется", "MiSans 50")
            self.b_next_step = tk.Button(const.main_window, text="Следующий ход", font="MiSans 30", command=lambda: new_move())
            self.b_next_step.place(x=800 - (self.b_next_step.winfo_reqwidth() / 2), y=700)
            return
        self.club = random.choice(self.available_clubs)
        const.text_on_center(f"Выбран клуб {self.club.name}", "MiSans 40")
        if self.club.manager is not None:
            const.text_on_center(f"В клубе {self.club.name} умирает менеджер {self.club.manager.name}", "MiSans 28")
            self.club.manager.die()
            self.b_info_personal = tk.Button(const.main_window, text="Информация о менеджере", font="MiSans 30", command=const.nothing)
        elif self.club.coach is not None:
            const.text_on_center(f"В клубе {self.club.name} умирает тренер {self.club.coach.name}", "MiSans 30")
            self.club.coach.die()
            self.b_info_personal = tk.Button(const.main_window, text="Информация о тренере", font="MiSans 30", command=const.nothing)
        elif self.club.footballer is not None:
            const.text_on_center(f"В клубе умирает футболист {self.club.footballer.name}", "MiSans 30")
            self.club.footballer.die()
            self.b_info_personal = tk.Button(const.main_window, text="Информация о футболисте", font="MiSans 30", command=const.nothing)
        self.b_info_club = tk.Button(const.main_window, text="Информация о клубе", font="MiSans 30", command=self.club.info)
        self.x_small = (1600 - self.b_info_personal.winfo_reqwidth()) // 2
        self.b_info_club.place(x=self.x_small // 2 - self.b_info_club.winfo_reqwidth() // 2, y=700)
        self.b_info_personal.place(x=800 - (self.b_info_personal.winfo_reqwidth() / 2), y=700)
        self.b_next_step = tk.Button(const.main_window, text="Следующий ход", font="MiSans 30", command=lambda: new_move())
        self.b_next_step.place(x=(self.x_small + self.b_info_personal.winfo_reqwidth()) + (self.x_small - self.b_next_step.winfo_reqwidth()) // 2, y=700)


class Money:
    def __init__(self, player, type):
        self.player = player
        self.type = type
        self.available_items = False
        if self.type == "Fine":
            self.money_list = const.money_fines
        else:
            self.money_list = const.money_bonuses
        for element in self.money_list.keys():
            if self.money_list[element] != 0:
                self.available_items = True
        if not self.available_items and self.type == "Fine":
            const.money_fines[3000000] = 2
            const.money_fines[1500000] = 3
            const.money_fines[750000] = 4
        elif not self.available_items:
            const.money_bonuses[1500000] = 2
            const.money_bonuses[1000000] = 3
            const.money_bonuses[500000] = 4
        self.money = random.choices(list(self.money_list.keys()), weights=list(self.money_list.values()))[0]
        """self.money = 500000"""
        self.clear_money = self.money
        if self.type == "Fine":
            const.money_fines[self.money] -= 1
            self.money = self.player.summary_check(self.money, type="Minus")
            self.text = f"{self.player.name} попал на денежный штраф в размере {self.clear_money}. К оплате {self.money}"
        else:
            const.money_bonuses[self.money] -= 1
            self.money = self.player.summary_check(self.money, type="Plus")
            self.text = f"{self.player.name} попал на денежный бонус в размере {self.clear_money}. К пополнению {self.money}"
        const.text_on_center(self.text, "MiSans 30")
        const.main_window.after(4000, self.__apply__)

    def __apply__(self):
        if self.type == "Bonus":
            self.player.deposit(self.money, economist=False)
            const.text_on_center(f"Пополнение баланса. Баланс составляет {self.player.balance}", font="MiSans 40")
            const.main_window.after(4000, new_move, self.player)
            print(hg.info(f"Cash bonus processed +{self.money}"))
        else:
            if self.player.balance >= self.money:
                self.player.withdrawal(self.money, economist=False)
                const.text_on_center(f"{self.player.name} оплатил штраф. Его баланс составляет {self.player.balance}", "MiSans 40")
                print(hg.successful(f"Cash fine processed -{self.money}"))
                const.main_window.after(4000, new_move, self.player)
            else:
                const.text_on_center(f"{self.player.name} НЕ смог оплатить штраф. Ему не хватает {self.money - self.player.balance}", "MiSans 40")
                print(hg.failed(f"The cash bonus has not been processed -{self.money}"))
                const.main_window.after(2000, property.Sell(self.player, False, False, self.__apply__, self.money))
