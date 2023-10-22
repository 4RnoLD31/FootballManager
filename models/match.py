"""class Match:
    def __init__(self, first_club):
        self.first_club = first_club
        if self.first_club.available() is True:
            text_on_center("Клуб игрока " + self.first_club.owner.name + " доступен для игры", "MiSans 40")
        else:
            text_on_center("Клуб игрока " + self.first_club.owner.name + " НЕ доступен для игры", "MiSans 40")
        utils.constants.main_window.after(3000, nothing)
        self.versus_player = utils.constants.next_player
        self.available_clubs = self.versus_player.available_clubs()
        if not self.available_clubs:
            text_on_center("У игрока " + self.versus_player.name + " нет доступных клубов для игры", "MiSans 40")
        else:
            clear()"""