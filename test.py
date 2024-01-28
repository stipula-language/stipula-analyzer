'''
test.py
'''
import os
import click



@click.command()
@click.option('-r', '--readable', 'is_readable', type=bool, default=False, show_default=True, is_flag=True, help='Show the output human readable.')
@click.option('-c', '--compact', 'is_compact', type=bool, default=False, show_default=True, is_flag=True, help='Show only the relevant output.')
def _main(is_readable, is_compact):
    entry_list = os.listdir('test')
    entry_list.sort()
    for entry in (entry for entry in entry_list if entry[-8:] == '.stipula'):
        print()
        print('================================================================================')
        print(f"test/{entry}")
        os.system(f"python analyzer.py {('-r ' if is_readable else '')}{('-c ' if is_compact else '')}test/{entry}")



if __name__ == '__main__':
    _main()
