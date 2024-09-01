import os, shutil
path = r'C:/Users/Derrick Mao/Downloads/python tutorial/'
file_names = os.listdir(path)

folder_names = ['png files', 'JPG files', 'pdf files']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop])::
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_names:
    if ".png" in file and not os.path.exists(path + folder_names[loop]):

