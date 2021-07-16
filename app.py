import zipfile
import os
import shutil
import itertools

src_folder = 'data'
target_folder = 'test_target'
if not os.path.isdir(target_folder):
    raise Exception(f'`{target_folder}` target_folder does not exist')

zip_files = ['data/' + f for f in os.listdir('data') if f.endswith('.zip')]

for file_to_unzip in zip_files:
    print(f'processing: {file_to_unzip}')
    unzip_folder = os.path.splitext(file_to_unzip)[0]

    with zipfile.ZipFile(file_to_unzip) as z:
        z.extractall(unzip_folder)

    existing_albums = [
        x for x in os.listdir(target_folder)
        if os.path.isdir(target_folder + '/' + x)]
    albums = os.listdir(unzip_folder)

    for album in albums:
        album_src_path = unzip_folder + '/' + album
        album_target_path = target_folder + '/' + album
        if not album in existing_albums:
            print(f'copying whole album: {album}')
            shutil.copytree(album_src_path, album_target_path)
        else:
            print(f'album already exists: {album}')
            files_in_album = os.listdir(album_src_path)
            existing_files = os.listdir(album_target_path)

            files_to_copy = [f for f in files_in_album if not f in existing_files]
            print(f'copying {len(files_to_copy)} files to album: {album}')
            for f in files_to_copy:
                shutil.copy(album_src_path + '/' + f, album_target_path)

    shutil.rmtree(unzip_folder)
