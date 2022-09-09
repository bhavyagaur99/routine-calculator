import os
import datetime
import save
from dotenv import load_dotenv


load_dotenv()
debug = True
cwd = os.getcwd()
base_dir = os.getenv('BASE_DIR', None)
if base_dir is None:
    base_dir = os.path.join(cwd, 'data')
database_path = os.path.join(base_dir, 'data', 'routine-calculator')
start_time = 0.0  # Store start time in seconds
auto_screen_clear = False
last_cal_result = ''
data_store_version = '1.0'
data_store = {  # default start values if map.json not found
    'version': data_store_version,
    'start_time': '',
    'variables': {
        'food': '60m',
        'news': '30m',
    }
}

if debug:
    print()
    print('database path:', database_path)


def update_variable_store(key, value):
    global data_store
    data_store['variables'][key] = value
    filename = get_savefile_name()
    save.save(filename, data_store)


def get_database_path() -> str:
    return database_path


def get_savefile_name() -> str:
    t = datetime.datetime.today()
    filename = os.path.join(database_path, str(
        t.year), str(t.month), str(t.day), 'map.json')
    return filename


def get_today() -> str:
    t = datetime.datetime.today()
    d = "{:02d}".format(t.day)
    m = "{:02d}".format(t.month)
    y = f'{t.year}'
    return '/'.join([d, m, y])


def get_savefile_name_custom(year: int, month: int, day: int) -> str:
    filename = os.path.join(database_path, str(
        year), str(month), str(day), 'map.json')
    return filename


def get_map():
    return data_store


def check_variable_syntax(var):
    return True


def check_value_syntax(val):
    return True


def convert_to_seconds(value):
    unit = value[-1]  # last character is the unit
    qty = float(value[:-1])  # remove the last character
    if unit == 's':
        return qty * 1
    if unit == 'm':
        return qty * 60
    if unit == 'h':
        return qty * 3600
    if unit == 'd':
        return qty * 86400
    if unit == 'y':
        return qty * 31536000
    return qty


def g2ds(float_var):  # get 2 decimal float string
    return str('{:.2f}'.format(float_var))


def check_true_false_syntax(var):
    return True
