import global_resource as gr


def set_var(var, val):
    try:
        code = gr.data_store["variables"].get(var, None)
        if code:  # var found update it
            print("updated")
            print(f"old: {var} -> {code}")
            print(f"new: {var} -> {val}")
        else:
            print(f"added {var} -> {val}")

        gr.update_variable_store(var, val)
        return True
    except Exception as e:
        return False
