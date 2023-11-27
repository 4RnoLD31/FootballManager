import random
import datetime
import tkinter as tk
import utils.constants as const
import models.field as field
import models.player as player
import models.highlighting as hg
import models.error as error
import models.panels as panels
import utils.initialize as initialize


def create_main_window():
    try:
        const.main_window.destroy()
    except:
        pass
    const.main_window = tk.Tk()
    const.main_window.geometry("1600x800+160+115")
    const.main_window.resizable(width=False, height=False)
    const.main_window.title("FOOTBALL MANAGER")
    l_logo = tk.Label(const.main_window, text="FOOTBALL MANAGER", font="MiSans 50")
    l_logo.pack(side="top")
    panels.panels_initialize()
    cascade()
    const.main_window.mainloop()


def cascade():
    global f_PL1, f_PL2
    l_PL1 = tk.Label(const.main_window, text="Имя первого игрока:", font="MiSans 40")
    l_PL1.place(x=50, y=250)
    f_PL1 = tk.Entry(const.main_window, font="MiSans 30")
    f_PL1.place(x=800, y=265, width=500)
    l_PL2 = tk.Label(const.main_window, text="Имя второго игрока:", font="MiSans 40")
    l_PL2.place(x=53, y=350)
    f_PL2 = tk.Entry(const.main_window, font="MiSans 30")
    f_PL2.place(x=800, y=362, width=500)
    b_start = tk.Button(const.main_window, text="НАЧАТЬ ИГРУ", font="MiSans 40", command=process)
    const.main_window.bind("<Return>", process)
    b_start.place(x=600, y=700, width=400, height=80)


def process(*args):
    if not const.game_loaded:
        try:
            PL1_name = f_PL1.get()
            PL2_name = f_PL2.get()
        except:
            create_main_window()
            return
        if len(PL1_name) > 20 or len(PL1_name) == 0 or len(PL2_name) > 20 or len(PL2_name) == 0:
            error.error(0)
            cascade()
            return
        const.clear()
        const.PL1 = player.Player(PL1_name, 10000000)
        const.PL2 = player.Player(PL2_name, 10000000)
        print(hg.info(f"Player 1: Name {const.PL1.name} | Balance {const.PL1.balance} | Income {const.PL1.income}"))
        print(hg.info(f"Player 2: Name {const.PL2.name} | Balance {const.PL2.balance} | Income {const.PL2.income}"))
        l_first = tk.Label(const.main_window, text="Первым бросает игрок: ....", font="MiSans 50")
        l_first.place(x=800 - (l_first.winfo_reqwidth() / 2), y=400 - (l_first.winfo_reqheight() / 2))
        choice = random.randint(1, 2)
        if choice == 1:
            first = const.PL2
            l_first.config(text=f"Первым бросает игрок: {const.PL1.name}")
            const.next_player = const.PL1
        else:
            first = const.PL1
            l_first.config(text=f"Первым бросает игрок: {const.PL2.name}")
            const.next_player = const.PL2
        l_first.place(x=800 - (l_first.winfo_reqwidth() / 2), y=400 - (l_first.winfo_reqheight() / 2))
        const.main_window.after(2000, field.Field.new_move, first)
    panels.panels_initialize()


initialize.initialize()
create_main_window()
