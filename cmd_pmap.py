import global_resource as gr
import json


def print_map():
    if not len(gr.data_store):
        print('date_store: None')
        return True
    print('data_store:', json.dumps(gr.data_store, indent=2))
    return True
