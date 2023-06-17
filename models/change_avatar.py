from tkinter import Toplevel, Button, Canvas, Scrollbar, filedialog, messagebox
from PIL import Image, ImageTk
from utils.constants import working_directory
from os import listdir

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
        for element in range(len(listdir(path=working_directory + "/assets/avatars/"))):
            self.path = working_directory + "/assets/avatars/" + str(element) + ".png"
            self.images.append(Image.open(self.path))
            self.images[element] = ImageTk.PhotoImage(self.images[element].resize((200, 200), Image.LANCZOS))
            self.paths.append(working_directory + "/assets/avatars/" + str(element) + ".png")
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
        messagebox.showinfo(title="Уведомление", message="Соотношение файла должно быть 1 к 1. Пример разрешений: 800x800, 450x450, 2300x2300")
        while True:
            self.path = filedialog.askopenfilename(title="Выбери файл .png", defaultextension=".png")
            if self.path[len(self.path) - 4:len(self.path)] != ".png" and self.path != "":
                messagebox.showerror(title="Ошибка", message="Файл должен иметь расширение .png")
            else:
                break
        self.__clicked__(self.path)
