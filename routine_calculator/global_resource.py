import os
import re
import routine_calculator.store as store
import datetime
from dotenv import load_dotenv
from typing import Tuple, Any, Optional, List


load_dotenv()
debug = True
cwd = os.getcwd()
base_dir = os.getenv('BASE_DIR', os.getcwd())
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


def update_variable_in_store(key: str, value: Any) -> Tuple[List[Any], bool]:
    global data_store
    data_store['variables'][key] = value
    filename = get_savefile_name()
    store.savemap(filename, data_store)
    return [key, value], True

def delete_variable_in_store(key: str) -> Tuple[Any, bool]:
    global data_store
    try:
        value = data_store['variables'][key]
        del data_store['variables'][key]
        filename = get_savefile_name()
        store.savemap(filename, data_store)
        return [key, value], True
    except Exception as e:
        return e, False


def save_data_store() -> None:
    global data_store
    filename = get_savefile_name()
    store.savemap(filename=filename, data_store=data_store)


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


def get_map() -> dict:
    return data_store


def check_variable_syntax(var: str) -> bool:
    regex_var = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if len(re.findall(regex_var, var)) == 1:
        return True
    print(f"Error: Invalid variable name '{var}'. Must start with a letter or underscore and contain only alphanumeric characters and underscores.")
    return False


def check_value_syntax(val: str) -> bool:
    regex_val = r'^\d+(\.\d+)?[smhdy]$'
    if len(re.findall(regex_val, val)) == 1:
        return True
    print(f"Error: Invalid value '{val}'. Must be a number followed by a unit (s, m, h, d, y).")
    return False


def convert_to_seconds(value: str) -> float:
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


def g2ds(float_var: float) -> str:  # get 2 decimal float string
    return str('{:.2f}'.format(float_var))


def check_true_false_syntax(var: str) -> bool:
    if var.lower() in ['true', 'false']:
        return True
    print(f"Error: Invalid boolean '{var}'. Must be 'true' or 'false'.")
    return False


def check_time_format(time: str) -> bool:
    regex_time = r'\d{1,2}:\d{1,2}:\d{1,2}'

    if len(re.findall(regex_time, time)) != 1:
        return False

    return True


def check_date_format(date: str) -> bool:
    regex_date = r'\d{1,2}/\d{1,2}/\d{4}'

    if len(re.findall(regex_date, date)) != 1:
        return False

    return True




def extract_date(date: str) -> Tuple[int, int, int]:
    d, mo, y = date.split('/')
    d = int(d)
    mo = int(mo)
    y = int(y)
    return y, mo, d


def extract_time(time: str) -> Tuple[int, int, int]:
    h, m, s = time.split(':')
    h = int(h)
    m = int(m)
    s = int(s)
    return h, m, s


def check_date_value(value: Tuple[int, int, int]) -> bool:
    try:
        datetime.date(year=value[0], month=value[1], day=value[2])
        return True
    except ValueError:
        return False


def check_time_value(value: Tuple[int, int, int]) -> bool:
    try:
        datetime.time(hour=value[0], minute=value[1], second=value[2])
        return True
    except ValueError:
        return False


def check_date(date: str) -> bool:
    if not check_date_format(date):
        return False
    y, mo, d = extract_date(date)
    if not check_date_value((y, mo, d)):
        return False
    return True


def check_time(time: str) -> bool:
    if not check_time_format(time):
        return False
    h, m, s = extract_time(time)
    if not check_time_value((h, m, s)):
        return False
    return True


def check_date_and_time(v: Tuple[int, int, int, int, int, int]) -> bool:
    try:
        datetime.datetime(year=v[0], month=v[1], day=v[2],
                          hour=v[3], minute=v[4], second=v[5])
        return True
    except ValueError:
        return False


def convert_date_and_time_to_seconds(v: Tuple[int, int, int, int, int, int]) -> float:
    try:
        val1 = datetime.datetime(
            year=v[0], month=v[1], day=v[2], hour=v[3], minute=v[4], second=v[5])
        val2 = datetime.datetime(year=1970, month=1, day=1)
        return abs((val2 - val1).total_seconds())
    except ValueError:
        return -1.0


def now() -> datetime.datetime:
    return datetime.datetime.now()


def time_format_1() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')
