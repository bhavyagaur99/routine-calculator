import os
import json
import global_resource as gr


def save(filename):
    print("filename =", filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    store_data = [gr.variable_store, gr.start_time]
    with open(filename, "w") as f:
        json.dump(store_data, f)
