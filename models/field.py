import utils.constants
from utils.constants import *
from models.stepped_club import SteppedClub
from models.property import Property
from random import choice, choices


class Field:
    def __init__(self, player):
        self.player = player
        if self.player.position == 1:
            SteppedClub(self.player, clubs["Барселона"])
        elif self.player.position == 14 or self.player.position == 30:
            self.fine = RandomFine(self.player)

class NewMove:
    def __init__(self, player):
        self.player = player
        print(self.player)
        if self.player == utils.constants.PL1:
            utils.constants.next_player = utils.constants.PL2
            print("1", utils.constants.next_player)
        elif self.player == utils.constants.PL2:
            utils.constants.next_player = utils.constants.PL1
            print("2", utils.constants.next_player)
        clear()
        # self.number = randint(2, 12)
        self.number = 14
        self.player.numbers_thrown += self.number
        self.player.throws += 1
        if self.player.position + self.number > 31:
            self.player.position = self.player.position + self.number - 31
        else:
            self.player.position += self.number
        text_on_center("Бросаю куб...", font="MiSans 50")
        main_window.after(2000, lambda: print("Новый ход игрока", self.player.name))
        text_on_center("Игрок " + self.player.name + " выбил " +
                       str(self.number) + " и наступил на клетку " + str(self.player.position), "MiSans 40")
        main_window.after(4000, lambda: Field(self.player))


class RandomFine:
    def __init__(self, player):
        clear()
        self.player = player
        self.available_fines = 0
        for element in fines.keys():
            if fines[element] != 0:
                self.available_fines += fines[element]
        print(self.available_fines)
        if self.available_fines == 0:
            utils.constants.fines["Money"] = 9
            utils.constants.fines["Dead"] = 2
            utils.constants.fines["Strike"] = 2
            utils.constants.fines["Coronavirus"] = 3
        # self.chosen = choices(list(fines.keys()), weights=list(fines.values()))[0]
        self.chosen = "Money"
        if self.chosen == "Money":
            self.fine = Money(self.player)
        elif self.chosen == "Dead":
            self.fine = Dead(self.player)


class Dead:
    def __init__(self, player):
        self.player = player
        text_on_center(self.player.name + ' выбил штраф "Смерть". Случайный поиск клуба...', "MiSans 40")
        main_window.after(5000, lambda: self.apply())


    def apply(self):
        self.clubs = self.player.search_owned_clubs()
        self.available_clubs = self.player.available_clubs("Dead")
        if not self.available_clubs:
            text_on_center("Нет доступных клубов. Штраф аннулируется", "MiSans 50")
            self.b_next_step = Button(main_window, text="Следующий ход", font="MiSans 30", command=lambda: NewMove(utils.constants.next_player))
            self.b_next_step.place(x=800 - (self.b_next_step.winfo_reqwidth() / 2), y=700)
            return
        self.club = choice(self.available_clubs)
        text_on_center("Выбран клуб " + self.club.name, "MiSans 40")
        if self.club.manager is not None:
            text_on_center("В клубе " + self.club.name + " умирает менеджер " + self.club.manager.name, "MiSans 28")
            self.club.manager.die()
            self.b_info_personal = Button(main_window, text="Информация о менеджере", font="MiSans 30", command=lambda: print())
        elif self.club.coach is not None:
            text_on_center("В клубе " + self.club.name + " умирает тренер " + self.club.coach.name, "MiSans 30")
            self.club.coach.die()
            self.b_info_personal = Button(main_window, text="Информация о тренере", font="MiSans 30", command=lambda: print())
        elif self.club.footballer is not None:
            text_on_center("В клубе " + self.club.name + " умирает футболист " + self.club.footballer.name, "MiSans 30")
            self.club.footballer.die()
            self.b_info_personal = Button(main_window, text="Информация о футболисте", font="MiSans 30", command=lambda: print())
        self.b_info_club = Button(main_window, text="Информация о клубе", font="MiSans 30", command=self.club.info)
        self.x_small = (1600 - self.b_info_personal.winfo_reqwidth()) // 2
        self.b_info_club.place(x=self.x_small // 2 - self.b_info_club.winfo_reqwidth() // 2, y=700)
        self.b_info_personal.place(x=800 - (self.b_info_personal.winfo_reqwidth() / 2), y=700)
        self.b_next_step = Button(main_window, text="Следующий ход", font="MiSans 30",
                                      command=lambda: NewMove(utils.constants.next_player))
        self.b_next_step.place(x=(self.x_small + self.b_info_personal.winfo_reqwidth()) + (self.x_small - self.b_next_step.winfo_reqwidth()) // 2, y=700)


class Money:
    def __init__(self, player):
        self.player = player
        self.available_fines = 0
        for element in money_fines.keys():
            if money_fines[element] != 0:
                self.available_fines += money_fines[element]
        if self.available_fines == 0:
            utils.constants.money_fines[3000] = 2
            utils.constants.money_fines[1500] = 3
            utils.constants.money_fines[750] = 4
        self.money_fine = choices(list(money_fines.keys()), weights=list(money_fines.values()))[0]
        money_fines[self.money_fine] -= 1
        self.money_fine = 5000000
        if self.player.economist_level() != 0:
            self.clear_money_fine = self.money_fine
            self.money_fine = self.player.check_balance(self.money_fine)
            self.text = self.player.name + " попал на денежный штраф в размере " + str(self.clear_money_fine) + ". К оплате " + str(self.money_fine)
            text_on_center(self.text, "MiSans 30")
        else:
            self.text = self.player.name + " попал на денежный штраф в размере " + str(self.money_fine)
            text_on_center(self.text, "MiSans 40")
        main_window.after(4000, self.__apply__)

    def __apply__(self):
        if self.player.balance >= self.money_fine:
            self.player.withdrawal(self.money_fine, economist=False)
            text_on_center(
                self.player.name + " оплатил штраф. Его баланс составляет " + str(self.player.balance),
                "MiSans 40")
            print("Успешная операция -", self.money_fine)
        else:
            text_on_center(
                self.player.name + " НЕ смог оплатить штраф. Ему не хватает " + str(
                    self.money_fine - self.player.balance),
                "MiSans 40")
            print("Неудачная операция -", self.money_fine)
            main_window.after(2000, Property(self.player, False, 2, self.money_fine, self.__apply__))
