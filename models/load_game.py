from configparser import ConfigParser
import pickle
import utils.constants
from models.field import new_move


def load_game(auto=True):
    if auto:
        settings_file = ConfigParser()
        settings_file.read("settings.ini")
        with open(settings_file["Settings"]["latest_autosave"], "rb") as load_file:
            data = pickle.load(load_file)
            print("loaded")
    for element in utils.constants.clubs:
        utils.constants.clubs[element] = data[element]
    for element in utils.constants.footballers:
        utils.constants.footballers[element] = data[element]
    for element in utils.constants.managers:
        utils.constants.managers[element] = data[element]
    for element in utils.constants.coaches:
        utils.constants.coaches[element] = data[element]
    for element in utils.constants.TVs:
        utils.constants.TVs[element] = data[element]
    utils.constants.PL1 = data["PL1"]
    utils.constants.PL2 = data["PL2"]
    utils.constants.next_player = data["Next Player"]
    utils.constants.working_directory = data["Working Directory"]
    utils.constants.game_loaded = data["Game Loaded"]
    if utils.constants.next_player == utils.constants.PL1:
        new_move(utils.constants.PL2)
    else:
        new_move(utils.constants.PL1)
