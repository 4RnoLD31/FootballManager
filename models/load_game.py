import pickle
import configparser
import utils.constants as const
import models.field as field
import models.highlighting as hg


def load_game(auto=True):
    if auto:
        settings_file = configparser.ConfigParser()
        settings_file.read("settings.ini")
        with open(settings_file["Settings"]["latest_autosave"], "rb") as load_file:
            data = pickle.load(load_file)
            print(hg.info("Game loaded"))
    for element in const.clubs:
        const.clubs[element] = data[element]
    for element in const.footballers:
        const.footballers[element] = data[element]
    for element in const.managers:
        const.managers[element] = data[element]
    for element in const.coaches:
        const.coaches[element] = data[element]
    for element in const.TVs:
        const.TVs[element] = data[element]
    const.PL1 = data["PL1"]
    const.PL2 = data["PL2"]
    const.queue = data["Queue"]
    const.next_player = data["Next Player"]
    const.working_directory = data["Working Directory"]
    const.game_loaded = data["Game Loaded"]
    field.Field.new_move()
