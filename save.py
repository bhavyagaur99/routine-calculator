import os
import json


def save(filename, data_store):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data_store, f, indent=2)
