import tkinter as tk
import utils.constants as const
import models.coach as coach
import models.footballer as footballer
import models.club as club
import models.manager as manager

"""class PlusButton:
    def __init__(self, strings, color_font, w_info, canvas, y=0, personal=None):
        self.strings = strings
        self.color_font = color_font
        self.w_info = w_info
        self.canvas = canvas
        self.y = y
        self.personal = personal
        self.list = []
        self.list_outline = []
        self.button = tk.Button(self.w_info, text="+", font=("MiSans Heavy", 30), fg="green", bg=self.color_font, command=self.clicked)
        self.is_closed = True
        for element in self.strings:
            if "Владелец" in element:
                if self.y == 0:
                    self.stock_y = self.y = 115
                self.stock_y = self.y
                self.title_outline = self.canvas.create_text(405, self.y + 5, text="Основные сведения", font=("MiSans Heavy", 40), anchor="center", fill="black")
                self.title = self.canvas.create_text(400, self.y, text="Основные сведения", font=("MiSans Heavy", 40), anchor="center", fill=self.color_font)
                self.type = "Основные сведения"
                self.button.place(x=720, y=self.y - 11, width=35, height=35)
            elif "Футболист" in element:
                if self.y == 0:
                    self.stock_y = self.y = 175
                self.stock_y = self.y
                self.title_outline = self.canvas.create_text(405, self.y + 5, text="Персонал", font=("MiSans Heavy", 40), anchor="center", fill="black")
                self.title = self.canvas.create_text(400, self.y, text="Персонал", font=("MiSans Heavy", 40), anchor="center", fill=self.color_font)
                self.type = "Персонал"
                self.button.place(x=720, y=self.y - 11, width=35, height=35)

    def clicked(self):
        if self.is_closed is True:
            self.y = self.stock_y
            self.button.configure(text="-", fg="red")
            self.is_closed = False
            self.img_rectangle = tk.PhotoImage(file="assets/rectangle.png")
            self.image_rectangle = self.canvas.create_image(10, self.y + 35, anchor="nw", image=self.img_rectangle)
            self.y += 55
            self.y = self.y + 120 - (30 * (len(self.strings) + 1)) // 2
            for element in self.strings:
                self.list_outline.append(self.canvas.create_text(402, self.y + 2, text=element, font=("MiSans Heavy", 20), anchor="center", fill="black"))
                self.list.append(self.canvas.create_text(400, self.y, text=element, font=("MiSans Heavy", 20), anchor="center", fill=self.color_font))
                self.y += 32
            if self.type == "Основные сведения":
                self.personal.change_position(420)
        else:
            self.button.configure(text="+", fg="green")
            self.is_closed = True
            self.canvas.delete(self.image_rectangle)
            for element in range(len(self.list)):
                self.canvas.delete(self.list[element])
                self.canvas.delete(self.list_outline[element])
            self.canvas.delete(self.title)
            self.canvas.delete(self.title_outline)
            self.button.destroy()
            if self.type == "Основные сведения":
                self.personal.change_position(175)
            self.__init__(self.strings, self.color_font, self.w_info, self.canvas, y=self.stock_y, personal=self.personal)

    def change_position(self, y):
        self.y = y
        self.stock_y = self.y
        self.button.place(x=720, y=self.y - 11, width=35, height=35)
        self.canvas.coords(self.title_outline, 405, self.y + 5)
        self.canvas.coords(self.title, 400, self.y)
        try:
            self.canvas.coords(self.image_rectangle, 10, self.y + 35)
        except:
            pass
        self.y += 55
        self.y = self.y + 120 - (30 * (len(self.strings) + 1)) // 2
        for element in range(len(self.list)):
            self.canvas.coords(self.list_outline[element], 402, self.y + 2)
            self.canvas.coords(self.list[element], 400, self.y)
            self.y += 32"""


class AllClubs:
    def __init__(self):
        self.window = tk.Toplevel()
        self.buttons = []
        self.i = 0
        for element in const.clubs.keys():
            self.buttons.append(tk.Button(self.window, text=const.clubs[element].name))
            self.buttons[self.i].pack()
            self.i += 1
        self.buttons[0].configure(command=lambda: InfoClub(const.clubs["Manchester City"]))
        self.buttons[1].configure(command=lambda: InfoClub(const.clubs["Arsenal"]))
        self.buttons[2].configure(command=lambda: InfoClub(const.clubs["Liverpool"]))
        self.buttons[3].configure(command=lambda: InfoClub(const.clubs["Barcelona"]))
        self.buttons[4].configure(command=lambda: InfoClub(const.clubs["Real Madrid"]))
        self.buttons[5].configure(command=lambda: InfoClub(const.clubs["Atletico Madrid"]))
        self.buttons[6].configure(command=lambda: InfoClub(const.clubs["Inter"]))
        self.buttons[7].configure(command=lambda: InfoClub(const.clubs["Milan"]))
        self.buttons[8].configure(command=lambda: InfoClub(const.clubs["Juventus"]))
        self.buttons[9].configure(command=lambda: InfoClub(const.clubs["Bayern"]))
        self.buttons[10].configure(command=lambda: InfoClub(const.clubs["Borussia"]))
        self.buttons[11].configure(command=lambda: InfoClub(const.clubs["Leipzig"]))
        self.buttons[12].configure(command=lambda: InfoClub(const.clubs["Spartak Moscow"]))
        self.buttons[13].configure(command=lambda: InfoClub(const.clubs["CSKA"]))
        self.buttons[14].configure(command=lambda: InfoClub(const.clubs["Krasnodar"]))
        self.window.mainloop()


class Info:
    def __init__(self, object):
        self.object = object
        if isinstance(self.object, club.Club):
            InfoClub(self.object)
        elif isinstance(self.object, coach.Coach) or isinstance(self.object, footballer.Footballer) or isinstance(self.object, manager):
            InfoPersonal(self.object)


class InfoClub:
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


class InfoPersonal:
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
            self.strings_stats.append(f"Более еще {self.object.flu} ходов")
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
