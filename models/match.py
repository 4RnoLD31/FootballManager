"""class Match:
    def __init__(self, first_club):
        self.first_club = first_club
        if self.first_club.available() is True:
            const.text_on_center("Клуб игрока " + self.first_club.owner.name + " доступен для игры", "MiSans 40")
        else:
            const.text_on_center("Клуб игрока " + self.first_club.owner.name + " НЕ доступен для игры", "MiSans 40")
        const.main_window.after(3000, const.nothing)
        self.versus_player = const.next_player
        self.available_const.clubs = self.versus_player.available_const.clubs()
        if not self.available_const.clubs:
            const.text_on_center("У игрока " + self.versus_player.name + " нет доступных клубов для игры", "MiSans 40")
        else:
            const.clear()"""