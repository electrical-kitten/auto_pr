import shutil
import os
from pathlib import Path

# сощздаем локальный корневой путь
local_path = Path.home()

# 1arg. прокидываем в метод корневой путь и копируем оттуда файл (source)
# 2arg. прокидываем папку назначения (destination)
# shutil.copy(local_path / 'spam.txt', local_path / 'Documents')

# # копируем все дерево папок и создаем папку куда будем копировать
# shutil.copytree(local_path / 'some_folder', local_path / 'some_folder_backup')

# перемещаем папку или файл
# shutil.move(local_path / 'some_folder', local_path / 'Documents')

# перемещаем файл в папку и переименовываем его
# shutil.move(local_path / 'example_file.txt', local_path /
#             'Documents' / 'moved_example_file.txt')

# deleting files and folders
