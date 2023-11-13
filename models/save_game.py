import os
import datetime
import pickle
import configparser
import utils.constants as const
import models.highlighting as hg


def save_game(autosave=True):
    if const.PL1 is None or const.PL2 is None:
        print(hg.c_failed("Saving is impossible"))
        return
    if autosave:
        type = "autosave"
    else:
        type = "manual"
    try:
        os.mkdir("saves")
    except:
        pass
    try:
        os.mkdir(f"saves/{type}")
    except:
        pass
    try:
        os.mkdir(f"saves/{type}/{datetime.date.today().strftime('%d.%m.%Y')}")
    except:
        pass
    index = 0
    while True:
        if os.path.exists(f"saves/{type}/{datetime.date.today().strftime('%d.%m.%Y')}/save{index}.dat"):
            index += 1
        else:
            path = f"saves/{type}/{datetime.date.today().strftime('%d.%m.%Y')}/save{index}.dat"
            break
    with open(path, "wb") as save_file:
        data = {}
        for element in const.clubs:
            data[element] = const.clubs[element]
        for element in const.footballers:
            data[element] = const.footballers[element]
        for element in const.managers:
            data[element] = const.managers[element]
        for element in const.coaches:
            data[element] = const.coaches[element]
        for element in const.TVs:
            data[element] = const.TVs[element]
        data["PL1"] = const.PL1
        data["PL2"] = const.PL2
        data["Next Player"] = const.next_player
        data["Working Directory"] = const.working_directory
        data["Game Loaded"] = True
        settings_file = configparser.ConfigParser()
        settings_file.read("settings.ini")
        with open(f"{const.working_directory}\\tmp\\save.tmp", "wb") as tmp_file:
            pickle.dump(data, tmp_file)
        with open(settings_file["Settings"]["latest_autosave"], "rb") as old_file, open(f"{const.working_directory}\\tmp\\save.tmp", "rb") as new_file:
            old = old_file.read()
            new = new_file.read()
            if old == new:
                print(hg.c_failed("Game is not saved. File has already been saved"))
                leave = True
            else:
                leave = False
        pickle.dump(data, save_file)
        d_path = {"latest_autosave": path}
        settings_file = configparser.ConfigParser()
        settings_file["Settings"] = d_path
    if leave:
        os.remove(f"{const.working_directory}\\tmp\\save.tmp")
        os.remove(f"{const.working_directory}\\{path}")
        return
    with open(const.path_to_settings, "w") as file:
        settings_file.write(file)
    print(hg.c_successful("Game saved"))
