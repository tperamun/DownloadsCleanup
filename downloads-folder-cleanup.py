import os
import shutil

source_folder = "/home/timal/Downloads/"
files_in_source_folder = os.listdir(source_folder)



## Paths to the destinations

dest_folder_for_pictures = "/home/timal/Pictures/"
dest_folder_for_videos = "/home/timal/Videos/"
dest_folder_for_zip_files = "/home/timal/Documents/zip_file_archive/"
dest_folder_for_deb_files = "/home/timal/Documents/deb_file_archive/" #Only for debian systems


for file in files_in_source_folder:

    ###For Pictures ###
    if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.jpg'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_pictures, file))


    ### For Videos ###
    if file.endswith('.mov'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_videos, file))

    ## For Zip files ##
    if file.endswith('.zip'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_zip_files, file))

    if file.endswith('.deb'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_deb_files, file))

