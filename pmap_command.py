import global_resource as gr


def print_map():
    if not len(gr.variable_store):
        print("\nMap is empty\n")
        return True
    print("")
    for k, v in gr.variable_store.items():
        print(k, "=", v)
    print("")
    return True
