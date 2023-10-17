import models.field
import utils.constants
from utils.constants import *

def stepped_club(player, club):
    if club.owner == player:
        text_on_center(player.name + " наступил на свой клуб " + club.name, "MiSans 40")
        print(utils.constants.next_player.name)
        b_info = Button(main_window, text="Информация о клубе", font="MiSans 30", command=club.info)
        b_info.place(x=350, y=700)
        b_next_step = Button(main_window, text="Следующий ход", font="MiSans 30", command=lambda: models.field.new_move(utils.constants.next_player))
        b_next_step.place(x=950, y=700)
        return
    elif club.owner is None:
        text_on_center(player.name + " наступил на не купленный клуб " + club.name + ". Хочешь купить его?", "MiSans 30")
        b_info = Button(main_window, text="Информация о клубе", font="MiSans 30", command=club.info)
        b_info.place(x=50, y=700)
        b_buy = Button(main_window, text="Купить", font="MiSans 30", command=lambda: print())
        b_buy.place(x=800 - (b_buy.winfo_reqwidth() / 2), y=700)
        b_next_step = Button(main_window, text="Следующий ход", font="MiSans 30",
                                  command=lambda: models.field.new_move(utils.constants.next_player))
        b_next_step.place(x=1200, y=700)
    else:
        text_on_center(player.name + " наступил на клуб " + club.name + ". Им владеет " + club.owner.name, "MiSans 40")


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




