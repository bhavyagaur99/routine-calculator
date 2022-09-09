import global_resource as gr
import json


def load(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            data_json = json.loads(data)

            if type(data_json) == list:
                version = '0.0'
            else:
                version = data_json['version']

            if version == '0.0':  # old style version 0 upgrade to data_store_version style
                gr.data_store['version'] = gr.data_store_version
                gr.data_store['variables'] = data_json[0]
                gr.data_store['start_time'] = data_json[1]
            elif version == '1.0':
                gr.data_store = data_json
    except FileNotFoundError:
        print('File does not exit')
