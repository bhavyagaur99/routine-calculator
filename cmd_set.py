import global_resource as gr


def set_var(var, val):
    try:
        val_old = gr.data_store['variables'].get(var, None)
        if val_old:  # var found update it
            print(f'Updated: {var} from {val_old} to {val}')
        else:
            print(f'Created: {var} -> {val}')

        gr.update_variable_store(var, val)
        return True
    except Exception as e:
        return False
