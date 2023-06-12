import utils.constants
from utils.constants import *
from models.play_video import *

class PlusButton:
    def __init__(self, strings, color_font, y=0):
        self.strings = strings
        self.color_font = color_font
        self.y = y
        self.list = []
        self.list_outline = []
        self.w_info = utils.constants.statistics_club_window
        self.canvas = utils.constants.statistics_club_canvas
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
                utils.constants.plus_personal.change_position(420)
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
                utils.constants.plus_personal.change_position(175)
            self.__init__(self.strings, self.color_font, self.stock_y)


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

class Club:
    def __init__(self, name, price, league, color_font, codename):
        self.name = name
        self.price = price
        self.league = league
        self.color_font = color_font
        self.codename = codename
        self.income = round(self.price // 100000 // 10) * 100000
        self.win_footballer = round(self.price // 100000 // 3) * 100000
        self.win_coach = round(self.price // 100000 // 1.5) * 100000
        self.win_manager = round(self.price // 100000 * 2) * 100000
        self.cooldown = None
        self.footballer = None
        self.coach = None
        self.manager = None
        self.potential_owner = None
        self.owner = None
        self.img_bg = working_directory + "/assets/clubs/" + self.codename + "/background.mp4"
        self.img_small = working_directory + "/assets/clubs/" + self.codename + "/small.png"
        self.img_25x25 = working_directory + "/assets/clubs/" + self.codename + "/25x25.png"

    def buy(self, potential_owner):
        self.potential_owner = potential_owner
        if self.owner != self.potential_owner and self.owner is not None:
            print("Клуб куплен")
        elif self.potential_owner.balance >= self.potential_owner.check_balance(self.price):
            self.owner = self.potential_owner
            self.owner.withdrawal(self.price)
            self.owner.deposit(self.income, "Income")
            print("Клуб приобретен")
        else:
            print("Недостаточно средств")

    def change_owner(self, owner):
        self.owner = owner

    def current_win(self):
        self.result = 0
        if self.manager is not None:
            self.result = self.win_manager
            if self.manager.type_manager == "Sheikh":
                self.result += sheikh_level[self.manager.level]
        elif self.coach is not None:
            self.result = self.win_coach
        elif self.footballer is not None:
            self.result = self.win_footballer
        return self.result

    def power(self):
        self.result = 0
        try:
            self.result += self.footballer.power
            self.result += self.coach.power
            self.result += former_footballer_level[self.manager.level]
        except:
            pass
        return self.result

    def sell(self, new_owner, on_the_transfer_market):
        self.on_the_transfer_market = on_the_transfer_market
        self.new_owner = new_owner
        self.reason_error = []
        self.reason_error.append(self.footballer)
        self.reason_error.append(self.coach)
        self.reason_error.append(self.manager)
        if self.reason_error[0] is not None or self.reason_error[1] is not None or self.reason_error[2] is not None:
            self.text = "Ошибка 1: В клубе " + self.name + " присутствуют: "
            for element in self.reason_error:
                if element is not None:
                    self.text += element.name + ", "
            self.text = self.text[:-2]
            messagebox.showerror(title="Ошибка 1", message=self.text)
            return
        self.price_sold = self.owner.deposit(round(self.price // 100000 // self.on_the_transfer_market) * 100000)
        self.owner.withdrawal(self.income, "Income")
        self.owner = self.new_owner
        print("Клуб продан", self.owner)
        return self.price_sold

    def get_fine(self, type_fine):
        self.type_fan = type_fine

    def win(self, club):
        self.club = club
        self.summary = self.current_win()
        if self.club.owner.balance >= self.summary:
            self.club.owner.withdrawal(self.summary, economist=False)
            self.owner.deposit(self.summary, economist=False)
        else:
            print("Не удалось выплатить деньги за поражение")

    def lose(self, club):
        self.club = club
        self.summary = self.club.current_win()
        if self.owner.balance >= self.summary:
            self.owner.withdrawal(self.summary, economist=False)
            self.club.owner.deposit(self.summary, economist=False)
        else:
            print("Не удалось выплатить деньги за поражение")

    def available(self):
        self.result = False
        if self.cooldown is None and self.footballer is not None and self.footballer.flu is None:
            self.result = True
        return self.result


    def info(self):
        self.w_info = utils.constants.statistics_club_window = Toplevel()
        self.w_info.geometry("800x800+560+115")
        self.w_info.resizable(width=False, height=False)
        self.w_info.title("FOOTBALL MANAGER | Информация о клубе " + self.name)
        self.canvas = utils.constants.statistics_club_canvas = Canvas(self.w_info, height=800, width=802)
        self.canvas.place(x=-2, y=0)
        MainWindow(self.w_info, utils.constants.statistics_club_canvas, self.img_bg)
        self.stats = []
        self.stats_outline = []
        self.strings_stats = []
        if self.owner is not None:
            self.strings_stats.append("Владелец: " + str(self.owner.name))
        else:
            self.strings_stats.append("Владелец: Отсутствует")
        self.strings_stats.append("Стоимость: " + str(self.price))
        self.strings_stats.append("Мощность клуба: " + str(self.power()))
        self.strings_stats.append("Действующая победа: " + str(self.current_win()))
        self.strings_stats.append("Цена за победу с игроков: " + str(self.win_footballer))
        self.strings_stats.append("Цена за победу с тренером: " + str(self.win_coach))
        self.strings_stats.append("Цена за победу с менеджером: " + str(self.win_manager))
        if self.footballer is not None and self.coach is not None and managers is not None:
            self.strings_stats.append("Футболист: " + str(self.footballer.name) + " (" + str(self.footballer.power) + ")")
            self.strings_stats.append("Тренер: " + str(self.coach.name) + " (" + str(self.coach.power) + ")")
            self.strings_stats.append("Менеджер: " + str(self.manager.name))
            self.strings_stats.append("Тип менеджера: " + str(self.manager.type_manager))
            if self.manager.type_manager == "Sheikh":
                self.strings_stats.append("Бонус менеджера: +" + str(int(sheikh_level[self.manager.level])) + " за победу")
            elif self.manager.type_manager == "Former Footballer":
                self.strings_stats.append("Бонус менеджера: +" + str(int(former_footballer_level[self.manager.level])) + " к победе")
            elif self.manager.type_manager == "Economist":
                self.strings_stats.append("Бонус менеджера: +" + str(int(economist_plus_level[self.manager.level] * 100)) + "% к пополнению")
                self.strings_stats.append("Бонус менеджера: -" + str(int(economist_minus_level[self.manager.level] * 100)) + "% к тратам")
            self.strings_stats.append("Уровень менеджера: " + str(self.manager.level))
        elif self.footballer is not None and self.coach is not None:
            self.strings_stats.append("Футболист: " + str(self.footballer.name) + " (" + str(self.footballer.power) + ")")
            self.strings_stats.append("Тренер: " + str(self.coach.name) + " (" + str(self.coach.power) + ")")
            self.strings_stats.append("Менеджер: Отсутствует")
        elif self.footballer is not None:
            self.strings_stats.append("Футболист: " + str(self.footballer.name) + " (" + str(self.footballer.power) + ")")
            self.strings_stats.append("Тренер: Отсутствует")
            self.strings_stats.append("Менеджер: Отсутствует")
        else:
            self.strings_stats.append("Футболист: Отсутствует")
            self.strings_stats.append("Тренер: Отсутствует")
            self.strings_stats.append("Менеджер: Отсутствует")
        self.canvas.create_text(406, 46, text=self.name, font=("MiSans Heavy", 50), anchor="center", fill="black")
        self.canvas.create_text(400, 40, text=self.name, font=("MiSans Heavy", 50), anchor="center", fill=self.color_font)
        self.y = 170
        self.list = []
        for element in self.strings_stats:
            if "Цена за победу с менеджером" in element:
                self.list.append(element)
                print(1)
                utils.constants.plus_basic = PlusButton(self.list, self.color_font)
                self.list = []
            elif "Менеджер: Отсутствует" in element:
                self.list.append(element)
                print(2)
                utils.constants.plus_personal = PlusButton(self.list, self.color_font)
                self.list = []
            elif "Уровень менеджера" in element:
                self.list.append(element)
                print(3)
                utils.constants.plus_personal = PlusButton(self.list, self.color_font)
                self.list = []
            else:
                self.list.append(element)
                print(element)
        self.list_personal = self.stats
        self.list_personal_outline = self.stats_outline
        self.w_info.mainloop()
