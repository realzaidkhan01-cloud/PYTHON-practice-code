import os

# specify the directory you want to list
directory_path = '/'

# list all files in the directory in the specified path
contents = os.listdir(directory_path)

# print the contents:
for item in contents:
    print(item)