import os, shutil
path = r'C:/Users/Derrick Mao/Downloads/'
file_names = os.listdir(path)

folder_names = ['png files', 'JPG files', 'pdf files']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_names:
    if ".png" in file and not os.path.exists(path + 'png files/' + file):
        shutil.move(path + file, path + 'png files/' + file )
    elif ".pdf" in file and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file, path + 'pdf files/' + file )
    elif ".JPG" in file and not os.path.exists(path + 'JPG files/' + file):
        shutil.move(path + file, path + 'JPG files/' + file )