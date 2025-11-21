def get():
    output = '''
    Routine Calculator Help
    =======================

    Commands:
    ---------
    help                    Display this help message
    quit, exit              Exit the application
    clear, cls              Clear the screen
    
    Variables & Time Tracking:
    --------------------------
    set <var> = <val>       Set a variable to a time value.
                            Example: set food = 30m
                            Units: s (seconds), m (minutes), h (hours), d (days), y (years)
                            
    delvar <var>            Delete a variable.
                            Example: delvar food
                            
    pmap, printmap          Print all variables and their values.
    pvar <var>              Print the value of a specific variable.
    dmap                    Delete all variables (clear map).
    
    savemap [date]          Save variables to disk. Default is today.
                            Example: savemap
                            Example: savemap 12/12/2023
                            
    loadmap [date]          Load variables from disk. Default is today.
                            Example: loadmap
                            Example: loadmap 12/12/2023

    Calculation:
    ------------
    cal                     Calculate total time spent and time wasted (if start time is set).
    plresult                Print the last calculation result.
    eval <expression>       Evaluate a math expression.
                            Example: eval 1 + 1
    diff <start_date> <start_time> <end_date> <end_time>
                            Calculate difference between two timestamps.
                            Example: diff 5/3/2020 17:30:0 4/4/2020 23:12:0

    Configuration:
    --------------
    stime <date> <time>     Set the start time of the day.
                            Example: stime 12/12/2023 09:00:00
                            
    autoscrclr <bool>       Enable/disable auto screen clear.
                            Example: autoscrclr true

    Utilities:
    ----------
    calendar [date]         Print calendar. Default is current month.
                            Example: calendar
                            Example: calendar 12/12/2023
    now                     Print current time.
    today                   Print current date.

    Validation Rules:
    -----------------
    - Variables: Must start with a letter/underscore and contain only alphanumeric chars.
    - Values: Number followed by unit (e.g., 10m, 1.5h).
    - Booleans: 'true' or 'false' (case-insensitive).
'''
    return output
