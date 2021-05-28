#!/usr/bin/python3
import date_and_time as dt
import command
import global_resource as gr
import input as imp

print("time:", dt.time_format_1())
print("Type \"help me\" to print help")


while True:
    try:
        cmd = imp.get_string(start='timecal >>> ', end='', min_len=2, max_len=4096,
                             autoclrscr=gr.auto_screen_clear)
        if not command.execute(cmd):
            print("syntax or format error type \"help me\"")
    except Exception as e:
        print('something went wrong: ', e)
