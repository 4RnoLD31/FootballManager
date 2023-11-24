import utils.constants as const
import models.field as field
import models.match as match
import models.panels as panels


class CharityMatch:
    def __init__(self, player):
        self.first_player = player
        if self.first_player == const.PL1:
            self.second_player = const.PL2
        else:
            self.second_player = const.PL1
        self.first_club = self.first_player.most_powerful_club()
        if self.first_club is False:
            const.text_on_center(f"У игрока {self.first_player.name} нет доступных клубов. Пропуск", "MiSans 40")
            const.main_window.after(4000, field.Field.new_move)
        self.second_club = self.second_player.most_powerless_club()
        del const.queue[0]
        match.Match(self.first_club, self.second_club)

    def __stop__(self):
        del const.queue[0]
        panels.panels_initialize()
        field.Field.new_move()