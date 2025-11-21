import os
import json
import routine_calculator.global_resource as gr


def savemap(filename: str, data_store: dict):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(data_store, f, indent=2)
    return None, True
