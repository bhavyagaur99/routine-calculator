def get_int(start='>>> ', min_range='-inf', max_range='+inf', retryonerror=True, print_value=False):
    number = 'Error'
    while True:
        okay = True
        msg = input(start)
        try:
            number = int(msg)
        except Exception as e:
            print('Error:', e)
            input('Hit enter to continue  .  .  .')
            okay = False
        if min_range != '-inf' and okay:
            if number < min_range:
                print('Error: Number must be greater than or equal to:', min_range)
                input('Hit enter to continue  .  .  .')
                okay = False
        if max_range != '+inf' and okay:
            if number > max_range:
                print('Error: Number must be smaller than or equal to:', max_range)
                input('Hit enter to continue  .  .  .')
                okay = False
        if not okay:
            if not retryonerror:
                break
        else:
            break
    if print_value:
        print('Last input:', number)
    return number


def get_float(start='>>> ', min_range='-inf', max_range='+inf', retryonerror=True, print_value=False):
    number = 'Error'
    while True:
        okay = True
        msg = input(start)
        try:
            number = float(msg)
        except Exception as e:
            print('Error:', e)
            input('Hit enter to continue  .  .  .')
            okay = False
        if min_range != '-inf' and okay:
            if number < min_range:
                print('Error: Number must be greater than or equal to:', min_range)
                input('Hit enter to continue  .  .  .')
                okay = False
        if max_range != '+inf' and okay:
            if number > max_range:
                print('Error: Number must be smaller than or equal to:', max_range)
                input('Hit enter to continue  .  .  .')
                okay = False
        if not okay:
            if not retryonerror:
                break
        else:
            break
    if print_value:
        print('Last input:', number)
    return number


def get_string(start='>>> ', min_len=0, max_len='+inf', retryonerror=True, print_value=False):
    msg = 'Error'
    while True:
        okay = False
        msg = input(start)
        if min_len <= len(msg) <= max_len:
            okay = True
        else:
            print(f'\nError: The string must be between {min_len} and {max_len}\n')
        if not okay:
            if not retryonerror:
                break
        else:
            break

    if print_value:
        print('Last input:', msg)
    return msg
