import os

path = 'your file path'
# path = 'your folder path'

if os.path.exists(path):
    print('exists')
    if os.path.isfile(path):
        print('that is a file')
    elif os.path.isdir(path):
        print('that is a directory')
else:
    print('location not found.')
