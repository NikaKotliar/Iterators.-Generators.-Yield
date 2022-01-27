from datetime import date
from datetime import datetime
from pathlib import Path


def path_to_logs(path):
    def decor_logs(a):
        def add_datatime(*args, **kwars):
            path_to_save = Path(path, 'log_file.txt')
            with open(path_to_save, 'w', encoding='utf-8') as f:
                f.write(f'''Дата:{date.today()}\nВремя:{datetime.now().time()}\nВызвана функция - {a.__name__} \nС аргументами:{args, kwars}''')
            result = a(*args, **kwars)
            return result
        return add_datatime
    return decor_logs


@path_to_logs(path='C:\HomeworkNetology')
def a(n):
    for a in range(n):
        print ('*', end='')

if __name__ == '__main__':
    a(5)
