import global_resource as gr


def remove_var(var):
    code = gr.data_store['variables'].pop(var, None)
    if code:
        print(f'Deleted: {var} -> {code}')
    else:
        print(f'Error: variable does not exist')
    return
