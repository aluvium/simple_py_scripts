#ALUVIUM
#Simple tool behaves similar to 'ls' and 'dir' on every system
#Using listdir command from os.path module
import os
import sys
path1=input('Please enter a path:\n')
if os.path.exists(path1):
    fd_l=os.listdir(path1)
else:
    print('Please provide valid path.')
    sys.exit()

list_of_files=os.listdir(path1)
print(f'All files and dirs in the path: \n{list_of_files}\n')
for each_f in list_of_files:
    ffile=os.path.join(path1,each_f)
    if os.path.isfile(ffile):
        print(f'{ffile} is a file')
    else:
        print(f'{ffile} is a dictionary')
