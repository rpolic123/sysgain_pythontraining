
'''
write a script to create 10 directories in the current directory as below.

dir1
dir2
dir3
dir4
..
..
dir10


'''

import os
try:
    for value in range(1,11):
        dirname = 'dir' + str(value)
        if os.path.isdir(dirname):
            os.rmdir(dirname)
except Exception as err:
    print(err)