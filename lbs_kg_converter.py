#ALUVIUM - Metric system to US standard converter
import sys
import time

#-----------------------------------------------------------MENU LAYOUT
def menu():
    print("""
    ------------------->
    Please press:\n
    '1' for lbs to kg,\n
    '2' for kg to lbs,\n
    '3' for meters to foot,\n
    '4' for foot to meters\n\n
    'q 'for exit
    ------------------->
    """)
    return None
#-----------------------------------------------------------LOOP
def cho_loop(ch):
    if ch=='1':
        print('Lbs to Kg converter\n')
    elif ch=='2':
        print('Kg to Lbs converter\n')
    elif ch=='3':
        print('Meteres to foot converter\n')
    elif ch=='4':
        print('Foot to meters converter\n')
    elif ch=='q':
        print('\nBye, Bye!!\n')
        sys.exit()
    else:
        print('Please try again - wrong input.')
        ch=input("\n")
        cho_loop(ch)
    return None

#-----------------------------------------------------------CALCUL CONDITIONS
def calc_loop(ch,a):
    if ch=='1':
        result=a*0.4535
        print(f'The output is {round(result,2)} kg.')
    elif ch=='2':
        result=a*2.20
        print(f'The output is {round(result,2)} lbs.')
    elif ch=='3':
        result=a*3.2808
        print(f'The output is {round(result,2)} foots.')
    else:
        result=a*0.3048
        print(f'The output is {round(result,2)} meters.')
    return None

#-----------------------------------------------------------MAIN
def main():
    ch=0
    while ch!='q':
        menu()
        ch=input("\n")
        cho_loop(ch)
        in_nr=''
        while not in_nr.isdecimal():
            in_nr=input('Enter the number for convertion: ')
            if in_nr=='q':
                sys.exit()

        in_nr=int(in_nr)
        calc_loop(ch,in_nr)
        time.sleep(2)
    return None
#-----------------------------------------------------------START
main()
