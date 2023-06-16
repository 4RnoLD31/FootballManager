import utils.constants
from utils.constants import *
from models.play_video import PlayVideo
from models.club import Club


class PlusButton:
    def __init__(self, strings, color_font, w_info, canvas, y=0, personal=None):
        self.strings = strings
        self.color_font = color_font
        self.w_info = w_info
        self.canvas = canvas
        self.y = y
        self.personal = personal
        self.list = []
        self.list_outline = []
        self.button = Button(self.w_info, text="+", font=("MiSans Heavy", 30), fg="green", bg=self.color_font, command=self.clicked)
        self.is_closed = True
        for element in self.strings:
            if "Владелец" in element:
                if self.y == 0: self.stock_y = self.y = 115
                self.stock_y = self.y
                self.title_outline = self.canvas.create_text(405, self.y + 5, text="Основные сведения", font=("MiSans Heavy", 40), anchor="center", fill="black")
                self.title = self.canvas.create_text(400, self.y, text="Основные сведения", font=("MiSans Heavy", 40), anchor="center", fill=self.color_font)
                self.type = "Основные сведения"
                self.button.place(x=720, y=self.y - 11, width=35, height=35)
            elif "Футболист" in element:
                if self.y == 0: self.stock_y = self.y = 175
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
            self.img_rectangle = PhotoImage(file="assets/rectangle.png")
            self.image_rectangle = self.canvas.create_image(10, self.y + 35, anchor='nw', image=self.img_rectangle)
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
            self.y += 32


class AllClubs:
    def __init__(self):
        self.frame = Toplevel()
        self.buttons = []
        self.i = 0
        for element in utils.constants.clubs.keys():
            self.buttons.append(Button(self.frame, text=clubs[element].name))
            self.buttons[self.i].pack()
            self.i += 1
        self.buttons[0].configure(command=lambda: InfoClub(clubs["Манчестер Сити"]))
        self.buttons[1].configure(command=lambda: InfoClub(clubs["Арсенал"]))
        self.buttons[2].configure(command=lambda: InfoClub(clubs["Ливерпуль"]))
        self.buttons[3].configure(command=lambda: InfoClub(clubs["Барселона"]))
        self.buttons[4].configure(command=lambda: InfoClub(clubs["Реал Мадрид"]))
        self.buttons[5].configure(command=lambda: InfoClub(clubs["Атлетико"]))
        self.buttons[6].configure(command=lambda: InfoClub(clubs["Интер"]))
        self.buttons[7].configure(command=lambda: InfoClub(clubs["Милан"]))
        self.buttons[8].configure(command=lambda: InfoClub(clubs["Ювентус"]))
        self.buttons[9].configure(command=lambda: InfoClub(clubs["Бавария"]))
        self.buttons[10].configure(command=lambda: InfoClub(clubs["Боруссия"]))
        self.buttons[11].configure(command=lambda: InfoClub(clubs["Лейпциг"]))
        self.buttons[12].configure(command=lambda: InfoClub(clubs["Спартак"]))
        self.buttons[13].configure(command=lambda: InfoClub(clubs["ЦСКА"]))
        self.buttons[14].configure(command=lambda: InfoClub(clubs["Краснодар"]))
        self.frame.mainloop()


class Info:
    def __init__(self, object):
        self.object = object
        if isinstance(self.object, Club):
            InfoClub(self.object)


class InfoClub:
    def __init__(self, club):
        self.club = club
        self.w_info = Toplevel()
        self.w_info.geometry("800x800+560+115")
        self.w_info.resizable(width=False, height=False)
        self.w_info.title("FOOTBALL MANAGER | Информация о клубе " + self.club.name)
        self.canvas = Canvas(self.w_info, height=800, width=802)
        self.canvas.place(x=-2, y=0)
        PlayVideo(self.w_info, self.canvas, self.club.img_bg)
        self.stats = []
        self.stats_outline = []
        self.strings_stats = []
        if self.club.owner is not None:
            self.strings_stats.append("Владелец: " + str(self.club.owner.name))
        else:
            self.strings_stats.append("Владелец: Отсутствует")
        self.strings_stats.append("Стоимость: " + str(self.club.price))
        self.strings_stats.append("Мощность клуба: " + str(self.club.power()))
        self.strings_stats.append("Действующая победа: " + str(self.club.current_win()))
        self.strings_stats.append("Цена за победу с игроков: " + str(self.club.win_footballer))
        self.strings_stats.append("Цена за победу с тренером: " + str(self.club.win_coach))
        self.strings_stats.append("Цена за победу с менеджером: " + str(self.club.win_manager))
        if self.club.footballer is not None and self.club.coach is not None and self.club.manager is not None:
            self.strings_stats.append("Футболист: " + str(self.club.footballer.name) + " (" + str(self.club.footballer.power) + ")")
            self.strings_stats.append("Тренер: " + str(self.club.coach.name) + " (" + str(self.club.coach.power) + ")")
            self.strings_stats.append("Менеджер: " + str(self.club.manager.name))
            self.strings_stats.append("Тип менеджера: " + str(self.club.manager.type_manager))
            if self.club.manager.type_manager == "Sheikh":
                self.strings_stats.append("Бонус менеджера: +" + str(int(sheikh_level[self.club.manager.level])) + " за победу")
            elif self.club.manager.type_manager == "Former Footballer":
                self.strings_stats.append("Бонус менеджера: +" + str(int(former_footballer_level[self.club.manager.level])) + " к победе")
            elif self.club.manager.type_manager == "Economist":
                self.strings_stats.append("Бонус менеджера: +" + str(int(economist_plus_level[self.club.manager.level] * 100)) + "% к пополнению")
                self.strings_stats.append("Бонус менеджера: -" + str(int(economist_minus_level[self.club.manager.level] * 100)) + "% к тратам")
            self.strings_stats.append("Уровень менеджера: " + str(self.club.manager.level))
        elif self.club.footballer is not None and self.club.coach is not None:
            self.strings_stats.append("Футболист: " + str(self.club.footballer.name) + " (" + str(self.club.footballer.power) + ")")
            self.strings_stats.append("Тренер: " + str(self.club.coach.name) + " (" + str(self.club.coach.power) + ")")
            self.strings_stats.append("Менеджер: Отсутствует")
        elif self.club.footballer is not None:
            self.strings_stats.append("Футболист: " + str(self.club.footballer.name) + " (" + str(self.club.footballer.power) + ")")
            self.strings_stats.append("Тренер: Отсутствует")
            self.strings_stats.append("Менеджер: Отсутствует")
        else:
            self.strings_stats.append("Футболист: Отсутствует")
            self.strings_stats.append("Тренер: Отсутствует")
            self.strings_stats.append("Менеджер: Отсутствует")
        self.canvas.create_text(406, 46, text=self.club.name, font=("MiSans Heavy", 50), anchor="center", fill="black")
        self.canvas.create_text(400, 40, text=self.club.name, font=("MiSans Heavy", 50), anchor="center", fill=self.club.color_font)
        self.y = 170
        self.list = []
        for element in self.strings_stats:
            if "Цена за победу с менеджером" in element:
                self.list = []
            elif "Менеджер: Отсутствует" in element:
                self.list.append(element)
                print(2)
                self.plus_personal = PlusButton(self.list, self.club.color_font, self.w_info, self.canvas)
                self.list = []
            elif "Уровень менеджера" in element:
                self.list.append(element)
                print(3)
                self.plus_personal = PlusButton(self.list, self.club.color_font, self.w_info, self.canvas)
                self.list = []
            else:
                self.list.append(element)
                print(element)
        for element in self.strings_stats:
            if "Цена за победу с менеджером" in element:
                self.list.append(element)
                print(1)
                PlusButton(self.list, self.club.color_font, self.w_info, self.canvas, personal=self.plus_personal)
                del self.list
                break
            else:
                self.list.append(element)
                print(element)
        self.list_personal = self.stats
        self.list_personal_outline = self.stats_outline
        self.w_info.mainloop()
