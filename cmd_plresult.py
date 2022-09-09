import global_resource as gr


def print_last_result():
    if gr.last_cal_result:
        print('last result was:')
        print(gr.last_cal_result)
    else:
        print('you have not performed calculation till now')
