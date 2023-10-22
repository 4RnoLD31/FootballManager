import utils.constants
from models.club import Club
from models.footballer import Footballer
from models.tv_company import TVCompany
from models.coach import Coach
from models.manager import Manager
from utils.constants import *
from configparser import ConfigParser
from os import path as os
from models.statistics import ShowBalance
import pickle

if not os.exists(working_directory + "\\settings.ini"):
    settings_file = ConfigParser()
    with open(path_to_settings, "w") as settings:
        settings_file.write(settings)



def initialize():
    for element in range(len(utils.constants.names_clubs)):
        utils.constants.clubs[utils.constants.names_clubs[element]] = Club(utils.constants.names_clubs[element], utils.constants.prices_clubs[element],
                                                                           utils.constants.leagues_clubs[element], utils.constants.colors_clubs[element],
                                                                           utils.constants.codenames_clubs[element])



    for TV in utils.constants.name_TV:
        utils.constants.TVs[TV] = TVCompany(TV)
    database_file = ConfigParser()
    database_file.read(working_directory + "//configs//database.cfg")
    footballer_name = database_file["Footballers"]["name"].split(', ')
    footballer_power = database_file["Footballers"]["power"].split(', ')
    footballer_pp = {}
    coach_name = database_file["Coaches"]["name"].split(', ')
    coach_power = database_file["Coaches"]["power"].split(', ')
    coach_pp = {}
    manager_name = database_file["Managers"]["name"].split(', ')
    manager_type = database_file["Managers"]["type"].split(', ')
    manager_price = int(database_file["Managers"]["price"])
    # Создайте словарь, разбивая каждую пару на ключ и значение
    for element in database_file["Footballers"]["price_power"].split(', '):
        key, value = element.split(': ')
        key = int(key)
        value = int(value)
        footballer_pp[key] = value
    for index in range(len(footballer_name)):
        utils.constants.footballers[footballer_name[index]] = Footballer(footballer_name[index], int(footballer_power[index]), footballer_pp[int(footballer_power[index])])
    for element in database_file["Coaches"]["price_power"].split(', '):
        key, value = element.split(': ')
        key = int(key)
        value = int(value)
        coach_pp[key] = value
    for index in range(len(coach_name)):
        utils.constants.coaches[coach_name[index]] = Coach(coach_name[index], int(coach_power[index]), coach_pp[int(coach_power[index])])
    for element in database_file["Managers"]["sheikh"].split(', '):
        key, value = element.split(': ')
        key = int(key)
        value = int(value)
        utils.constants.sheikh_level[key] = value
    for element in database_file["Managers"]["former_footballer"].split(', '):
        key, value = element.split(': ')
        key = int(key)
        value = int(value)
        utils.constants.former_footballer_level[key] = value
    for element in database_file["Managers"]["economist_plus"].split(', '):
        key, value = element.split(': ')
        key = int(key)
        value = float(value)
        utils.constants.economist_plus_level[key] = value
    for element in database_file["Managers"]["economist_minus"].split(', '):
        key, value = element.split(': ')
        key = int(key)
        value = float(value)
        utils.constants.economist_minus_level[key] = value
    for index in range(len(manager_name)):
        utils.constants.managers[manager_name[index]] = Manager(manager_name[index], manager_type[index], manager_price)
#    footballers_data = {"names": name_footballers, "powers": power_footballers, "price_power": footballers_pp}
#    database_file = ConfigParser()
#    with open(working_directory + "//configs//footballers.cfg", "w") as database:
#        database_file["Footballers"] = footballers_data
#        database_file.write(database)


