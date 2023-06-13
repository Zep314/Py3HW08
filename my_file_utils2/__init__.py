"""
Init-файл для пакета с моими модулями
"""
from my_file_utils2.my_dirs import get_dirs
from my_file_utils2.files_routine import save_to_json

# Эти функции будем "экспортировать" для внешней работы
__all__ = ['get_dirs', 'save_to_json']
