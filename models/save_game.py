import os
from datetime import date
import utils.constants
import pickle
from configparser import ConfigParser
from utils.constants import path_to_settings
from models.highlighting import *


def save_game(autosave=True):
    if utils.constants.PL1 is None or utils.constants.PL2 is None:
        print(c_failed("Saving is impossible"))
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
        os.mkdir(f"saves/{type}/{date.today().strftime('%d.%m.%Y')}")
    except:
        pass
    index = 0
    while True:
        if os.path.exists(f"saves/{type}/{date.today().strftime('%d.%m.%Y')}/save{index}.dat"):
            index += 1
        else:
            path = f"saves/{type}/{date.today().strftime('%d.%m.%Y')}/save{index}.dat"
            break
    with open(path, "wb") as save_file:
        data = {}
        for element in utils.constants.clubs:
            data[element] = utils.constants.clubs[element]
        for element in utils.constants.footballers:
            data[element] = utils.constants.footballers[element]
        for element in utils.constants.managers:
            data[element] = utils.constants.managers[element]
        for element in utils.constants.coaches:
            data[element] = utils.constants.coaches[element]
        for element in utils.constants.TVs:
            data[element] = utils.constants.TVs[element]
        data["PL1"] = utils.constants.PL1
        data["PL2"] = utils.constants.PL2
        data["Next Player"] = utils.constants.next_player
        data["Working Directory"] = utils.constants.working_directory
        data["Game Loaded"] = True
        settings_file = ConfigParser()
        settings_file.read("settings.ini")
        with open(f"{utils.constants.working_directory}\\tmp\\save.tmp", "wb") as tmp_file:
            pickle.dump(data, tmp_file)
        with open(settings_file["Settings"]["latest_autosave"], "rb") as old_file, open(f"{utils.constants.working_directory}\\tmp\\save.tmp", "rb") as new_file:
            old = old_file.read()
            new = new_file.read()
            if old == new:
                print(c_failed("Game is not saved. File has already been saved"))
                leave = True
            else:
                leave = False
        pickle.dump(data, save_file)
        d_path = {"latest_autosave": path}
        settings_file = ConfigParser()
        settings_file["Settings"] = d_path
    if leave:
        os.remove(f"{utils.constants.working_directory}\\tmp\\save.tmp")
        os.remove(f"{utils.constants.working_directory}\\{path}")
        return
    with open(path_to_settings, "w") as file:
        settings_file.write(file)
    print(c_successful("Game saved"))
