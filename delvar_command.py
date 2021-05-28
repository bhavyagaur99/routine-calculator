import global_resource as gr


def remove_var(var):
    code = gr.variable_store.pop(var, None)
    if code:
        print(f"deleted {var} -> {code}")
    else:
        print(f"Error: ({var}) not found")
    return
