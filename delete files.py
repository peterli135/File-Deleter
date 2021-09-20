"""
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you’re trying to free up room on your computer,
you’ll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB.
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.
"""

import os, send2trash

while True:
    temp_files = input('Please input the path folder you want to delete: ').encode()
    print(f'Files to be deleted are: {os.listdir(temp_files)}')
    continue_to_delete = input('Do you wish to continue? (y/n): ')
    if continue_to_delete == 'y':
        for foldername, subfolders, filenames in os.walk(temp_files):
            for subfolder in subfolders:
                try:
                    subfolders_in_tempfolder = os.path.join(foldername, subfolder)
                    print(f'Deleted: {subfolders_in_tempfolder}.')
                    send2trash.send2trash(subfolders_in_tempfolder)
                except Exception as Err:
                    print(f'An error occurred: {Err}')
            for filename in filenames:
                try:
                    files_in_tempfolder = os.path.join(foldername, filename)
                    print(f'Deleted: {files_in_tempfolder}.')
                    send2trash.send2trash(files_in_tempfolder)
                except Exception as Err:
                    print(f'An error occurred: {Err}')
    elif continue_to_delete == 'n':
        print('The function will not continue.')
        break
    else:
        print('Please enter a valid (y/n).')
    another_folder_to_delete = input("Do you wish to delete another folder's contents? (y/n): ")
    if another_folder_to_delete == 'y':
        continue
    elif another_folder_to_delete == 'n':
        print('The function will not continue.')
        break
    else:
        print('Please enter a valid input.')
