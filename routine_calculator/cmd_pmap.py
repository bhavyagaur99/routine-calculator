import routine_calculator.global_resource as gr
import json
import yaml
import datetime


def print_map():
    if not len(gr.data_store):
        print('no data present')
        return False
    
    if gr.data_store and gr.data_store.get('variables'):
        print("items")
        print("-----")
        print(yaml.dump(gr.data_store.get('variables')))
    
    if gr.data_store and gr.data_store.get('start_time'):
        start = datetime.datetime.fromtimestamp(gr.data_store.get('start_time'))
        formatted_time = start.strftime("%d/%m/%Y %H:%M:%S")
        print("start time")
        print("----------")
        print(formatted_time)
    
    return True
