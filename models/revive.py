import tkinter as tk
import utils.constants as const
import models.info as info
import models.field as field
import models.panels as panels
import models.property as property
import models.footballer as footballer
import models.coach as coach
import models.manager as manager


class Revive:
    def __init__(self, player):
        self.player = player
        self.y = 100
        const.clear()
        self.l_name = tk.Label(const.main_window, text=f"{self.player.name} выберите персонал для возрождения", font="MiSans 40")
        self.l_name.place(x=800 - self.l_name.winfo_reqwidth() / 2, y=0)
        self.radio = []
        self.var = tk.IntVar()
        self.var.set(-1)
        if not self.player.personal_revive():
            self.l_nothing = tk.Label(const.main_window, text="Некого возрождать", font="MiSans 50")
            self.l_nothing.place(x=800 - self.l_nothing.winfo_reqwidth() / 2, y=400 - self.l_nothing.winfo_reqheight() / 2)
            const.main_window.after(2000, self.__stop__)
        for element in range(0, len(self.player.personal_revive())):
            self.radio.append(tk.Radiobutton(text=self.player.personal_revive()[element].name, variable=self.var, value=element, command=self.__r_first__, font="MiSans 30"))
            self.radio[element].place(x=20, y=self.y)
            self.y += 55

    def __r_first__(self):
        self.p_picked = self.player.personal_revive()[self.var.get()]
        self.b_info_about = tk.Button(const.main_window, text="Информация о персонале", font="MiSans 30", command=lambda: info.Info(self.p_picked))
        self.b_info_about.place(x=400 - self.b_info_about.winfo_reqwidth() / 2, y=600)
        self.b_continue = tk.Button(const.main_window, text="Продолжить", font="MiSans 30", command=self.__r_second__)
        self.b_continue.place(x=1200 - self.b_continue.winfo_reqwidth() / 2, y=600)

    def __r_second__(self):
        self.p_picked.revive()
        self.player.bonuses["Revive"] -= 1
        const.text_on_center(f"Персонал {self.p_picked.name} возрожден. Хотите перевести его в клуб?", "MiSans 40")
        self.b_yes = tk.Button(const.main_window, text="Да", font="MiSans 30", command=lambda: self.__stop__(True))
        self.b_yes.place(x=400 - self.b_yes.winfo_reqwidth() / 2, y=600, width=200)
        self.b_no = tk.Button(const.main_window, text="Нет", font="MiSans 30", command=lambda: self.__stop__(False))
        self.b_no.place(x=1200 - self.b_no.winfo_reqwidth() / 2, y=600, width=200)

    def __stop__(self, transfer):
        self.transfer = transfer
        del const.queue[0]
        panels.panels_initialize()
        if self.transfer:
            self.__transfer__()
        else:
            field.Field.new_move()

    def __transfer__(self):
        if isinstance(self.p_picked, footballer.Footballer):
            self.clubs = self.player.where_can_i_have_a_footballer(False)
        elif isinstance(self.p_picked, coach.Coach):
            self.clubs = self.player.where_can_i_have_a_coach(False)
        elif isinstance(self.p_picked, manager.Manager):
            self.clubs = self.player.where_can_i_have_a_manager(False)
        if not self.clubs:
            const.text_on_center("Нет доступных клубов", "MiSans 50")
            const.main_window.after(4000, field.Field.new_move)
        else:
            const.clear()
            self.l_name = tk.Label(const.main_window, text="Выберите клуб", font="MiSans 40")
            self.l_name.place(x=800 - self.l_name.winfo_reqwidth() / 2, y=0)
            self.b_cancel = tk.Button(const.main_window, text="Отмена", font="MiSans 30", command=field.Field.new_move)
            self.b_cancel.place(x=800 - self.b_cancel.winfo_reqwidth() / 2, y=600)
            self.y = 100
            self.radio = []
            self.var = tk.IntVar()
            self.var.set(-1)
            for element in range(0, len(self.clubs)):
                self.radio.append(tk.Radiobutton(text=self.clubs[element].name, variable=self.var, value=element, command=self.__t_first__, font="MiSans 30"))
                self.radio[element].place(x=20, y=self.y)
                self.y += 55

    def __t_first__(self):
        self.c_picked = self.clubs[self.var.get()]
        self.b_cancel.place(x=266 - self.b_cancel.winfo_reqwidth() / 2, y=600)
        self.b_info_about = tk.Button(const.main_window, text="Информация о клубе", font="MiSans 30", command=lambda: info.Info(self.c_picked))
        self.b_info_about.place(x=800 - self.b_info_about.winfo_reqwidth() / 2, y=600)
        self.b_continue = tk.Button(const.main_window, text="Продолжить", font="MiSans 30", command=self.__t_second__)
        self.b_continue.place(x=1333 - self.b_continue.winfo_reqwidth() / 2, y=600)

    def __t_second__(self):
        self.p_picked.transfer(self.c_picked)
        const.text_on_center("Успешно", "MiSans 50")
        const.main_window.after(4000, field.Field.new_move)