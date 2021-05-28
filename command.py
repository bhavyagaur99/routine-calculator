import sys
import os
import set_command as set_cmd
import global_resource as gr
import delvar_command as delvar_cmd
import pmap_command as pmap_cmd
import plresult_command as plresult_cmd
import cal_command as cal_cmd
import help_command as help_cmd
import date_and_time as dt
import datetime
import pvar_command as pvar_cmd
import calendar
import eval_command as eval_cmd
import savemap_command as savemap_cmd
import loadmap_command as loadmap_cmd


def execute(cmd):
    words = cmd.split()  # default value is a whitespace in case if the user enters nothing.
    if not words:  # If the user just hits enter without entering any command
        return True

    if words[0] == "help":
        print(help_cmd.get())
    elif words[0] in ["quit", 'exit']:
        print("program is now exiting\n")
        sys.exit()
    elif words[0] in ["clear", 'cls']:
        os.system('cls' if os.name == 'nt' else 'clear')
    elif words[0] in ["pmap", 'printmap']:
        pmap_cmd.print_map()
    elif words[0] in ["savemap", 'smap']:
        if len(words) == 1:
            filename = gr.get_savefile_name()
            savemap_cmd.save(filename)
            return True
        elif len(words) > 1:
            i = 1
            if words[1] == '=':
                i = 2
            date = words[i]
            if not dt.check_date(date):
                return False
            year, month, day = dt.extract_date(date)
            filename = gr.get_savefile_name_custom(year, month, day)
            savemap_cmd.save(filename)
            return True

    elif words[0] in ["loadmap", 'lmap']:
        if len(words) == 1:
            filename = gr.get_savefile_name()
            loadmap_cmd.load(filename)
            return True
        elif len(words) > 1:
            i = 1
            if words[1] == '=':
                i = 2
            date = words[i]
            if not dt.check_date(date):
                return False
            year, month, day = dt.extract_date(date)
            filename = gr.get_savefile_name_custom(year, month, day)
            loadmap_cmd.load(filename)
            return True

    elif words[0] == "cal":
        cal_cmd.print_result()
    elif words[0] == "plresult":
        plresult_cmd.print_last_result()
    elif words[0] == "set" and len(words) > 2:
        if not gr.check_variable_syntax(words[1]):
            return False
        i = 2
        if words[2] == "=":
            i = 3
        if not gr.check_value_syntax(words[i]):
            return False

        set_cmd.set_var(var=words[1], val=words[i])

    elif words[0] == "delvar" and len(words) > 1:
        if not gr.check_variable_syntax(words[1]):
            return False
        delvar_cmd.remove_var(words[1])

    elif words[0] == "autoscrclr" and len(words) > 1:
        i = 1
        if words[1] == "=":
            i = 2
        if not gr.check_true_false_syntax(words[i]):
            return False
        gr.auto_screen_clear = True if words[i] == "true" else False
        print(f"updated autoscrclr to {gr.auto_screen_clear}")

    elif words[0] == "stime" and len(words) > 2:
        i = 1
        if words[1] == "=":
            i = 2
        date = words[i]
        time = words[i + 1]

        if not dt.check_date(date):
            return False

        if not dt.check_time(time):
            return False

        y, mo, d = dt.extract_date(date)
        h, m, s = dt.extract_time(time)

        start = datetime.datetime(year=y, month=mo, day=d, hour=h, minute=m, second=s)
        gr.start_time = datetime.datetime.timestamp(start)
        print("start time update =", start)

    elif words[0] == "pvar" and len(words) > 1:
        i = 1
        if words[1] == "=":
            i = 2
        if not gr.check_variable_syntax(words[i]):
            return False
        pvar_cmd.print_var(words[i])

    elif words[0] == "calendar":
        count = len(words)
        if count == 1:
            # current month calendar
            now = datetime.datetime.now().date()
            print("\n" + calendar.month(theyear=now.year, themonth=now.month))
            return True
        elif count > 1:
            # the second parameter is date
            i = 1
            if words[1] == "=":
                i = 2
            date = words[i]
            if not dt.check_date(date):
                return False
            y, mo, d = dt.extract_date(date)
            print("\n" + calendar.month(theyear=y, themonth=mo))
            return True

    elif words[0] == "eval" and len(words) > 1:
        simple_string = ""
        for word in words[1:]:
            simple_string += word
            simple_string += ' '
        try:
            code = eval_cmd.simple_eval(simple_string)
        except:
            return False

        print(code)
        return True

    elif words[0] == "dmap":
        gr.variable_store = {}
        print("Map cleared")

    elif words[0] == "diff" and len(words) > 4:
        start_date = words[1]
        start_time = words[2]
        end_date = words[3]
        end_time = words[4]

        if (not dt.check_date(start_date)) or (not dt.check_date(end_date)) or (not dt.check_time(start_time)) or (
                not dt.check_time(end_time)):
            return False

        y, mo, d = dt.extract_date(start_date)
        h, m, s = dt.extract_time(start_time)

        start = datetime.datetime(year=y, month=mo, day=d, hour=h, minute=m, second=s)
        start_timepoint = datetime.datetime.timestamp(start)

        y, mo, d = dt.extract_date(end_date)
        h, m, s = dt.extract_time(end_time)

        end = datetime.datetime(year=y, month=mo, day=d, hour=h, minute=m, second=s)
        end_timepoint = datetime.datetime.timestamp(end)

        readable = datetime.timedelta(seconds=(end_timepoint - start_timepoint))
        print("Diff: ", readable)
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
