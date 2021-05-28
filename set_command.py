import global_resource as gr


def set_var(var, val):
    code = gr.variable_store.get(var, None)
    if code:  # var found update it
        print("updated")
        print(f"old: {var} -> {code}")
        print(f"new: {var} -> {val}")
    else:
        print(f"added {var} -> {val}")

    gr.variable_store[var] = val
    return True

