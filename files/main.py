__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


import os
from zipfile import ZipFile


padA = os.getcwd()
cache_dir = os.path.join(padA, "cache")
data_dir = os.path.join(padA, "data.zip")


def main():
    cache_zip()
    print(find_password(cached_files()))
    return


def clean_cache():
    if os.path.isdir(cache_dir):
        print('cache already exists, empty cache')
        '''empty cache'''
        for file in os.listdir(cache_dir):
            file_in_cache_dir = os.path.join(cache_dir, file)
            os.remove(file_in_cache_dir) 
    else:
        os.makedirs(cache_dir)
    return


def cache_zip(zip_file_path:str=data_dir,cache_dir_path:str=cache_dir):
    '''unpack indicated zip file in to clean cache'''
    clean_cache()

    with ZipFile (zip_file_path, 'r') as zipObj:
        zipObj.extractall(path=cache_dir_path)
    return


def cached_files():
    '''create list of absolute file paths'''
    absolute_cache_path = os.path.abspath('cache')
    print('absolute cache path: ', absolute_cache_path)
    files_in_cach = []
    for file in os.listdir(cache_dir):
            files_in_cach.append(os.path.join(absolute_cache_path, file)) 
    return files_in_cach

def find_password(search_list):
    '''find and return the password'''
    for file in search_list:
        reader = open(file, 'r')
        try:
            text = reader.read()
            if 'password' in text:
                print(f'password found in {file}')
                end_password = text.find('password')+10
                found = text[end_password:text.find('\n', end_password)]
                return found
        finally:
            reader.close()
    return 'can not find password'


if __name__ == '__main__':
    main()