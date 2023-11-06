import models.field
import utils.constants
from utils.constants import *


def stepped_on_club(player, club):
    if club.owner == player:
        text_on_center(f"{player.name} наступил на свой клуб {club.name}", "MiSans 40")
        b_info = Button(utils.constants.main_window, text="Информация о клубе", font="MiSans 30", command=club.info)
        b_info.place(x=350, y=700)
        b_next_step = Button(utils.constants.main_window, text="Следующий ход", font="MiSans 30", command=lambda: models.field.new_move(utils.constants.next_player))
        b_next_step.place(x=950, y=700)
        return
    elif club.owner is None:
        text_on_center(f"{player.name} наступил на свободный клуб {club.name}. Хочешь купить его?", "MiSans 30")
        b_info = Button(utils.constants.main_window, text="Информация о клубе", font="MiSans 30", command=club.info)
        b_info.place(x=50, y=700)
        b_buy = Button(utils.constants.main_window, text="Купить", font="MiSans 30", command=nothing)
        b_buy.place(x=800 - (b_buy.winfo_reqwidth() / 2), y=700)
        b_next_step = Button(utils.constants.main_window, text="Следующий ход", font="MiSans 30",
                             command=lambda: models.field.new_move(utils.constants.next_player))
        b_next_step.place(x=1200, y=700)
    else:
        text_on_center(f"{player.name} наступил на клуб {club.name}. Им владеет {club.owner.name}", "MiSans 40")


def stepped_on_tv_company(player, tv_company):
    if tv_company.owner == player:
        text_on_center(f"{player.name} наступил на свою телекомпанию {tv_company.name}", "MiSans 35")
        b_info = Button(utils.constants.main_window, text="Информация о телекомпании", font="MiSans 30", command=nothing)
        b_info.place(x=350, y=700)
        b_next_step = Button(utils.constants.main_window, text="Следующий ход", font="MiSans 30", command=lambda: models.field.new_move(utils.constants.next_player))
        b_next_step.place(x=950, y=700)
        return
    elif tv_company.owner is None:
        text_on_center(f"{player.name} наступил на свободную телекомпанию {tv_company.name}. Хочешь купить ее?", "MiSans 30")
        b_info = Button(utils.constants.main_window, text="Информация о телекомпании", font="MiSans 30", command=nothing)
        b_info.place(x=50, y=700)
        b_buy = Button(utils.constants.main_window, text="Купить", font="MiSans 30", command=nothing)
        b_buy.place(x=800 - (b_buy.winfo_reqwidth() / 2), y=700)
        b_next_step = Button(utils.constants.main_window, text="Следующий ход", font="MiSans 30",
                             command=lambda: models.field.new_move(utils.constants.next_player))
        b_next_step.place(x=1200, y=700)
    else:
        text_on_center(f"{player.name} наступил на телекомпанию {tv_company.name}. Им владеет {tv_company.owner.name}", "MiSans 40")