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
