import module_locator
import os
import datetime


debug = True
base_dir = module_locator.module_path()
database_path = os.path.join(base_dir, 'data', 'timecal_database')
start_time = 0.0  # Store start time in seconds
auto_screen_clear = False
last_cal_result = ""
variable_store = {
    "food": "60m",
    "news": "30m",
}

if debug:
    print('base dir:', base_dir)
    print('database path:', database_path)


def get_database_path() -> str:
    return database_path


def get_savefile_name() -> str:
    t = datetime.datetime.today()
    filename = os.path.join(database_path, str(t.year), str(t.month), str(t.day), 'map.json')
    return filename


def get_savefile_name_custom(year: int, month: int, day: int) -> str:
    filename = os.path.join(database_path, str(year), str(month), str(day), 'map.json')
    return filename


def get_map():
    return variable_store


def check_variable_syntax(var):
    return True


def check_value_syntax(val):
    return True


def convert_to_seconds(value):
    unit = value[-1]  # last character is the unit
    qty = float(value[:-1])  # remove the last character
    if unit == "s":
        return qty * 1
    if unit == "m":
        return qty * 60
    if unit == "h":
        return qty * 3600
    if unit == "d":
        return qty * 86400
    if unit == "y":
        return qty * 31536000
    return qty


def g2ds(float_var):  # get 2 decimal float string
    return str("{:.2f}".format(float_var))


def check_true_false_syntax(var):
    return True
