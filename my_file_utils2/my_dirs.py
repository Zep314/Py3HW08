import os

def get_dirs(path):
    """
    Функция получает на вход начальный каталог, и возвращает в виде словаря внутреннюю
    структуру этого каталога
    - Указывается родительская директория.
    - Указывается файл это или директория.
    - Для файлов указывается его размер в байтах, а для директорий размер файлов
      в ней с учётом всех вложенных файлов и директорий.
    :param path:
    :return:
    """
    ret = {}
    dir_size = 0
    for dr in os.listdir(path):
        obj_path = os.path.join(path, dr)
        if not os.path.isdir(obj_path):
            ret[dr] = {"parent": path, "is_dir": False, "size": os.stat(obj_path).st_size}
            dir_size += os.stat(obj_path).st_size
        else:
            ret[dr] = {"parent": path, "is_dir": True, "size": os.stat(obj_path).st_size}
        # else:
        #     ret.append()
        # if os.path.isdir(abs_path):
        #     print('dir')
        #     get_dirs(abs_path)

    return ret
