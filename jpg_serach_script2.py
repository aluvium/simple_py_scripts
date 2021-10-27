#JPG Segregator
import os
import shutil
from datetime import datetime
#-------------------------------------------------------------------------------
def copyf(f_pat,des_pat):
    try:
        shutil.copy2(f_pat,des_pat)
    except:
        print('File already exists')
    return None

pat=input('Please input valid path with data: \n')
typ1='.jpg'
typ2=typ1.upper()
year_f='2021'

i='d:\\'+year_f+'\I'
ii='d:\\'+year_f+'\II'
iii='d:\\'+year_f+'\III'
iv='d:\\'+year_f+'\IV'
#-------------------------------------------------------------------------------
try:
    os.mkdir('d:\\'+year_f)
    os.mkdir(i)
    os.mkdir(ii)
    os.mkdir(iii)
    os.mkdir(iv)
except:
    print('Folders aleardy exists')
#-------------------------------------------------------------------------------

for p,d,f in (os.walk(pat)):
    for each_f in f:
    #Fullpath to jpg
        f_pat=os.path.join(p,each_f)
        if f_pat.endswith(typ1) or f_pat.endswith(typ2):
            #File timestamp
            f_time=datetime.fromtimestamp(os.path.getmtime(f_pat))
            y=f_time.strftime('%Y')
            m=int(f_time.strftime('%m'))
            if y==year_f and m<=3:
                copyf(f_pat,i)
            elif y==year_f and m>3 and m<=6:
                copyf(f_pat,ii)
            elif y==year_f and m>6 and m<=9:
                copyf(f_pat,iii)
            elif y==year_f and m>9:
                copyf(f_pat,iv)
            else:
                print("Something went wrong")

#-------------------------------------------------------------------------------
