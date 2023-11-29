import tkinter as tk
import utils.constants as const
import models.info as info
import models.field as field
import models.panels as panels


class Vaccine:
    def __init__(self, player):
        self.player = player
        self.y = 100
        const.clear()
        self.l_name = const.Label(const.main_window, text=f"{self.player.name} выберите персонал для излечения", font="MiSans 40")
        self.l_name.custom_place(relx=0.5, rely=0.5, anchor="center")
        self.radio = []
        self.var = tk.IntVar()
        self.var.set(-1)
        if not self.player.personal_flu():
            self.l_nothing = const.Label(const.main_window, text="Нечего лечить", font="MiSans 50")
            self.l_nothing.custom_place(relx=0.5, rely=0.5, anchor="center")
            const.main_window.after(2000, self.__stop__)

        for element in range(0, len(self.player.personal_flu())):
            self.radio.append(const.Radiobutton(text=self.player.personal_flu()[element].name, variable=self.var, value=element, command=self.__first__, font="MiSans 30"))
            self.radio[element].custom_place(x=20, y=self.y)
            self.y += 55

    def __first__(self):
        self.picked = self.player.personal_flu()[self.var.get()]
        self.b_info_about = const.Button(const.main_window, text="Информация о персонале", font="MiSans 30", command=lambda: info.Info(self.picked))
        self.b_info_about.custom_place(x=400 - self.b_info_about.winfo_reqwidth() / 2, y=600)
        self.b_continue = const.Button(const.main_window, text="Продолжить", font="MiSans 30", command=self.__second__)
        self.b_continue.custom_place(x=1200 - self.b_continue.winfo_reqwidth() / 2, y=600)

    def __second__(self):
        self.picked.flu = None
        self.player.bonuses["Vaccine"] -= 1
        const.text_on_center(f"Персонал {self.picked.name} излечен", "MiSans 40")
        const.main_window.after(4000, self.__stop__)

    def __stop__(self):
        del const.queue[0]
        panels.panels_initialize()
        field.Field.new_move()
