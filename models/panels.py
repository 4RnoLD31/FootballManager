from tkinter import Toplevel, Button, Canvas, Scrollbar, filedialog, messagebox
from PIL import Image, ImageTk
from utils.constants import working_directory
from os import listdir
from tkinter import Label, Entry, Menu
import utils.constants
from models.save_game import save_game
from models.load_game import load_game
from models.statistics import ShowBalance
from models.debug import AllObjects

class ChangeAvatar:
    def __init__(self, player):
        self.player = player
        self.window = Toplevel()
        self.window.geometry("500x500")
        self.window.title(f"FOOTBALL MANAGER | Смена аватара {self.player.name}")
        self.window.resizable(width=False, height=False)
        self.canvas = Canvas(self.window)
        self.vsb = Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.x = 33
        self.y = 100
        self.images = []
        self.paths = []
        self.buttons = []
        self.b_upload = Button(self.canvas, text="Загрузить свою", font="MiSans 30", command=self.__file_clicked__)
        self.canvas.create_window(250 - self.b_upload.winfo_reqwidth() // 2, 0, anchor="nw", window=self.b_upload)
        for element in range(len(listdir(path=working_directory + "\\assets\\avatars\\"))):
            self.path = working_directory + "\\assets\\avatars\\" + str(element) + ".png"
            print(self.path)
            self.images.append(Image.open(self.path))
            self.images[element] = ImageTk.PhotoImage(self.images[element].resize((200, 200), Image.LANCZOS))
            self.paths.append(working_directory + "\\assets\\avatars\\" + str(element) + ".png")
            self.buttons.append(Button(self.canvas, image=self.images[element]))
            self.canvas.create_window(self.x, self.y, anchor="nw", window=self.buttons[element])
            if (element + 2) % 2 == 0:
                self.x += 233
            else:
                self.x = 33
                self.y += 233
        try:
            self.buttons[0].configure(command=lambda: self.__clicked__(self.paths[0]))
            self.buttons[1].configure(command=lambda: self.__clicked__(self.paths[1]))
            self.buttons[2].configure(command=lambda: self.__clicked__(self.paths[2]))
            self.buttons[3].configure(command=lambda: self.__clicked__(self.paths[3]))
            self.buttons[4].configure(command=lambda: self.__clicked__(self.paths[4]))
            self.buttons[5].configure(command=lambda: self.__clicked__(self.paths[5]))
            self.buttons[6].configure(command=lambda: self.__clicked__(self.paths[6]))
            self.buttons[7].configure(command=lambda: self.__clicked__(self.paths[7]))
            self.buttons[8].configure(command=lambda: self.__clicked__(self.paths[8]))
            self.buttons[9].configure(command=lambda: self.__clicked__(self.paths[9]))
        except:
            pass
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.window.mainloop()

    def __clicked__(self, path):
        self.path = path
        if self.path != "": self.player.avatar = self.path

    def __file_clicked__(self):
        messagebox.showinfo(title="Уведомление", message="Соотношение сторон файла должно быть 1 к 1. Пример разрешений: 800x800, 450x450, 2300x2300")
        while True:
            self.path = filedialog.askopenfilename(title="Выбери файл .png", defaultextension=".png")
            if self.path[len(self.path) - 4:len(self.path)] != ".png" and self.path != "":
                messagebox.showerror(title="Ошибка", message="Файл должен иметь расширение .png")
            else:
                break
        self.__clicked__(self.path)

class ChangeName:
    def __init__(self, player):
        self.player = player
        self.window = Toplevel()
        self.window.geometry("600x300")
        self.l_name = Label(self.window, text="Старое имя: " + self.player.name, font="MiSans 25")
        self.l_name.place(x=300 - (self.l_name.winfo_reqwidth() / 2), y=0)
        self.l_new_name = Label(self.window, text="Новое имя", font="MiSans 30")
        self.l_new_name.place(x=30, y=100)
        self.f_new_name = Entry(self.window, font="MiSans 30")
        self.f_new_name.place(x=255, y=105, width=300, height=50)
        self.b_new_name = Button(self.window, text="Применить", font="MiSans 20", command=lambda: self.__set_name__(self.f_new_name.get()))
        self.b_new_name.place(x=300 - (self.b_new_name.winfo_reqwidth() / 2), y=200)

    def __set_name__(self, name):
        self.name = name
        if self.player == utils.constants.PL1: utils.constants.PL1.name = self.name
        else: utils.constants.PL2.name = self.name
        panels_initialize()
        self.l_new_name.destroy()
        self.f_new_name.destroy()
        self.b_new_name.destroy()
        self.l_name.configure(text="Имя изменено на " + self.player.name, font="MiSans 30")
        self.l_name.place(x=300 - (self.l_name.winfo_reqwidth() / 2), y=150 - (self.l_name.winfo_reqheight() / 2))
        self.window.after(3000, self.window.destroy)

def pre_load_game():
    load_game()
    panels_initialize()




def panels_initialize():
    menu = Menu(utils.constants.main_window, tearoff=0)
    file_menu = Menu(utils.constants.main_window, tearoff=0)
    change_menu = Menu(utils.constants.main_window, tearoff=0)
    statistic_menu = Menu(utils.constants.main_window, tearoff=0)
    change_avatar = Menu(utils.constants.main_window, tearoff=0)
    change_name = Menu(utils.constants.main_window, tearoff=0)
    load_menu = Menu(utils.constants.main_window, tearoff=0)
    debug_menu = Menu(utils.constants.main_window, tearoff=0)
    objects_menu = Menu(utils.constants.main_window, tearoff=0)
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Изменить", menu=change_menu)
    menu.add_cascade(label="Статистика", menu=statistic_menu)
    menu.add_cascade(label="Дебаг-Меню", menu=debug_menu)
    utils.constants.main_window.configure(menu=menu)
    change_menu.add_cascade(label="Поменять аватарку", menu=change_avatar)
    change_menu.add_cascade(label="Поменять имя", menu=change_name)
    debug_menu.add_cascade(label="Все объекты", menu=objects_menu)
    objects_menu.add_command(label="Футболисты", command=lambda: AllObjects("Footballers"))
    objects_menu.add_command(label="Тренеры", command=lambda: AllObjects("Coaches"))
    objects_menu.add_command(label="Менеджеры", command=lambda: AllObjects("Managers"))
    file_menu.add_command(label="Сохранить игру", command=save_game)
    file_menu.add_cascade(label="Загрузить игру", menu=load_menu)
    file_menu.add_command(label="Выход", command=quit)
    load_menu.add_command(label="Последнее сохранение", command=pre_load_game)
    statistic_menu.add_command(label="Баланс", command=ShowBalance)
    if utils.constants.PL1 is not None:
        change_avatar.add_command(label=f"Игрок 1 - {utils.constants.PL1.name}", command=lambda: ChangeAvatar(utils.constants.PL1))
        change_avatar.add_command(label=f"Игрок 2 - {utils.constants.PL2.name}", command=lambda: ChangeAvatar(utils.constants.PL2))
        change_name.add_command(label=f"Игрок 1 - {utils.constants.PL1.name}", command=lambda: ChangeName(utils.constants.PL1))
        change_name.add_command(label=f"Игрок 2 - {utils.constants.PL2.name}", command=lambda: ChangeName(utils.constants.PL2))