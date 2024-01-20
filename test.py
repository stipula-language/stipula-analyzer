'''
test.py
'''
import os



if __name__ == '__main__':
    entry_list = os.listdir('test')
    entry_list.sort()
    for entry in (entry for entry in entry_list if entry[-8:] == '.stipula'):
        print()
        print('================================================================================')
        print(f"test/{entry}")
        os.system(f"python analyzer.py test/{entry}")
