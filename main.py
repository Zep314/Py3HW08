

import my_file_utils2 as mfu2

if __name__ == '__main__':
    path = 'C:\\Work\\python\\dz3\\Py3HW08\\my_file_utils2'
    data = mfu2.get_dirs(path)

    mfu2.save_to_json('dir_members.json', data)
    mfu2.save_to_csv('dir_members.csv', data)
    mfu2.save_to_pickle('dir_members.pickle', data)
