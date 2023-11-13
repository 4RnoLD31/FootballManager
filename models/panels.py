import os
import tkinter as tk
import models.property as property
import utils.constants as const
import models.save_game as save_game
import models.load_game as load_game
import models.statistics as statistics
import models.debug as debug
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog


class ChangeAvatar:
    def __init__(self, player):
        self.player = player
        self.window = tk.Toplevel()
        self.window.geometry("500x500")
        self.window.title(f"FOOTBALL MANAGER | Смена аватара {self.player.name}")
        self.window.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.window)
        self.vsb = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
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
        self.b_upload = tk.Button(self.canvas, text="Загрузить свою", font="MiSans 30", command=self.__file_clicked__)
        self.canvas.create_window(250 - self.b_upload.winfo_reqwidth() // 2, 0, anchor="nw", window=self.b_upload)
        for element in range(len(os.listdir(path=f"{const.working_directory}\\assets\\avatars\\"))):
            self.path = f"{const.working_directory}\\assets\\avatars\\{element}.png"
            self.images.append(Image.open(self.path))
            self.images[element] = ImageTk.PhotoImage(self.images[element].resize((200, 200), Image.LANCZOS))
            self.paths.append(f"{const.working_directory}\\assets\\avatars\\{element}.png")
            self.buttons.append(tk.Button(self.canvas, image=self.images[element]))
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
        if self.path != "":
            self.player.avatar = self.path

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
        self.window = tk.Toplevel()
        self.window.geometry("600x300")
        self.l_name = tk.Label(self.window, text=f"Старое имя: {self.player.name}", font="MiSans 25")
        self.l_name.place(x=300 - (self.l_name.winfo_reqwidth() / 2), y=0)
        self.l_new_name = tk.Label(self.window, text="Новое имя", font="MiSans 30")
        self.l_new_name.place(x=30, y=100)
        self.f_new_name = tk.Entry(self.window, font="MiSans 30")
        self.f_new_name.place(x=255, y=105, width=300, height=50)
        self.b_new_name = tk.Button(self.window, text="Применить", font="MiSans 20", command=lambda: self.__set_name__(self.f_new_name.get()))
        self.b_new_name.place(x=300 - (self.b_new_name.winfo_reqwidth() / 2), y=200)

    def __set_name__(self, name):
        self.name = name
        if self.player == const.PL1:
            const.PL1.name = self.name
        else:
            const.PL2.name = self.name
        panels_initialize()
        self.l_new_name.destroy()
        self.f_new_name.destroy()
        self.b_new_name.destroy()
        self.l_name.configure(text=f"Имя изменено на {self.player.name}", font="MiSans 30")
        self.l_name.place(x=300 - (self.l_name.winfo_reqwidth() / 2), y=150 - (self.l_name.winfo_reqheight() / 2))
        self.window.after(3000, self.window.destroy)


def pre_load_game():
    load_game.load_game()
    panels_initialize()


def panels_initialize():
    menu = tk.Menu(const.main_window, tearoff=0)
    file_menu = tk.Menu(const.main_window, tearoff=0)
    change_menu = tk.Menu(const.main_window, tearoff=0)
    statistic_menu = tk.Menu(const.main_window, tearoff=0)
    change_avatar = tk.Menu(const.main_window, tearoff=0)
    change_name = tk.Menu(const.main_window, tearoff=0)
    load_menu = tk.Menu(const.main_window, tearoff=0)
    debug_menu = tk.Menu(const.main_window, tearoff=0)
    property_menu = tk.Menu(const.main_window, tearoff=0)
    objects_menu = tk.Menu(const.main_window, tearoff=0)
    sell = tk.Menu(const.main_window, tearoff=0)
    menu.add_cascade(label="Файл", menu=file_menu)
    menu.add_cascade(label="Изменить", menu=change_menu)
    menu.add_cascade(label="Имущество", menu=property_menu)
    menu.add_cascade(label="Статистика", menu=statistic_menu)
    menu.add_cascade(label="Дебаг-Меню", menu=debug_menu)
    const.main_window.configure(menu=menu)
    property_menu.add_cascade(label="Продажа", menu=sell)
    change_menu.add_cascade(label="Поменять аватарку", menu=change_avatar)
    change_menu.add_cascade(label="Поменять имя", menu=change_name)
    debug_menu.add_cascade(label="Все объекты", menu=objects_menu)
    objects_menu.add_command(label="Футболисты", command=lambda: debug.AllObjects("Footballers"))
    objects_menu.add_command(label="Тренеры", command=lambda: debug.AllObjects("Coaches"))
    objects_menu.add_command(label="Менеджеры", command=lambda: debug.AllObjects("Managers"))
    file_menu.add_command(label="Сохранить игру", command=save_game.save_game)
    file_menu.add_cascade(label="Загрузить игру", menu=load_menu)
    file_menu.add_command(label="Выход", command=quit)
    load_menu.add_command(label="Последнее сохранение", command=pre_load_game)
    if const.PL1 is not None:
        debug_menu.add_command(label="Изменить баланс", command=debug.ChangeBalance)
        statistic_menu.add_command(label="Баланс", command=statistics.ShowBalance)
        statistic_menu.add_command(label="Основная статистика", command=statistics.Statistics)
        sell.add_command(label=f"Игрок 1 - {const.PL1.name}", command=lambda: property.Sell(const.PL1, None, None, None, None))
        sell.add_command(label=f"Игрок 2 - {const.PL2.name}", command=lambda: property.Sell(const.PL2, None, None, None, None))
        change_avatar.add_command(label=f"Игрок 1 - {const.PL1.name}", command=lambda: ChangeAvatar(const.PL1))
        change_avatar.add_command(label=f"Игрок 2 - {const.PL2.name}", command=lambda: ChangeAvatar(const.PL2))
        change_name.add_command(label=f"Игрок 1 - {const.PL1.name}", command=lambda: ChangeName(const.PL1))
        change_name.add_command(label=f"Игрок 2 - {const.PL2.name}", command=lambda: ChangeName(const.PL2))
