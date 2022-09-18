import os
import re
import store
import datetime
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
    store.savemap(filename, data_store)


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


def check_time_format(time):
    regex_time = '\d{1,2}:\d{1,2}:\d{1,2}'

    if len(re.findall(regex_time, time)) != 1:
        return False

    return True


def check_date_format(date):
    regex_date = '\d{1,2}/\d{1,2}/\d{4}'

    if len(re.findall(regex_date, date)) != 1:
        return False

    return True


def check_format(date, time, zone):
    regex_date = '\d{1,2}/\d{1,2}/\d{4}'
    regex_time = '\d{1,2}:\d{1,2}:\d{1,2}'
    regex_zone = '[a-z]{2,32}'

    if len(re.findall(regex_date, date)) != 1:
        return False

    if len(re.findall(regex_time, time)) != 1:
        return False

    if len(re.findall(regex_zone, zone)) != 1:
        return False

    return True


def extract_date(date):
    d, mo, y = date.split('/')
    d = int(d)
    mo = int(mo)
    y = int(y)
    return y, mo, d


def extract_time(time):
    h, m, s = time.split(':')
    h = int(h)
    m = int(m)
    s = int(s)
    return h, m, s


def check_date_value(value):
    try:
        datetime.date(year=value[0], month=value[1], day=value[2])
        return True
    except ValueError:
        return False


def check_time_value(value):
    try:
        datetime.time(hour=value[0], minute=value[1], second=value[2])
        return True
    except ValueError:
        return False


def check_date(date):
    if not check_date_format(date):
        return False
    y, mo, d = extract_date(date)
    if not check_date_value((y, mo, d)):
        return False
    return True


def check_time(time):
    if not check_time_format(time):
        return False
    h, m, s = extract_time(time)
    if not check_time_value((h, m, s)):
        return False
    return True


def check_date_and_time(v):
    try:
        datetime.datetime(year=v[0], month=v[1], day=v[2],
                          hour=v[3], minute=v[4], second=v[5])
        return True
    except ValueError:
        return False


def convert_date_and_time_to_seconds(v):
    try:
        val1 = datetime.datetime(
            year=v[0], month=v[1], day=v[2], hour=v[3], minute=v[4], second=v[5])
        val2 = datetime.datetime(year=1970, month=1, day=1)
        return abs((val2 - val1).total_seconds())
    except ValueError:
        return -1


def now():
    return datetime.datetime.now()


def time_format_1():
    return datetime.datetime.now().strftime('%H:%M:%S')
