#ALUVIUM
#Simple programm which shows you amount of days before you die- based on your imput.
import os
import time
import dead_art
os.system('cls')
dead_art.d_a()
# VERSION 1
age=eval(input('Enter your age: '))
age_d=age*356
print(f'You already live approximately {age_d} days.')

dead=eval(input("\n\nAverage Life Expectancy for people is 75 years. \nWhat do You think? How many years are you going to live: "))
dead_d=dead*356
print("\n\nThis is rest of your life.")
time.sleep(2)

for each in range(dead_d-age_d+1):
    print(f'This is your {each} day')
    #time.sleep(0.0000001)

print ('\n + + + R. I. P. + + +')
print(f'\nYou have still {each} days of living.\nSpend it wisely. Happy living!! :).')
