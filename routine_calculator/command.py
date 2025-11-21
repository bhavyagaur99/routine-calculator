import routine_calculator.global_resource as gr
import sys
import os
import datetime
import calendar
import routine_calculator.cmd_pmap as cmd_pmap
import routine_calculator.cmd_plresult as cmd_plresult
import routine_calculator.cmd_cal as cmd_cal
import routine_calculator.cmd_help as cmd_help
import routine_calculator.cmd_pvar as cmd_pvar
import routine_calculator.cmd_eval as cmd_eval
import routine_calculator.cmd_savemap as cmd_savemap
import routine_calculator.cmd_loadmap as cmd_loadmap


def parse_date_arg(words):
    """Helper to parse date argument from command words."""
    if len(words) > 1:
        i = 1
        if words[1] == '=':
            i = 2
        date = words[i]
        if not gr.check_date(date):
            return None
        return date
    return None


def handle_help(words):
    print(cmd_help.get())
    return True


def handle_quit(words):
    print('exiting ...\n')
    sys.exit()


def handle_clear(words):
    os.system('cls' if os.name == 'nt' else 'clear')
    return True


def handle_pmap(words):
    cmd_pmap.print_map()
    return True


def handle_savemap(words):
    if len(words) == 1:
        cmd_savemap.save_by_today()
        return True
    
    date = parse_date_arg(words)
    if date:
        year, month, day = gr.extract_date(date)
        today = datetime.datetime(year=year, month=month, day=day)
        cmd_savemap.save_by_custom_date(today)
        return True
    return False


def handle_loadmap(words):
    if len(words) == 1:
        cmd_loadmap.load_by_today(gr.get_today())
        return True
    
    date = parse_date_arg(words)
    if date:
        year, month, day = gr.extract_date(date)
        today = f'{day}-{month}-{year}'
        cmd_loadmap.load_by_today(today)
        return True
    return False


def handle_cal(words):
    cmd_cal.print_result()
    return True


def handle_plresult(words):
    cmd_plresult.print_last_result()
    return True


def handle_set(words):
    if len(words) <= 2:
        return False
    if not gr.check_variable_syntax(words[1]):
        return False
    i = 2
    if words[2] == '=':
        i = 3
    if not gr.check_value_syntax(words[i]):
        return False
    key = words[1]
    value = words[i]
    value_old = gr.data_store['variables'].get(key, None)
    gr.update_variable_in_store(key, value)
    if value_old:
        print(f'Updated: {key} from {value_old} to {value}')
    else:
        print(f'Created: {key} -> {value}')
    return True


def handle_del(words):
    if len(words) <= 1:
        return False
    if not gr.check_variable_syntax(words[1]):
        return False
    obj, ok = gr.delete_variable_in_store(words[1])
    if ok == True:
        print(f'Deleted: {obj[0]} -> {obj[1]}')
    else:
        print(f'Error: variable does not exist')
    return True


def handle_autoscrclr(words):
    if len(words) <= 1:
        return False
    i = 1
    if words[1] == '=':
        i = 2
    if not gr.check_true_false_syntax(words[i]):
        return False
    gr.auto_screen_clear = True if words[i] == 'true' else False
    print(f'updated autoscrclr to {gr.auto_screen_clear}')
    return True


def handle_stime(words):
    if len(words) <= 2:
        return False
    
    # stime needs both date and time, so we can't fully use parse_date_arg
    # but we can reuse the index logic if we wanted, but let's keep it simple for now
    # or we can adapt parse_date_arg to return index too.
    # For now, let's just leave stime as is or slightly refactor if possible.
    # Actually, stime uses `words[i]` and `words[i+1]`.
    
    i = 1
    if words[1] == '=':
        i = 2
    date = words[i]
    time = words[i + 1]

    if not gr.check_date(date):
        return False

    if not gr.check_time(time):
        return False

    y, mo, d = gr.extract_date(date)
    h, m, s = gr.extract_time(time)

    start = datetime.datetime(
        year=y, month=mo, day=d, hour=h, minute=m, second=s)
    gr.data_store['start_time'] = datetime.datetime.timestamp(start)
    gr.save_data_store()
    print('start time update =', start)
    return True


def handle_pvar(words):
    if len(words) <= 1:
        return False
    i = 1
    if words[1] == '=':
        i = 2
    if not gr.check_variable_syntax(words[i]):
        return False
    cmd_pvar.print_var(words[i])
    return True


def handle_calendar(words):
    count = len(words)
    if count == 1:
        # current month calendar
        now = datetime.datetime.now().date()
        print('\n' + calendar.month(theyear=now.year, themonth=now.month))
        return True
    
    date = parse_date_arg(words)
    if date:
        y, mo, d = gr.extract_date(date)
        print('\n' + calendar.month(theyear=y, themonth=mo))
        return True
    return False


def handle_eval(words):
    if len(words) <= 1:
        return False
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


def handle_dmap(words):
    gr.data_store['variables'] = {}
    print('Map cleared')
    return True


def handle_diff(words):
    if len(words) <= 4:
        return False
    start_date = words[1]
    start_time = words[2]
    end_date = words[3]
    end_time = words[4]

    if (not gr.check_date(start_date)) or (not gr.check_date(end_date)) or (not gr.check_time(start_time)) or (
            not gr.check_time(end_time)):
        return False

    y, mo, d = gr.extract_date(start_date)
    h, m, s = gr.extract_time(start_time)

    start = datetime.datetime(
        year=y, month=mo, day=d, hour=h, minute=m, second=s)
    start_timepoint = datetime.datetime.timestamp(start)

    y, mo, d = gr.extract_date(end_date)
    h, m, s = gr.extract_time(end_time)

    end = datetime.datetime(year=y, month=mo, day=d,
                            hour=h, minute=m, second=s)
    end_timepoint = datetime.datetime.timestamp(end)

    readable = datetime.timedelta(
        seconds=(end_timepoint - start_timepoint))
    print('Diff: ', readable)
    return True


def handle_now(words):
    now = datetime.datetime.now()
    print(f'\n{now.hour}:{now.minute}:{now.second}\n')
    return True


def handle_today(words):
    now = datetime.datetime.now()
    print(f'\n{now.day}/{now.month}/{now.year}\n')
    return True


COMMANDS = {
    'help': handle_help,
    'quit': handle_quit,
    'exit': handle_quit,
    'clear': handle_clear,
    'cls': handle_clear,
    'pmap': handle_pmap,
    'printmap': handle_pmap,
    'savemap': handle_savemap,
    'smap': handle_savemap,
    'loadmap': handle_loadmap,
    'lmap': handle_loadmap,
    'cal': handle_cal,
    'plresult': handle_plresult,
    'set': handle_set,
    'setvar': handle_set,
    'del': handle_del,
    'delvar': handle_del,
    'autoscrclr': handle_autoscrclr,
    'stime': handle_stime,
    'pvar': handle_pvar,
    'calendar': handle_calendar,
    'eval': handle_eval,
    'dmap': handle_dmap,
    'diff': handle_diff,
    'now': handle_now,
    'today': handle_today,
}


def execute(cmd):
    # default value is a whitespace in case if the user enters nothing.
    words = cmd.split()
    if not words:  # If the user just hits enter without entering any command
        return True

    command_name = words[0]
    if command_name in COMMANDS:
        return COMMANDS[command_name](words)
    
    return False
