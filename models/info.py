import webbrowser
import tkinter as tk
import utils.constants as const
import models.coach as coach
import models.footballer as footballer
import models.club as club
import models.manager as manager


class AllClubs:
    def __init__(self):
        self.window = tk.Toplevel()
        self.buttons = []
        self.i = 0
        for element in const.clubs.keys():
            self.buttons.append(tk.Button(self.window, text=const.clubs[element].name))
            self.buttons[self.i].pack()
            self.i += 1
        self.buttons[0].configure(command=lambda: Club(const.clubs["Manchester City"]))
        self.buttons[1].configure(command=lambda: Club(const.clubs["Arsenal"]))
        self.buttons[2].configure(command=lambda: Club(const.clubs["Liverpool"]))
        self.buttons[3].configure(command=lambda: Club(const.clubs["Barcelona"]))
        self.buttons[4].configure(command=lambda: Club(const.clubs["Real Madrid"]))
        self.buttons[5].configure(command=lambda: Club(const.clubs["Atletico Madrid"]))
        self.buttons[6].configure(command=lambda: Club(const.clubs["Inter"]))
        self.buttons[7].configure(command=lambda: Club(const.clubs["Milan"]))
        self.buttons[8].configure(command=lambda: Club(const.clubs["Juventus"]))
        self.buttons[9].configure(command=lambda: Club(const.clubs["Bayern"]))
        self.buttons[10].configure(command=lambda: Club(const.clubs["Borussia"]))
        self.buttons[11].configure(command=lambda: Club(const.clubs["Leipzig"]))
        self.buttons[12].configure(command=lambda: Club(const.clubs["Spartak Moscow"]))
        self.buttons[13].configure(command=lambda: Club(const.clubs["CSKA"]))
        self.buttons[14].configure(command=lambda: Club(const.clubs["Krasnodar"]))
        self.window.mainloop()


class Info:
    def __init__(self, object):
        self.object = object
        if self.object == "Build":
            Build()
        elif isinstance(self.object, club.Club):
            Club(self.object)
        elif isinstance(self.object, coach.Coach) or isinstance(self.object, footballer.Footballer) or isinstance(self.object, manager.Manager):
            Personal(self.object)


class Club:
    def __init__(self, club):
        self.club = club
        self.y = 20
        self.w_info = tk.Toplevel()
        self.w_info.geometry("800x800+560+115")
        self.w_info.resizable(width=False, height=False)
        self.w_info.title(f"FOOTBALL MANAGER | Информация о клубе {self.club.name}")
        self.stats = []
        self.strings_stats = []
        if self.club.owner is not None:
            self.strings_stats.append(f"Владелец: {self.club.owner.name}")
        else:
            self.strings_stats.append("Владелец: Отсутствует")
        self.strings_stats.append(f"Стоимость: {self.club.price}")
        self.strings_stats.append(f"Мощность клуба: {self.club.power()}")
        self.strings_stats.append(f"Действующая победа: {self.club.current_win()}")
        self.strings_stats.append(f"Цена за победу с игроков: {self.club.win_footballer}")
        self.strings_stats.append(f"Цена за победу с тренером: {self.club.win_coach}")
        self.strings_stats.append(f"Цена за победу с менеджером: {self.club.win_manager}")
        if self.club.footballer is not None and self.club.coach is not None and self.club.manager is not None:
            self.strings_stats.append(f"Футболист: {self.club.footballer.name} ({self.club.footballer.power})")
            self.strings_stats.append(f"Тренер: {self.club.coach.name} + ({self.club.coach.power})")
            self.strings_stats.append(f"Менеджер: {self.club.manager.name}")
            self.strings_stats.append(f"Тип менеджера: {self.club.manager.type}")
            if self.club.manager.type == "Sheikh":
                self.strings_stats.append(f"Бонус менеджера: +{const.sheikh_level[self.club.manager.level]} за победу")
            elif self.club.manager.type == "Former Footballer":
                self.strings_stats.append(f"Бонус менеджера: +{const.former_footballer_level[self.club.manager.level]} к победе")
            elif self.club.manager.type == "Economist":
                self.strings_stats.append(f"Бонус менеджера: +{const.economist_plus_level[self.club.manager.level] * 100}% к пополнению")
                self.strings_stats.append(f"Бонус менеджера: -{const.economist_minus_level[self.club.manager.level] * 100}% к тратам")
            self.strings_stats.append(f"Уровень менеджера: {self.club.manager.level}")
        elif self.club.footballer is not None and self.club.coach is not None:
            self.strings_stats.append(f"Футболист: {self.club.footballer.name} ({self.club.footballer.power})")
            self.strings_stats.append(f"Тренер: {self.club.coach.name} ({self.club.coach.power})")
            self.strings_stats.append("Менеджер: Отсутствует")
        elif self.club.footballer is not None:
            self.strings_stats.append(f"Футболист: {self.club.footballer.name} ({self.club.footballer.power})")
            self.strings_stats.append("Тренер: Отсутствует")
            self.strings_stats.append("Менеджер: Отсутствует")
        else:
            self.strings_stats.append("Футболист: Отсутствует")
            self.strings_stats.append("Тренер: Отсутствует")
            self.strings_stats.append("Менеджер: Отсутствует")
        for element in range(0, len(self.strings_stats)):
            self.stats.append(tk.Label(self.w_info, text=self.strings_stats[element], font="MiSans 20"))
            self.stats[element].place(x=20, y=self.y)
            self.y += 40


class Personal:
    def __init__(self, object):
        self.object = object
        self.y = 20
        self.w_info = tk.Toplevel()
        self.w_info.geometry("800x800+560+115")
        self.w_info.resizable(width=False, height=False)
        self.w_info.title(f"FOOTBALL MANAGER | Информация о персонале {self.object.name}")
        self.stats = []
        self.strings_stats = []
        self.strings_stats.append(f"Имя: {self.object.name}")
        if self.object.owner is not None:
            self.strings_stats.append(f"Владелец: {self.object.owner.name}")
        else:
            self.strings_stats.append("Владелец: Отсутствует")
        self.strings_stats.append(f"Стоимость: {self.object.price}")
        self.strings_stats.append(f"Мощность: {self.object.power}")
        if self.object.club is None:
            self.strings_stats.append("Клуб: Отсутствует")
        else:
            self.strings_stats.append(f"Клуб: {self.object.club.name}")
        try:
            self.strings_stats.append(f"Тип: {self.object.type}")
            if self.object.type == "Sheikh":
                self.strings_stats.append(f"Бонус менеджера: +{const.sheikh_level[self.object.level]} за победу")
            elif self.object.type == "Former Footballer":
                self.strings_stats.append(f"Бонус менеджера: +{const.former_footballer_level[self.object.level]} к победе")
            elif self.object.type == "Economist":
                self.strings_stats.append(f"Бонус менеджера: +{const.economist_plus_level[self.object.level] * 100}% к пополнению")
                self.strings_stats.append(f"Бонус менеджера: -{const.economist_minus_level[self.object.level] * 100}% к тратам")
            self.strings_stats.append(f"Уровень менеджера: {self.object.level}")
        except:
            pass
        if self.object.flu is None:
            self.strings_stats.append("Не болеет")
        else:
            self.strings_stats.append(f"Болеет еще {self.object.flu} ходов")
        if isinstance(self.object, coach.Coach) and self.object.strike is False:
            self.strings_stats.append("Нет забастовки")
        elif isinstance(self.object, coach.Coach):
            self.strings_stats.append(f"Забастовка еще {self.object.strike} ходов")
        if self.object.dead:
            self.strings_stats.append("Мертв")
        for element in range(0, len(self.strings_stats)):
            self.stats.append(tk.Label(self.w_info, text=self.strings_stats[element], font="MiSans 20"))
            self.stats[element].place(x=20, y=self.y)
            self.y += 40


class Build:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("300x170+0+0")
        self.window.resizable(False, False)
        self.window.title = "FOOTBALL MANAGER | Информация о версии"
        self.title = tk.Label(self.window, text=f"FOOTBALL MANAGER", font=("Agency FB", "30"))
        self.title.place(x=150 - self.title.winfo_reqwidth() / 2, y=0)
        self.version = tk.Label(self.window, text=f"Version: {const.version}", font=("Agency FB", "30"))
        self.version.place(x=2, y=45)
        self.date_of_build = tk.Label(self.window, text=f"Date of build: {const.date_of_build}", font=("Agency FB", "20"))
        self.date_of_build.place(x=2, y=90)
        self.github = tk.Label(self.window, text="Github: ", font=("Agency FB", "30"))
        self.github.place(x=2, y=120)
        self.github_link = tk.Button(self.window, text="CLICK", command=lambda: webbrowser.open_new("https://github.com/4RnoLD31/FootballManager"), font=("Agency FB", "30"))
        self.github_link.place(x=(300 - self.github.winfo_reqwidth()) / 2 - self.github_link.winfo_reqwidth() / 2 + self.github.winfo_reqwidth(), y=125, height=40, width=72)