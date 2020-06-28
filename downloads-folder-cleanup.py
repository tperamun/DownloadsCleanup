import os
import shutil

source_folder = "/home/timal/Downloads/"
files_in_source_folder = os.listdir(source_folder)

dest_folder_for_pictures = "/home/timal/Pictures/"

picture_files = ["*.jpeg", "*.png", "*.jpg"]


### For Pictures ###

for file in files_in_source_folder:
    if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.jpg'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_pictures, file))


