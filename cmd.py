import global_resource as gr
import date_and_time as dt
import sys
import os
import datetime
import calendar
import cmd_set
import cmd_delvar
import cmd_pmap
import cmd_plresult
import cmd_cal
import cmd_help
import cmd_pvar
import cmd_eval
import cmd_savemap
import cmd_loadmap


def execute(cmd):
    # default value is a whitespace in case if the user enters nothing.
    words = cmd.split()
    if not words:  # If the user just hits enter without entering any command
        return True

    if words[0] == 'help':
        print(cmd_help.get())
    elif words[0] in ['quit', 'exit']:
        print('program is now exiting\n')
        sys.exit()
    elif words[0] in ['clear', 'cls']:
        os.system('cls' if os.name == 'nt' else 'clear')
    elif words[0] in ['pmap', 'printmap']:
        cmd_pmap.print_map()
    elif words[0] in ['savemap', 'smap']:
        if len(words) == 1:
            cmd_savemap.save_by_today(gr.get_today())
            return True
        elif len(words) > 1:
            i = 1
            if words[1] == '=':
                i = 2
            date = words[i]
            if not dt.check_date(date):
                return False
            year, month, day = dt.extract_date(date)
            today = f'{day}-{month}-{year}'
            cmd_savemap.save_by_today(today)
            return True

    elif words[0] in ['loadmap', 'lmap']:
        if len(words) == 1:
            cmd_loadmap.load_by_today(gr.get_today())
            return True
        elif len(words) > 1:
            i = 1
            if words[1] == '=':
                i = 2
            date = words[i]
            if not dt.check_date(date):
                return False
            year, month, day = dt.extract_date(date)
            today = f'{day}-{month}-{year}'
            cmd_loadmap.load_by_today(today)
            return True

    elif words[0] == 'cal':
        cmd_cal.print_result()
    elif words[0] == 'plresult':
        cmd_plresult.print_last_result()
    elif words[0] == 'set' and len(words) > 2:
        if not gr.check_variable_syntax(words[1]):
            return False
        i = 2
        if words[2] == '=':
            i = 3
        if not gr.check_value_syntax(words[i]):
            return False

        cmd_set.set_var(var=words[1], val=words[i])

    elif words[0] == 'delvar' and len(words) > 1:
        if not gr.check_variable_syntax(words[1]):
            return False
        cmd_delvar.remove_var(words[1])

    elif words[0] == 'autoscrclr' and len(words) > 1:
        i = 1
        if words[1] == '=':
            i = 2
        if not gr.check_true_false_syntax(words[i]):
            return False
        gr.auto_screen_clear = True if words[i] == 'true' else False
        print(f'updated autoscrclr to {gr.auto_screen_clear}')

    elif words[0] == 'stime' and len(words) > 2:
        i = 1
        if words[1] == '=':
            i = 2
        date = words[i]
        time = words[i + 1]

        if not dt.check_date(date):
            return False

        if not dt.check_time(time):
            return False

        y, mo, d = dt.extract_date(date)
        h, m, s = dt.extract_time(time)

        start = datetime.datetime(
            year=y, month=mo, day=d, hour=h, minute=m, second=s)
        gr.data_store['start_time'] = datetime.datetime.timestamp(start)
        print('start time update =', start)

    elif words[0] == 'pvar' and len(words) > 1:
        i = 1
        if words[1] == '=':
            i = 2
        if not gr.check_variable_syntax(words[i]):
            return False
        cmd_pvar.print_var(words[i])

    elif words[0] == 'calendar':
        count = len(words)
        if count == 1:
            # current month calendar
            now = datetime.datetime.now().date()
            print('\n' + calendar.month(theyear=now.year, themonth=now.month))
            return True
        elif count > 1:
            # the second parameter is date
            i = 1
            if words[1] == '=':
                i = 2
            date = words[i]
            if not dt.check_date(date):
                return False
            y, mo, d = dt.extract_date(date)
            print('\n' + calendar.month(theyear=y, themonth=mo))
            return True

    elif words[0] == 'eval' and len(words) > 1:
        simple_string = ''
        for word in words[1:]:
            simple_string += word
            simple_string += ' '
        try:
            code = cmd_eval.simple_eval(simple_string)
        except:
            return False

        print(code)
        return True

    elif words[0] == 'dmap':
        gr.data_store = {}
        print('Map cleared')

    elif words[0] == 'diff' and len(words) > 4:
        start_date = words[1]
        start_time = words[2]
        end_date = words[3]
        end_time = words[4]

        if (not dt.check_date(start_date)) or (not dt.check_date(end_date)) or (not dt.check_time(start_time)) or (
                not dt.check_time(end_time)):
            return False

        y, mo, d = dt.extract_date(start_date)
        h, m, s = dt.extract_time(start_time)

        start = datetime.datetime(
            year=y, month=mo, day=d, hour=h, minute=m, second=s)
        start_timepoint = datetime.datetime.timestamp(start)

        y, mo, d = dt.extract_date(end_date)
        h, m, s = dt.extract_time(end_time)

        end = datetime.datetime(year=y, month=mo, day=d,
                                hour=h, minute=m, second=s)
        end_timepoint = datetime.datetime.timestamp(end)

        readable = datetime.timedelta(
            seconds=(end_timepoint - start_timepoint))
        print('Diff: ', readable)
        return True

    elif words[0] == 'now':
        now = datetime.datetime.now()
        print(f'\n{now.hour}:{now.minute}:{now.second}\n')
        return True

    elif words[0] == 'today':
        now = datetime.datetime.now()
        print(f'\n{now.day}/{now.month}/{now.year}\n')
        return True

    else:
        return False

    return True
