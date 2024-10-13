from pathlib import Path
import os
import shelve
# генерим путь для создания нового файла

file_path = Path('auto_pr/rw_files')


def get_file_path(path_string):
    gen_path = Path.cwd() / path_string
    return gen_path

# def get_file_path():
#     # print(Path.cwd())
#     relative_path = Path('auto_pr/rw_files')
#     gen_path = Path.cwd() / relative_path
#     return gen_path

# открываем и читаем файл. Прокидываем имя файла и его тип


def read_file(file_name):
    open_file = open(get_file_path() / file_name)
    read_file_content = open_file.read()
    open_file.close()
    return read_file_content

# открываем и читаем файл. Прокидываем имя файла и его тип
# читает построчно и возвращает массив строк


def read_lines(file_name):
    open_file = open(get_file_path() / file_name)
    read_lines_file_content = open_file.readlines()
    open_file.close()
    return read_lines_file_content

# открываем и перезаписываем файл. закрываем
# если прокинутого файла нет, то создаем его


def rewrite_file(file_name, content):
    open_file_wmode = open(get_file_path() / file_name, 'w')
    rewrite_content = open_file_wmode.write(f'{content}\n')
    open_file_wmode.close()
    return rewrite_content

# добавляем котент к файлу не презаписывая его


def add_to_file(file_name, content):
    open_file_amode = open(get_file_path() / file_name, 'a')
    add_content = open_file_amode.write(f'{content}\n')
    open_file_amode.close()
    return add_content

# shelve module


shelf_file = shelve.open(get_file_path() / 'my_data')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats

dogs = ['Woof', 'Woofy', 'Gav']
shelf_file['dogs'] = dogs
print(type(shelf_file))
# print(shelf_file['cats'])
# print(shelf_file['dogs'])
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()
