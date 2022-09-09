import datetime
import re


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
