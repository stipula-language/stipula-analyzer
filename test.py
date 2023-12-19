'''
test.py
'''
import os



if __name__ == '__main__':
    for entry in os.listdir('test'):
        print()
        print('================================================================================')
        print(f"test/{entry}")
        os.system(f"python analyzer.py test/{entry}")
