import global_resource as gr


def print_var(var):
    code = gr.variable_store.get(var, None)
    if code:
        print(var, "->", code)
    else:
        print(f"Error: ({var}) not found")

