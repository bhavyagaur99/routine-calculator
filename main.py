#!/usr/bin/python3

import input as imp
import date_and_time as dt
import global_resource as gr
import load
import cmd


filename = gr.get_savefile_name()
load.load(filename=filename)

print(gr.get_today(), dt.time_format_1())
print('Type "help me" to print help')
print()


while True:
    try:
        inpcmd = imp.get_string(start='timecal >>> ', end='', min_len=2, max_len=4096,
                                autoclrscr=gr.auto_screen_clear)
        if not cmd.execute(inpcmd):
            print('syntax or format error type "help me"')
    except Exception as e:
        print('something went wrong: ', e)
