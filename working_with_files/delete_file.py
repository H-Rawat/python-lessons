# cant remove empty folder

import os
import shutil

# path = 'text.txt'
path = 'test'

try:
    # os.remove(path)
    os.rmdir(path)
    # shutil.rmtree(path)
except FileNotFoundError:
    print('file was not found')
except PermissionError:
    print('you do not have permissions to delete that')
except OSError:
    print('you can not delete that using os.rmdir')
else:
    print(path + ' was deleted')
