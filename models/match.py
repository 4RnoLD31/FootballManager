import random
import tkinter as tk
import utils.constants as const
import models.property as property
import models.field as field
import models.panels as panels
import models.info as info


class Match:
    def __init__(self, first_club, second_club=None):
        self.first_club = first_club
        self.second_club = second_club
        self.first_player = self.first_club.owner
        if self.first_player == const.PL1:
            self.second_player = const.PL2
        else:
            self.second_player = const.PL1
        if self.first_club.available() and self.second_club is None:
            const.text_on_center(f"{self.first_club.name} доступен для игры", "MiSans 50")
        elif not self.first_club.available() and self.second_club is None:
            const.text_on_center(f"{self.first_club.name} не доступен для игры", "MiSans 50")
        if self.second_club is not None and self.second_club is not False:
            self.__match__()
            return
        elif self.second_club is False:
            self.lost_player = self.second_player
            self.lost_club = self.second_club
            self.won_player = self.first_player
            self.won_club = self.first_club
            const.text_on_center(f"Благотворительный матч: Лучший клуб {self.first_player.name} {self.first_club.name}, а у {self.second_player.name} нет клубов", "MiSans 40")
            const.main_window.after(4000, self.__lose__)
            return
        const.main_window.after(4000, self.__choose_club__)

    def __choose_club__(self):
        if not self.first_club.available() and not self.second_player.available_clubs():
            const.text_on_center(f"Клуб {self.first_club.name} недоступен для игры, а у игрока {self.second_player.name} нет доступных клубов\nПропуск", font="MiSans 40")
            const.main_window.after(4000, field.Field.new_move)
        elif len(self.second_player.available_clubs()) == 1:
            self.second_club = self.second_player.available_clubs()[0]
            const.text_on_center(f"У игрока {self.second_player.name} есть только один клуб для игры - {self.second_club.name}", "MiSans 40")
            const.main_window.after(4000, self.__match__)
        elif len(self.second_player.available_clubs()) > 1:
            const.text_on_center(f"У игрока {self.second_player.name} есть несколько клубов для игры", "MiSans 40")
            const.main_window.after(4000, self.__cc_first__)
        else:
            const.text_on_center(f"У игрока {self.second_player.name} нет доступных клубов для игры", "MiSans 40")
            self.lost_player = self.second_player
            self.lost_club = self.second_club
            self.won_player = self.first_player
            self.won_club = self.first_club
            const.main_window.after(3000, self.__lose__)

    def __cc_first__(self):
        const.clear()
        self.y = 100
        self.l_name = tk.Label(const.main_window, text=f"{self.second_player.name} выберите клуб для игры", font="MiSans 40")
        self.l_name.place(x=800 - self.l_name.winfo_reqwidth() / 2, y=0)
        self.clubs = self.second_player.available_clubs()
        self.radio_clubs = []
        self.var = tk.IntVar()
        self.var.set(-1)
        for element in range(0, len(self.clubs)):
            self.radio_clubs.append(tk.Radiobutton(text=self.clubs[element].name, variable=self.var, value=element, command=self.__cc_second__, font="MiSans 30"))
            self.radio_clubs[element].place(x=20, y=self.y)
            self.y += 55

    def __cc_second__(self):
        self.second_club = self.clubs[self.var.get()]
        self.b_info_about_club = tk.Button(const.main_window, text="Информация о клубе", font="MiSans 30", command=lambda: info.Info(self.second_club))
        self.b_info_about_club.place(x=400 - self.b_info_about_club.winfo_reqwidth() / 2, y=600)
        self.b_continue = tk.Button(const.main_window, text="Продолжить", font="MiSans 30", command=self.__match__)
        self.b_continue.place(x=1200 - self.b_continue.winfo_reqwidth() / 2, y=600)

    def __match__(self):
        if self.first_club.available():
            const.text_on_center(f"Матч между {self.first_club.name} и {self.second_club.name}", "MiSans 50")
            const.main_window.after(4000, self.__m_first__)
        else:
            const.text_on_center(f"Матч между {self.first_club.name} (недоступен) и {self.second_club.name}", "MiSans 50")
            self.lost_player = self.first_player
            self.lost_club = self.first_club
            self.won_player = self.second_player
            self.won_club = self.second_club
            const.main_window.after(4000, self.__lose__)

    def __m_first__(self):
        const.clear()
        self.statistic_list = []
        self.statistic_list.append(tk.Label(const.main_window, text=self.first_club.name, font="MiSans 30"))
        self.statistic_list[0].place(x=400 - self.statistic_list[0].winfo_reqwidth() / 2, y=40)
        self.statistic_list.append(tk.Label(const.main_window, text=self.second_club.name, font="MiSans 30"))
        self.statistic_list[1].place(x=1200 - self.statistic_list[1].winfo_reqwidth() / 2, y=40)
        self.statistic_list.append(tk.Label(const.main_window, text=f"Общая мощность: {self.first_club.power()}", font="MiSans 20"))
        self.statistic_list[2].place(x=400 - self.statistic_list[2].winfo_reqwidth() / 2, y=100)
        self.statistic_list.append(tk.Label(const.main_window, text=f"Общая мощность: {self.second_club.power()}", font="MiSans 20"))
        self.statistic_list[3].place(x=1200 - self.statistic_list[3].winfo_reqwidth() / 2, y=100)
        self.l_throw = tk.Label(const.main_window, text=f"Бросает {self.first_player.name}", font="MiSans 40")
        self.l_throw.place(x=800 - self.l_throw.winfo_reqwidth() / 2, y=400)
        self.b_throw = tk.Button(const.main_window, text="Бросить", font="MiSans 30", command=lambda: self.__throw__(self.first_player))
        self.b_throw.place(x=800 - self.b_throw.winfo_reqwidth() / 2, y=500)

    def __throw__(self, player):
        self.player = player
        self.b_throw.destroy()
        self.summary = 0
        self.picked = random.randint(1, 6)
        self.summary += self.picked
        for element in const.main_window.winfo_children():
            if element not in self.statistic_list:
                element.destroy()
        panels.panels_initialize()
        self.l_thrown = tk.Label(const.main_window, text=f"{self.player.name} бросает первый куб.....", font="MiSans 40")
        self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
        const.main_window.after(2000, self.__t_first__)

    def __t_first__(self):
        self.l_thrown.configure(text=f"{self.player.name} бросает первый куб..... {self.picked}")
        self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
        const.main_window.after(2000, self.__t_second__)

    def __t_second__(self):
        self.picked = random.randint(1, 6)
        self.summary += self.picked
        self.l_thrown.configure(text=f"{self.player.name} бросает второй куб.....")
        self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
        const.main_window.after(2000, self.__t_third__)

    def __t_third__(self):
        self.l_thrown.configure(text=f"{self.player.name} бросает второй куб..... {self.picked}")
        self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
        const.main_window.after(2000, self.__t_forth__)

    def __t_forth__(self):
        self.l_thrown.configure(text=f"Сумма выбитых чисел: {self.summary}")
        if self.player == self.first_player:
            self.first_player_summary = self.summary
            self.first_player_all = self.first_club.power() + self.first_player_summary
            self.statistic_list.append(tk.Label(const.main_window, text=f"Выбито чисел: {self.first_player_summary}", font="MiSans 20"))
            self.statistic_list[4].place(x=400 - self.statistic_list[4].winfo_reqwidth() / 2, y=160)
            self.statistic_list.append(tk.Label(const.main_window, text=f"Всего: {self.first_club.power()} + {self.first_player_summary} = {self.first_player_all}", font="MiSans 20"))
            self.statistic_list[5].place(x=400 - self.statistic_list[5].winfo_reqwidth() / 2, y=220)
            self.b_throw = tk.Button(const.main_window, text=f"{self.second_player.name} бросить", font="MiSans 30", command=lambda: self.__throw__(self.second_player))
            self.b_throw.place(x=800 - self.b_throw.winfo_reqwidth() / 2, y=500)
        else:
            self.second_player_summary = self.summary
            self.second_player_all = self.second_club.power() + self.second_player_summary
            self.statistic_list.append(tk.Label(const.main_window, text=f"Выбито чисел: {self.second_player_summary}", font="MiSans 20"))
            self.statistic_list[6].place(x=1200 - self.statistic_list[6].winfo_reqwidth() / 2, y=160)
            self.statistic_list.append(tk.Label(const.main_window, text=f"Всего: {self.second_club.power()} + {self.second_player_summary} = {self.second_player_all}", font="MiSans 20"))
            self.statistic_list[7].place(x=1200 - self.statistic_list[7].winfo_reqwidth() / 2, y=220)
            const.main_window.after(4000, self.__t_fifth__)

    def __t_fifth__(self):
        self.second_club.cooldown = 10
        if self.first_player_all > self.second_player_all:
            self.l_thrown.configure(text=f"Победил игрок {self.first_player.name} с разницей в {self.first_player_all - self.second_player_all}")
            self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
            self.lost_player = self.second_player
            self.lost_club = self.second_club
            self.won_player = self.first_player
            self.won_club = self.first_club
            const.main_window.after(4000, self.__lose__)
        elif self.second_player_all > self.first_player_all:
            if self.first_club.available:
                self.l_thrown.configure(text=f"Победил игрок {self.second_player.name} с разницей в {self.second_player_all - self.first_player_all}")
                self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
            else:
                const.text_on_center(f"Победил игрок {self.second_player.name}, так как клуб {self.first_club.name} недоступен", "MiSans 40")
            self.lost_player = self.first_player
            self.lost_club = self.first_club
            self.won_player = self.second_player
            self.won_club = self.second_club
            const.main_window.after(4000, self.__lose__)
        else:
            self.l_thrown.configure(text=f"Ничья. Оба игрока набрали {self.first_player_all}")
            self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
            const.main_window.after(4000, field.Field.new_move)

    def __lose__(self):
        try:
            self.l_thrown.configure(text=f"Игрок {self.lost_player.name} должен выплатить {self.won_club.current_win()}")
            self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
        except:
            const.text_on_center(f"Игрок {self.lost_player.name} должен выплатить {self.won_club.current_win()}", "MiSans 40")
        const.main_window.after(3000, self.__l_first__)

    def __l_first__(self):
        if self.won_club.current_win() <= self.lost_player.balance:
            self.lost_player.withdrawal(self.first_club.current_win(), False)
            self.won_player.deposit(self.first_club.current_win(), False)
            try:
                self.l_thrown.configure(text=f"Игрок {self.lost_player.name} перевел {self.won_club.current_win()} {self.won_player.name}")
                self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
            except:
                const.text_on_center(f"Игрок {self.lost_player.name} перевел {self.won_club.current_win()} {self.won_player.name}", "MiSans 40")
            const.main_window.after(4000, field.Field.new_move)
        else:
            try:
                self.l_thrown.configure(text=f"Игроку {self.lost_player.name} не хватает денег. Необходимо еще {self.won_club.current_win() - self.lost_player.balance}")
                self.l_thrown.place(x=800 - self.l_thrown.winfo_reqwidth() / 2, y=400)
            except:
                const.text_on_center(f"Игроку {self.lost_player.name} не хватает денег. Необходимо еще {self.won_club.current_win() - self.lost_player.balance}", "MiSans 40")
            const.main_window.after(4000, lambda: property.Sell(self.lost_player, self.__lose__, need_money=self.won_club.current_win() - self.lost_player.balance))
