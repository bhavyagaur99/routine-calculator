import os
import routine_calculator.store as store
import datetime
import routine_calculator.global_resource as gr

def save_by_custom_date(date: datetime.datetime):
    filename = os.path.join(gr.database_path, str(date.year), str(date.month), str(date.day), 'map.json')
    print('Filename:', filename)
    return store.savemap(filename, gr.data_store)
    

def save_by_today():
    return save_by_custom_date(datetime.datetime.today())