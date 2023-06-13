
import my_file_utils2 as mfu2

if __name__ == '__main__':
    path = 'c:\_Export'
    data = mfu2.get_dirs(path)
    print(data)
    mfu2.save_to_json('dir_members.json', data)
