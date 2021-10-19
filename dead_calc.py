#ALUVIUM
#Simple programm which shows you amount of days before you die- based on your imput.
import os
os.system('cls')

# VERSION 1
age=eval(input('Enter your age: '))
age_d=age*356
print(f'You already live {age_d} days.')
dead=eval(input("\n\nToday's average lifspan of human being is around 75 years. \nEnter how many years are you going to live: "))
dead_d=dead*356

for each in range(age_d,dead_d):
    print(f'{each} Day')
print ('\nR. I. P.')
print(f'\nYou have still {len(range(age_d,dead_d))} days of living. Spend it wisely.\nHappy living :).')
