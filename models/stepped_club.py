import models.field
import utils.constants
from utils.constants import *

class SteppedClub:
    def __init__(self, player, club):
        self.player = player
        self.club = club
        if self.club.owner == self.player:
            text_on_center(self.player.name + " наступил на свой клуб " + self.club.name, "MiSans 40")
            print(utils.constants.next_player.name)
            self.b_info = Button(main_window, text="Информация о клубе", font="MiSans 30", command=self.club.info)
            self.b_info.place(x=350, y=700)
            self.b_next_step = Button(main_window, text="Следующий ход", font="MiSans 30", command=lambda: models.field.NewMove(utils.constants.next_player))
            self.b_next_step.place(x=950, y=700)
            return
        elif self.club.owner is None:
            text_on_center(self.player.name + " наступил на не купленный клуб " + self.club.name + ". Хочешь купить его?", "MiSans 30")
            self.b_info = Button(main_window, text="Информация о клубе", font="MiSans 30", command=self.club.info)
            self.b_info.place(x=50, y=700)
            self.b_buy = Button(main_window, text="Купить", font="MiSans 30", command=lambda: print())
            self.b_buy.place(x=800 - (self.b_buy.winfo_reqwidth() / 2), y=700)
            self.b_next_step = Button(main_window, text="Следующий ход", font="MiSans 30",
                                      command=lambda: models.field.NewMove(utils.constants.next_player))
            self.b_next_step.place(x=1200, y=700)
        else:
            text_on_center(self.player.name + " наступил на клуб " + self.club.name + ". Им владеет " + self.club.owner.name, "MiSans 40")


class Match:
    def __init__(self, first_club):
        self.first_club = first_club
        if self.first_club.available() is True:
            text_on_center("Клуб игрока " + self.first_club.owner.name + " доступен для игры", "MiSans 40")
        else:
            text_on_center("Клуб игрока " + self.first_club.owner.name + " НЕ доступен для игры", "MiSans 40")
        main_window.after(3000, nothing)
        self.versus_player = utils.constants.next_player
        self.available_clubs = self.versus_player.available_clubs()
        if not self.available_clubs:
            text_on_center("У игрока " + self.versus_player.name + " нет доступных клубов для игры", "MiSans 40")
        else:
            clear()




