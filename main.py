#!/usr/bin/python3

import input as imp
import global_resource as gr
import load
import cmd


filename = gr.get_savefile_name()
load.load(filename=filename)

print(gr.get_today(), gr.time_format_1())
print('Type "help me" to print help')


while True:
    try:
        print()
        inpcmd = imp.get_string(start='routinecal >>> ', end='', min_len=2, max_len=4096,
                                autoclrscr=gr.auto_screen_clear)
        print()
        if not cmd.execute(inpcmd):
            print('syntax or format error type "help me"')
    except Exception as e:
        print('Error: ', e)
