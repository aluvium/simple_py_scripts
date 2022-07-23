import os, subprocess
#creating temp files
# Assume one transaction ends in one day
def extract():
   #start files 
   cmd="cat log.log | grep 'begin' | sort --key=7n | awk '{print $2}' | awk -F ':' '{print $1}' | tr -d '0' > h"
   cmd1="cat log.log | grep 'begin' | sort --key=7n | awk '{print $2}' | awk -F ':' '{print $2}' | tr -d '0' > m"
   cmd2="cat log.log | grep 'begin' | sort --key=7n | awk '{print $2}' | awk -F ':' '{print $3}' | tr -d '.' > s"
   #stop files
   cmd3="cat log.log | grep 'end' | sort --key=7n | awk '{print $2}' | awk -F ':' '{print $1}' | tr -d '0' > h_e"
   cmd4="cat log.log | grep 'end' | sort --key=7n | awk '{print $2}' | awk -F ':' '{print $2}' | tr -d '0' > m_e"
   cmd5="cat log.log | grep 'end' | sort --key=7n | awk '{print $2}' | awk -F ':' '{print $3}' | tr -d '.' > s_e"
   #IDs of transactions
   cmd7="cat log.log | grep 'end' | sort --key=7n | awk '{print$8}' > end-id"
   cmd8="touch total"
   os.system(cmd); os.system(cmd1); os.system(cmd2)
   os.system(cmd3); os.system(cmd4); os.system(cmd5)
   os.system(cmd7); os.system(cmd8)
   return 0

# Cleaning
def clean():
    cmd="rm h m s h_e m_e s_e end-id total"
    e2=os.system(cmd)
    return 0

# open files, converting
def o(arg, mult):
    fo=open(arg, 'r')
    f_list=[]
    var=fo.readlines()
    var2=""
    #6 lists in milisec h,m,s
    l_i_m=[];
    for each in var:
        var2=int(each) * mult
        l_i_m+=[var2]  
    fo.close()
    return l_i_m
# list in milisec trasnasction start/stop; return total time in milisec
def l_i_m_s(a,b,c):
    l_h=o(a, 3600000)
    l_m=o(b, 60000)
    l_s=o(c, 1)
    l_o_l=len(l_h)
    i=0; add=0
    t_l_s=[];
    while i<l_o_l:
        add=int(l_h[i])+int(l_m[i])+int(l_s[i])
        t_l_s+=[add]
        i=i+1
    return t_l_s
# substaraction beetwen lists
def sub_o_lists():
    l_start=l_i_m_s('h','m','s')
    l_stop=l_i_m_s('h_e','m_e','s_e')
    l_o_l=len(l_stop)
    i=0; t_t=0
    wf=open('total','w')
    while i<l_o_l:
        t_t=l_stop[i] - l_start[i]
        i=i+1
        wf.write(str(f'{t_t}\n'))
    wf.close()    
    return 0
# compare shortest time with ID
def comp():
    cmd="cat -n total | sort -k2 | head -1 | awk '{print $1}'"
    sp=subprocess.check_output(cmd, shell=True)
    o=int(sp)
    fo=open('end-id','r')
    var=fo.readlines()
    i=0
    for each in var:
        i=i+1
        if i==o:
            print(each)
    fo.close()
    return 0
# average time
def average():
    fo=open('total','r')
    t_l=fo.readlines()
    l_o_l=len(t_l)
    sum_t=0
    for each in t_l:
        sum_t+=int(each) 
    print(sum_t/l_o_l)
    return 0
def main():
    extract()
    sub_o_lists()
    average()
    clean()
    return 0
main()
