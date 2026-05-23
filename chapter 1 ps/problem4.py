# WAP to print to print the contents of a directory using the os model .
# search online for the function which does that.

# Program to print contents of a directory using os module

# Write a program to print the contents of a directory

import os

# specify the directory you want to list 
directory_path = '/'

# list all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name 
for item in contents:
    print(item)
