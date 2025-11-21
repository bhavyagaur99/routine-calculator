import routine_calculator.global_resource as gr


def print_last_result():
    if gr.last_cal_result:
        print('last result:')
        print(gr.last_cal_result)
    else:
        print('last result: None')
