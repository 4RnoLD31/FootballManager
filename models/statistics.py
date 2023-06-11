from utils.constants import *
import utils.constants


class Statistics:
    def __init__(self):
        utils.constants.PL1.throws = 5
        utils.constants.PL2.throws = 7
        utils.constants.PL1.numbers_thrown = 14
        utils.constants.PL2.numbers_thrown = 20
        self.element_statistic = ["Бросков сделано: ", "Сумма выбитых чисел: "]
        self.element_fonts = ["MiSans 30", "MiSans 25"]
        self.element_y = [125, 175]
        self.element_values_pl1 = [utils.constants.PL1.throws, utils.constants.PL1.numbers_thrown]
        self.element_values_pl2 = [utils.constants.PL2.throws, utils.constants.PL2.numbers_thrown]
        utils.constants.statistics_window = Toplevel()
        self.frame = utils.constants.statistics_window
        self.frame.geometry("900x900+510+70")
        self.frame.resizable(width=False, height=False)
        self.frame.title("FOOTBALL MANAGER | Статистика")
        self.canvas = Canvas(self.frame, width=100, height=900)
        self.canvas.pack()
        self.canvas.create_line(50, 0, 50, 900, width=5)
        self.l_logo = Label(self.frame, text="Статистика", font="MiSans 40")
        self.l_logo.place(x=450 - (self.l_logo.winfo_reqwidth() / 2), y=1)
        self.l_name_pl1 = Label(self.frame, text=utils.constants.PL1.name, font="MiSans 40")
        self.l_name_pl1.place(x=(450 - self.l_name_pl1.winfo_reqwidth()) / 2, y=60)
        self.l_name_pl2 = Label(self.frame, text=utils.constants.PL2.name, font="MiSans 40")
        self.l_name_pl2.place(x=(450 - self.l_name_pl2.winfo_reqwidth()) / 2 + 450, y=60)
        self.y = 150
        for element in range(0, len(self.element_statistic)):
            self.l_pl1 = Label(self.frame, text=self.element_statistic[element] + str(self.element_values_pl1[element]),
                               font=self.element_fonts[element])
            self.l_pl1.place(x=(450 - self.l_pl1.winfo_reqwidth()) / 2, y=self.element_y[element])
            self.l_pl2 = Label(self.frame, text=self.element_statistic[element] + str(self.element_values_pl2[element]),
                               font=self.element_fonts[element])
            self.l_pl2.place(x=(450 - self.l_pl2.winfo_reqwidth()) / 2 + 450, y=self.element_y[element])
        self.frame.mainloop()

    def __value_for_pl1__(self, element):
        self.element = element
        self.element.place(x=45 - self.element.winfo_reqwidth() / 2 + 355, y=150)
