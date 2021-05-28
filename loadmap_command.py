import global_resource as gr
import json


def load(filename):
    print("filename =", filename)
    try:
        with open(filename, "r") as f:
            data = f.read()
            store_data = json.loads(data)
            gr.variable_store = store_data[0]
            gr.start_time = store_data[1]
    except FileNotFoundError:
        print("File does not exit")
