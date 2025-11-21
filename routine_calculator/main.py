import routine_calculator.input as imp
import routine_calculator.global_resource as gr
import routine_calculator.load as load
import routine_calculator.command as command


def main():
    filename = gr.get_savefile_name()
    load.load(filename=filename)

    print(gr.get_today(), gr.time_format_1())
    print('Type "help me" to print help')


    while True:
        try:
            print()
            inpcmd = imp.get_string(start='routinecal >>> ', min_len=2, max_len=4096)
            print()
            if not command.execute(inpcmd):
                print('Error: syntax or format error type "help me"')
        except Exception as e:
            print('Error: ', e)

if __name__ == '__main__':
    main()
