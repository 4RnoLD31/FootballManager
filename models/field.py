import random
import tkinter as tk
import models.save_game as save_game
import models.transfer_window as transfer_window
import models.highlighting as hg
import models.club as club
import models.match as match
import models.property as property
import utils.constants as const
import models.info as info
import models.panels as panels


class Field:
    @staticmethod
    def field(player):
        if player.position == 0:
            Field.start_pos(player)
        elif player.position == 1:
            Field.stepped_on(player, const.clubs["Barcelona"])
        elif player.position == 2 or player.position == 20:
            Field.random_bonus(player)
        elif player.position == 3:
            Field.stepped_on(player, const.clubs["Real Madrid"])
        elif player.position == 4:
            Field.stepped_on(player, const.TVs["Setanta Sports"])
        elif player.position == 5:
            Field.stepped_on(player, const.clubs["Atletico Madrid"])
        elif player.position == 6 or player.position == 16 or player.position == 22:
            transfer_window.TransferWindow(player)
        elif player.position == 7:
            Field.stepped_on(player, const.clubs["Arsenal"])
        elif player.position == 8:
            player.disqualified = True
            print(hg.info(f"Player {player.name} has been disqualified"))
            const.text_on_center(f"Игрок {player.name} наступил на дисквалификацию. Он пропустит 1 ход", font="MiSans 40")
            const.main_window.after(4000, Field.new_move)
        elif player.position == 9:
            Field.stepped_on(player, const.clubs["Liverpool"])
        elif player.position == 10:
            Field.stepped_on(player, const.clubs["Manchester City"])
        elif player.position == 11:
            Field.stepped_on(player, const.TVs["Euro Sports"])
        elif player.position == 12:
            Field.stepped_on(player, const.clubs["Bayern"])
        elif player.position == 13:
            Field.stepped_on(player, const.clubs["Borussia"])
        elif player.position == 14 or player.position == 30:
            Field.random_fine(player)
        elif player.position == 15:
            Field.stepped_on(player, const.clubs["Leipzig"])
        elif player.position == 17:
            Field.stepped_on(player, const.clubs["Juventus"])
        elif player.position == 18:
            Field.stepped_on(player, const.TVs["Rai Uno"])
        elif player.position == 19:
            Field.stepped_on(player, const.clubs["Inter"])
        elif player.position == 21:
            Field.stepped_on(player, const.clubs["Milan"])
        elif player.position == 23:
            Field.stepped_on(player, const.clubs["Krasnodar"])
        elif player.position == 24:
            if player.balance >= player.summary_check(1000000):
                const.text_on_center(f"Игрок {player.name} наступил на налоговую. Штраф 1000000", font="MiSans 40")
                player.withdrawal(1000000)
                const.main_window.after(4000, Field.new_move)
            else:
                const.text_on_center(f"Игрок {player.name} наступил на налоговую. Штраф 1000000\nОн не может выплатить штраф. Ему нехватает {player.summary_check(1000000) - player.balance}", font="MiSans 40")
                const.main_window.after(4000, lambda: property.Sell(player, Field.new_move, need_money=1000000))
        elif player.position == 25:
            Field.stepped_on(player, const.clubs["Spartak Moscow"])
        elif player.position == 26:
            Field.stepped_on(player, const.clubs["CSKA"])
        elif player.position == 27:
            Field.stepped_on(player, const.TVs["ESPN"])
        elif player.position == 28:
            Field.stepped_on(player, const.clubs["Al-Nassr"])
        elif player.position == 29:
            Field.stepped_on(player, const.clubs["Al-Ittihad"])
        elif player.position == 31:
            Field.stepped_on(player, const.clubs["Al-Hilal"])

    @staticmethod
    def stepped_on(player, object):
        if object.owner == player:
            const.text_on_center(f"{player.name} наступил на свой объект {object.name}", "MiSans 40")
            const.main_window.after(4000, Field.new_move)
        elif object.owner is None:
            if player.balance >= player.summary_check(object.price):
                const.text_on_center(f"{player.name} наступил на свободный объект {object.name}. Хочешь купить его?", "MiSans 30")
            else:
                const.text_on_center(f"{player.name} наступил на свободный объект {object.name}. Недостаточно средств для покупки. Нужно еще {player.summary_check(object.price) - player.balance}. Хочешь купить его?", "MiSans 30")
            b_info = tk.Button(const.main_window, text="Информация о объекте", font="MiSans 30", command=lambda: info.Info(object))
            b_info.place(x=50, y=700)
            b_buy = tk.Button(const.main_window, text="Купить", font="MiSans 30", command=lambda: property.OtherBuy(player, object, lambda: Field.stepped_on(player, object)))
            b_buy.place(x=800 - (b_buy.winfo_reqwidth() / 2), y=700)
            b_next_step = tk.Button(const.main_window, text="Следующий ход", font="MiSans 30", command=lambda: Field.new_move())
            b_next_step.place(x=1200, y=700)
        else:
            if isinstance(object, club.Club):
                const.text_on_center(f"{player.name} наступил на клуб {object.name}. Им владеет {object.owner.name}", "MiSans 40")
                const.main_window.after(4000, match.Match, object)
            else:
                const.text_on_center(f"{player.name} наступил на телекомпанию {object.name}. Им владеет {object.owner.name}", "MiSans 40")
                const.main_window.after(4000, object.get_gain, player)

    @staticmethod
    def clubs_with_cooldown():
        list = []
        for element in const.clubs.values():
            if element.cooldown is not None:
                list.append(element)
        return list

    @staticmethod
    def footballers_with_flu():
        list = []
        for element in const.footballers.values():
            if element.flu is not None:
                list.append(element)
        return list

    @staticmethod
    def coaches_with_flu():
        list = []
        for element in const.coaches.values():
            if element.flu is not None:
                list.append(element)
        return list

    @staticmethod
    def coaches_with_strike():
        list = []
        for element in const.coaches.values():
            if element.strike is not None:
                list.append(element)
        return list

    @staticmethod
    def managers_with_flu():
        list = []
        for element in const.managers.values():
            if element.flu is not None:
                list.append(element)
        return list

    @staticmethod
    def new_move(*args):
        if const.queue:
            const.queue[0]()
            return
        player = None
        if const.number is None:
            const.number = random.randint(2, 12)
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
        if Field.clubs_with_cooldown():
            for element in Field.clubs_with_cooldown():
                if element.cooldown == 1 and element.owner == player:
                    element.cooldown = None
                elif element.owner == player:
                    element.cooldown -= 1
        if Field.footballers_with_flu():
            for element in Field.footballers_with_flu():
                if element.flu == 1 and element.owner == player:
                    element.flu = None
                elif element.owner == player:
                    element.flu -= 1
        if Field.coaches_with_flu():
            for element in Field.coaches_with_flu():
                if element.flu == 1 and element.owner == player:
                    element.flu = None
                elif element.owner == player:
                    element.flu -= 1
        if Field.coaches_with_strike():
            for element in Field.coaches_with_strike():
                if element.strike == 1 and element.owner == player:
                    element.strike = None
                elif element.owner == player:
                    element.strike -= 1
        if Field.managers_with_flu():
            for element in Field.managers_with_flu():
                if element.flu == 1 and element.owner == player:
                    element.flu = None
                elif element.owner == player:
                    element.flu -= 1
        const.clear()
        # number = 2
        player.numbers_thrown += const.number
        player.throws += 1
        if player.position + const.number > 31:
            player.position = player.position + const.number - 31
            player.circle()
        else:
            player.position += const.number
        const.text_on_center("Бросаю куб...", font="MiSans 50")
        const.main_window.after(2000, const.nothing)
        const.text_on_center(f"Игрок {player.name} выбил {const.number} и наступил на клетку {player.position}", "MiSans 35")
        const.number = None
        const.main_window.after(4000, Field.field, player)

    @staticmethod
    def start_pos(player):
        const.text_on_center(f"Игрок {player.name} наступил на стартовую позицию", "MiSans 40")
        const.main_window.after(4000, Field.new_move, const.next_player)

    @staticmethod
    def random_bonus(player):
        const.clear()
        available_bonuses = 0
        for element in const.bonuses.keys():
            if const.bonuses[element] != 0:
                available_bonuses += const.bonuses[element]
        if available_bonuses == 0:
            const.bonuses["Money"] = 9
            const.bonuses["Transfer Window"] = 2
            const.bonuses["Vaccine"] = 2
            const.bonuses["Revive"] = 1
            const.bonuses["Charity Match"] = 1
        chosen = random.choices(list(const.bonuses.keys()), weights=list(const.bonuses.values()))[0]
        const.bonuses[chosen] -= 1
        if chosen == "Money":
            Money(player, type="Bonus")
        elif chosen == "Transfer Window":
            TransferWindow(player)
        elif chosen == "Vaccine":
            Vaccine(player)
        elif chosen == "Revive":
            Revive(player)
        elif chosen == "Charity Match":
            CharityMatch(player)

    @staticmethod
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
        chosen = random.choices(list(const.fines.keys()), weights=list(const.fines.values()))[0]
        const.fines[chosen] -= 1
        if chosen == "Money":
            Money(player, type="Fine")
        elif chosen == "Dead":
            Dead(player)
        elif chosen == "Strike":
            Strike(player)
        elif chosen == "Coronavirus":
            Coronavirus(player)


class CharityMatch:
    def __init__(self, player):
        self.player = player
        self.player.bonuses["Charity Match"] += 1
        const.text_on_center(f"{self.player.name} получил бонус благотворительного матча", "MiSans 40")
        panels.panels_initialize()
        const.main_window.after(4000, Field.new_move)


class Revive:
    def __init__(self, player):
        self.player = player
        self.player.bonuses["Revive"] += 1
        const.text_on_center(f"{self.player.name} получил бонус воскрешения", "MiSans 40")
        panels.panels_initialize()
        const.main_window.after(4000, Field.new_move)


class Vaccine:
    def __init__(self, player):
        self.player = player
        self.player.bonuses["Vaccine"] += 1
        const.text_on_center(f"{self.player.name} получил бонус вакцины", "MiSans 40")
        panels.panels_initialize()
        const.main_window.after(4000, Field.new_move)


class TransferWindow:
    def __init__(self, player):
        self.player = player
        self.player.bonuses["Transfer Window"] += 1
        const.text_on_center(f"{self.player.name} получил бонус трансферного окна", "MiSans 40")
        panels.panels_initialize()
        const.main_window.after(4000, Field.new_move)


class Dead:
    def __init__(self, player):
        self.player = player
        const.text_on_center(f'{self.player.name} выбил штраф "Смерть"', "MiSans 40")
        const.main_window.after(5000, self.__first__)

    def __first__(self):
        const.clear()
        self.all_managers = self.player.search_bought_managers()
        self.managers = []
        for element in self.all_managers:
            if element.flu is None:
                self.managers.append(element)
        if not self.managers:
            self.all_coaches = self.player.search_bought_coaches()
            self.coaches = []
            for element in self.all_coaches:
                if element.flu is None:
                    self.coaches.append(element)
            if not self.coaches:
                self.all_footballers = self.player.search_bought_footballers()
                self.footballers = []
                for element in self.all_footballers:
                    if element.flu is None:
                        self.footballers.append(element)
                if not self.footballers:
                    const.text_on_center("Нет персонала. Пропуск штрафа", "MiSans 50")
                    const.main_window.after(4000, Field.new_move)
                else:
                    const.text_on_center(f"У игрока {self.player.name} куплен только футболист", "MiSans 40")
                    self.items = self.footballers
            else:
                const.text_on_center(f"У игрока {self.player.name} куплен тренер", "MiSans 40")
                self.items = self.coaches
        else:
            const.text_on_center(f"У игрока {self.player.name} куплен менеджер", "MiSans 40")
            self.items = self.managers
        const.main_window.after(4000, self.__second__)

    def __second__(self):
        self.picked = random.choice(self.items)
        self.picked.die()
        const.text_on_center(f"Умер персонал {self.picked.name}", "MiSans 40")
        self.b_info_personal = tk.Button(const.main_window, text="Информация о персонале", font="MiSans 30", command=lambda: info.Info(self.picked))
        self.b_info_personal.place(x=400 - (self.b_info_personal.winfo_reqwidth() / 2), y=700)
        self.b_next_step = tk.Button(const.main_window, text="Следующий ход", font="MiSans 30", command=Field.new_move)
        self.b_next_step.place(x=1200 - self.b_next_step.winfo_reqwidth() / 2, y=700)


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
            const.main_window.after(4000, Field.new_move, self.player)
            print(hg.info(f"Cash bonus processed +{self.money}"))
        else:
            if self.player.balance >= self.money:
                self.player.withdrawal(self.money, economist=False)
                const.text_on_center(f"{self.player.name} оплатил штраф. Его баланс составляет {self.player.balance}", "MiSans 40")
                print(hg.successful(f"Cash fine processed -{self.money}"))
                const.main_window.after(4000, Field.new_move, self.player)
            else:
                const.text_on_center(f"{self.player.name} не смог оплатить штраф. Ему не хватает {self.money - self.player.balance}", "MiSans 40")
                print(hg.failed(f"Cash fine has not been processed -{self.money}"))
                const.main_window.after(2000, lambda: property.Sell(self.player, self.__apply__, need_money=self.money))


class Strike:
    def __init__(self, player):
        self.player = player
        const.text_on_center(f"{self.player.name} получил штраф забастовка", "MiSans 50")
        const.main_window.after(4000, self.__first__)

    def __first__(self):
        const.clear()
        self.all_coaches = self.player.search_bought_coaches()
        self.coaches = []
        for element in self.all_coaches:
            if element.strike is None:
                self.coaches.append(element)
        if self.coaches:
            self.y = 100
            self.l_name = tk.Label(const.main_window, text=f"{self.player.name} выберите тренера для забастовки", font="MiSans 40")
            self.l_name.place(x=800 - self.l_name.winfo_reqwidth() / 2, y=0)
            self.radio_coaches = []
            self.var = tk.IntVar()
            self.var.set(-1)
            for element in range(0, len(self.coaches)):
                self.radio_coaches.append(tk.Radiobutton(text=self.coaches[element].name, variable=self.var, value=element, command=self.__second__, font="MiSans 30"))
                self.radio_coaches[element].place(x=20, y=self.y)
                self.y += 55
        else:
            const.text_on_center("Нет доступных тренеров. Пропуск", "MiSans 40")
            const.main_window.after(4000, Field.new_move)

    def __second__(self):
        self.picked_coach = self.coaches[self.var.get()]
        self.b_info_about_coach = tk.Button(const.main_window, text="Информация о тренере", font="MiSans 30", command=lambda: info.Info(self.picked_coach))
        self.b_info_about_coach.place(x=400 - self.b_info_about_coach.winfo_reqwidth() / 2, y=600)
        self.b_continue = tk.Button(const.main_window, text="Продолжить", font="MiSans 30", command=self.__third__)
        self.b_continue.place(x=1200 - self.b_continue.winfo_reqwidth() / 2, y=600)

    def __third__(self):
        self.picked_coach.strike = 10
        const.text_on_center(f"Тренер {self.picked_coach.name} в забастовке на 10 ходов", "MiSans 50")
        const.main_window.after(4000, Field.new_move)


class Coronavirus:
    def __init__(self, player):
        self.player = player
        const.text_on_center(f"{self.player.name} получил штраф коронавирус", "MiSans 50")
        const.main_window.after(4000, self.__first__)

    def __first__(self):
        const.clear()
        self.all_managers = self.player.search_bought_managers()
        self.managers = []
        for element in self.all_managers:
            if element.flu is None:
                self.managers.append(element)
        if not self.managers:
            self.all_coaches = self.player.search_bought_coaches()
            self.coaches = []
            for element in self.all_coaches:
                if element.flu is None:
                    self.coaches.append(element)
            if not self.coaches:
                self.all_footballers = self.player.search_bought_footballers()
                self.footballers = []
                for element in self.all_footballers:
                    if element.flu is None:
                        self.footballers.append(element)
                if not self.footballers:
                    const.text_on_center("Нет персонала. Пропуск штрафа", "MiSans 50")
                    const.main_window.after(4000, Field.new_move)
                else:
                    self.l_name = tk.Label(const.main_window, text=f"{self.player.name} выберите футболиста для болезни", font="MiSans 40")
                    self.items = self.footballers
            else:
                self.l_name = tk.Label(const.main_window, text=f"{self.player.name} выберите тренера для болезни", font="MiSans 40")
                self.items = self.coaches
        else:
            self.l_name = tk.Label(const.main_window, text=f"{self.player.name} выберите менеджера для болезни", font="MiSans 40")
            self.items = self.managers
        self.y = 100
        self.l_name.place(x=800 - self.l_name.winfo_reqwidth() / 2, y=0)
        self.radio = []
        self.var = tk.IntVar()
        self.var.set(-1)
        for element in range(0, len(self.items)):
            self.radio.append(tk.Radiobutton(text=self.items[element].name, variable=self.var, value=element, command=self.__second__, font="MiSans 30"))
            self.radio[element].place(x=20, y=self.y)
            self.y += 55

    def __second__(self):
        self.picked = self.items[self.var.get()]
        self.b_info_about = tk.Button(const.main_window, text="Информация о персонале", font="MiSans 30", command=lambda: info.Info(self.picked))
        self.b_info_about.place(x=400 - self.b_info_about.winfo_reqwidth() / 2, y=600)
        self.b_continue = tk.Button(const.main_window, text="Продолжить", font="MiSans 30", command=self.__third__)
        self.b_continue.place(x=1200 - self.b_continue.winfo_reqwidth() / 2, y=600)

    def __third__(self):
        self.picked.flu = 10
        const.text_on_center(f"Персонал {self.picked.name} заболел на 10 ходов", "MiSans 50")
        const.main_window.after(4000, Field.new_move)
