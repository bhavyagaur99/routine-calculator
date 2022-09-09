import global_resource as gr
import json


def print_map():
    if not len(gr.data_store):
        print('\nMap is empty\n')
        return True
    print('')
    print('data_store:', json.dumps(gr.data_store, indent=2))
    print('')
    return True
