import global_resource as gr


def print_var(var):
    code = gr.data_store["variables"].get(var, None)
    if code:
        print(var, "->", code)
    else:
        print(f"Error: ({var}) not found")

