import datetime
import models.highlighting as hg

timebuild = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p").lstrip("0").replace(" 0", " ")
new_lines = []

version = str(input(hg.info("Enter program version (example 0.0.2): ")))

with open("utils/constants.py", "r") as file:
    lines = file.readlines()

for element in lines:
    if element.startswith("date_of_build"):
        new_lines.append(f'date_of_build = "{timebuild}"\n')
    elif element.startswith("version"):
        new_lines.append(f'version = "{version}"\n')
    else:
        new_lines.append(element)

with open("utils/constants.py", "w") as file:
    file.writelines(new_lines)

print(hg.successful("Successful edited"))