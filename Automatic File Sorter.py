import os
import shutil

path = r'C:/Users/inegi/Documents/iphone photos/'
file_names = os.listdir(path)

folder_names = ['photos', 'videos']

# Create the folders if they do not exist
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


for file in file_names:
    file_path = os.path.join(path, file)

    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        if not os.path.exists(os.path.join(path, 'photos', file)):
            shutil.move(file_path, os.path.join(path, 'photos', file))

    elif file.lower().endswith(('.mov', '.mp4')):
        if not os.path.exists(os.path.join(path, 'videos', file)):
            shutil.move(file_path, os.path.join(path, 'videos', file))