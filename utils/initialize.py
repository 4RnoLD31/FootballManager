import models.club as club
import models.footballer as footballer
import models.tv_company as tv
import models.coach as coach
import models.manager as manager
import utils.constants as const
import models.highlighting as hg
import configparser
import os


if not os.path.exists(const.path_to_settings):
    settings_file = configparser.ConfigParser()
    with open(const.path_to_settings, "w") as settings:
        d_path = {"latest_autosave": ""}
        settings_file["Settings"] = d_path
        settings_file.write(settings)

if not os.path.exists(f"{const.working_directory}\\tmp"):
    os.mkdir(f"{const.working_directory}\\tmp")


def initialize():
    database_file = configparser.ConfigParser()
    database_file.read(f"{const.working_directory}//configs//database.cfg")
    footballer_name = database_file["Footballers"]["name"].split(", ")
    footballer_power = database_file["Footballers"]["power"].split(", ")
    footballer_pp = {}
    coach_name = database_file["Coaches"]["name"].split(", ")
    coach_power = database_file["Coaches"]["power"].split(", ")
    coach_pp = {}
    manager_name = database_file["Managers"]["name"].split(", ")
    manager_type = database_file["Managers"]["type"].split(", ")
    manager_price = int(database_file["Managers"]["price"])
    club_name = database_file["Clubs"]["name"].split(", ")
    club_codename = database_file["Clubs"]["codename"].split(", ")
    club_league = database_file["Clubs"]["league"].split(", ")
    club_price = database_file["Clubs"]["price"].split(", ")
    club_color = database_file["Clubs"]["color"].split(", ")
    tv_name = database_file["TVs"]["name"].split(", ")
    for index in range(len(tv_name)):
        const.TVs[tv_name[index]] = tv.TVCompany(tv_name[index])
    # Создайте словарь, разбивая каждую пару на ключ и значение
    for index in range(len(club_name)):
        const.clubs[club_name[index]] = club.Club(club_name[index], int(club_price[index]), club_league[index], club_color[index], club_codename[index])
    for element in database_file["Footballers"]["price_power"].split(", "):
        key, value = element.split(": ")
        key = int(key)
        value = int(value)
        footballer_pp[key] = value
    for index in range(len(footballer_name)):
        const.footballers[footballer_name[index]] = footballer.Footballer(footballer_name[index], int(footballer_power[index]), footballer_pp[int(footballer_power[index])])
    for element in database_file["Coaches"]["price_power"].split(", "):
        key, value = element.split(": ")
        key = int(key)
        value = int(value)
        coach_pp[key] = value
    for index in range(len(coach_name)):
        const.coaches[coach_name[index]] = coach.Coach(coach_name[index], int(coach_power[index]), coach_pp[int(coach_power[index])])
    for element in database_file["Managers"]["sheikh"].split(", "):
        key, value = element.split(": ")
        key = int(key)
        value = int(value)
        const.sheikh_level[key] = value
    for element in database_file["Managers"]["former_footballer"].split(", "):
        key, value = element.split(": ")
        key = int(key)
        value = int(value)
        const.former_footballer_level[key] = value
    for element in database_file["Managers"]["economist_plus"].split(", "):
        key, value = element.split(": ")
        key = int(key)
        value = float(value)
        const.economist_plus_level[key] = value
    for element in database_file["Managers"]["economist_minus"].split(", "):
        key, value = element.split(": ")
        key = int(key)
        value = float(value)
        const.economist_minus_level[key] = value
    for index in range(len(manager_name)):
        const.managers[manager_name[index]] = manager.Manager(manager_name[index], manager_type[index], manager_price)
    print(hg.successful("Initialized"))
