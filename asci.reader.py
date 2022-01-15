import re
path=input('Please provide a path to file in ASCII code for decoding: ')
fo=open(path,'r')
#open file
z=(fo.read())
print('\nThis is the content of the file: ')
print(z)
print('\n')

data=(re.findall(r"\d+\d", z))
#print a file as a string
fo.close()

answ=''
for each in data:
    y=(chr(int(each)))
    answ=answ+y

#conversion to int and ascii by chr and int
print('Decoding message:')
print(answ)
