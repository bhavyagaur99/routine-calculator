def get():
    output = '''
    
    commands and description 
    ========================
    
    1) quit cmd to quit the application
    2) help cmd to display this page
    3) clear cmd to clear the display
    4) set(set_t) <variable name> = time cmd to add a new entry
    5) plresult cmd to print the result last calculated by calc
    6) cal cmd to calculate save and print result
    7) stime cmd to set start time of the day
    8) pmap cmd to print all variables and there value.
    9) pvar cmd to print a selected variable
    10) delvar cmd to delete a variable
    11) autoscrclr cmd will automatically screen for you
    12) calendar cmd to print the calendar to screen
    13) savemap cmd to save the variables to the disk
    14) eval cmd to do basic arithmetic and print to screen also use this result to set
    15) dmap cmd will delete the current map
    16) loadmap cmd will load map from the disk
    17) diff cmd will help you to calculate the difference between two points in time
    
    reserved variables
    ==================    
    stime
    quit
    help
    set
    cal
    presult
    pmap
    delvar
    autoscrclr
    .
    .
    .
    Basically all the command variables are reserved please do not use them
    also ` char is reserved
    
    format or syntax
    ================
    
    stime <time>       
        start_time = hh:mm:ss    
        rules are relaxed you can also do
        start_time 1:32:0    
        presence of all the field is mandatory
        fields are h, m, s
        example: start_time  16:1:00
            or   start_time = 16:1:00
            or   start_time = 16:01:0
            or   any other valid combination
            just enter the time written on your computer or phone
            you might get incorrect result if your timezone on your
            computer is incorrect look into that.
        
    set <var> = <val>      
        only type the time that you think you have saved.
        postfix y = years
        postfix d = days    
        postfix h = hour
        postfix m = minute
        postfix s = seconds
        example: set food = 30m
                 set food = 1h
                 set food = 1.5h
                 set food = 1800s
    
    delvar <var>
        example: delvar food
    
    cal
        example: cal
    
    autoscrclr
        syntax: autoscrclr true|false
        example: autoscrclr = false to turn auto clearing off
        example: autoscrclr = true to turn auto clearing on
    
    calendar
        syntax calendar <empty or no date> then the current month calendar will be printed
               calendar <date> then the corresponding calendar will be printed
               calendar = <date> same as above
    
    diff    
        syntax: diff <start date> <start time> <end date> <end time>
        example: diff 5/3/2020 17:30:0 4/4/2020 23:12:0

'''
    return output
