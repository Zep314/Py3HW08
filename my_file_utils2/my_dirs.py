import os

def get_dirs(path):
    """
    Функция получает на вход начальный каталог, и возвращает в виде словаря внутреннюю
    структуру этого каталога
    :param path:
    :return:
    """
    ret = []
    for dr in os.listdir(path):
        obj_path = os.path.join(path, dr)
        is_dir = True if os.path.isdir(obj_path) else False
        if not is_dir:
            ret.append({"name": dr, "data": {"parent": path, "is_dir": is_dir, "size": os.stat(obj_path).st_size}})

        # if os.path.isdir(abs_path):
        #     print('dir')
        #     get_dirs(abs_path)

    return ret
