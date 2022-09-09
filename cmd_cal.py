import global_resource as gr
import datetime
import math


# The smallest unit for calculation supported by this program is seconds
# Hence convert all the time units to second and then perform any calculation

def print_result():
    gr.last_cal_result = "None"
    total_sec = 0.0
    for k, v in gr.data_store["variables"].items():
        sec = gr.convert_to_seconds(v)
        total_sec += sec

    readable = datetime.timedelta(seconds=math.ceil(total_sec))
    time_saved_msg = f"time saved: {readable}"
    gr.last_cal_result = ""
    gr.last_cal_result += time_saved_msg
    print(time_saved_msg)

    if gr.data_store["start_time"]:  # make this check to see if the user has entered start_time
        current_time = datetime.datetime.now().timestamp()
        elapsed_time = current_time - gr.data_store["start_time"]
        time_waste = elapsed_time - total_sec
        readable = datetime.timedelta(seconds=math.ceil(time_waste))
        time_waste_msg = f"time wasted: {readable}"
        print(time_waste_msg)
        gr.last_cal_result += "\n"
        gr.last_cal_result += time_waste_msg

    return True
