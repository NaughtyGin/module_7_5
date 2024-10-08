import os
import time


print()
os.chdir('test_dir')  # Иначе печатает слишком много файлов
print('Текущая директория: ', os.getcwd())

print()

directory = ('.')
for root, dirs, files in os.walk(directory):
    for file in files:
        filename = file
        filepath = os.path.abspath(file)
        filepath2 = os.path.join(root, file)
        filetime_create = os.path.getctime(filepath2)
        formatted_time_create = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime_create))
        filetime = os.path.getmtime(filepath2)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath2)
        parent_dir = os.path.dirname(filepath2)
        print(f'Обнаружен файл: {file} \nПуть: {filepath} \nРазмер: {filesize} байт \nВремя создания: '
              f'{formatted_time_create} \nВремя изменения: {formatted_time} \nРодительская директория: {parent_dir}')
