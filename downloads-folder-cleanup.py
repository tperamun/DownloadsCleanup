import os
import shutil

source_folder = "/home/timal/Downloads/"
files_in_source_folder = os.listdir(source_folder)



## Paths to the destinations

dest_folder_for_pictures = "/home/timal/Pictures/"
dest_folder_for_videos = "/home/timal/Videos/"

### For Pictures ###

for file in files_in_source_folder:

    ###For Pictures ###
    if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.jpg'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_pictures, file))


    ### For Videos ###
    if file.endswith('.mov'):
        shutil.move(os.path.join(source_folder, file), os.path.join(dest_folder_for_videos, file))

