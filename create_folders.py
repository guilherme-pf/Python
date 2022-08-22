from importlib.resources import path
import os

root_path = "C:/Users/guilh/Documents/GitHub/Python"

list_folders = []

for i in range(10, 101):
    list_folders.append("Day" + str(i))

for folders in list_folders:
    path = os.path.join(root_path, folders)
    os.mkdir(path)