#ALUVIUM
#Fast tool for deep data scan using os.walk
import os
os.system('cls')
path=input('***Please enter a path for searaching: ')
opt=eval(input("\n***Full scan press: 1, \n***Scan all but empty folders press: 2, \n***Scan only files press: 3, \n***Scan only files with paths: 4:\n"))
td=input('\n***Topdown press ------any key, Downtop press ------d\n')

if td=='d':
    if opt==1:
        for p,d,f in os.walk(path,topdown=False):
            print(f'Path: {p}, \nDir: {d}, \nFiles:{f}\n')
    elif opt==2:
        for p,d,f in os.walk(path,topdown=False):
            if len(f) != 0:
                print(f'Path: {p}, \nDir: {d}, \nFiles:{f}\n')
    elif opt==3:
        for p,d,f in os.walk(path,topdown=False):
            if len(f) !=0:
                print(f'Files:\t{f}\n')
    else:
        for p,d,f in os.walk(path,topdown=False):
            if len(f) !=0:
                print(f'Path:{p}')
                for each_f in f:
                    print(os.path.join(p,each_f))
                    print('---------------------------------------------------')
else:
    if opt==1:
        for p,d,f in os.walk(path,topdown=True):
            print(f'Path: {p}, \nDir: {d}, \nFiles:{f}\n')
    elif opt==2:
        for p,d,f in os.walk(path,topdown=True):
            if len(f) != 0:
                print(f'Path: {p}, \nDir: {d}, \nFiles:{f}\n')
    elif opt==3:
        for p,d,f in os.walk(path,topdown=True):
            if len(f) !=0:
                print(f'Files:\t{f}\n')
    else:
        for p,d,f in os.walk(path,topdown=True):
            if len(f) !=0:
                print(f'Path:{p}')
                for each_f in f:
                    print(os.path.join(p,each_f))
                    print('---------------------------------------------------')
