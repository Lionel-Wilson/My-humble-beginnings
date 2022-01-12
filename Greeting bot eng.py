# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
name = input('What is your name?')
print(f"Hello {name}. Nice to meet you!")
while True:
    try:
        time = int(input('What time is it right now?'))
        break
    except ValueError:
        print('Please input time with numbers. Following the format - 09:00 = 0900')


if time<1200:
    print("Good morning! Let's go hard today!")
else:
    if time<1800:
        while True:
            ans = input("Good afternoon! Have you had lunch? (Please answer with 'yes'or 'no')")
            if ans == 'yes':
                lunch = input('What did you eat?')
                print(f'{lunch} SLAPPPPPS。I might have to order some right now!')
                break
            elif ans == 'no':
                print('Bro, hurry up and go eat lunch!')
                break
            else:
                print("My G, I said 'answer with 'yes'or 'no'. Are you silly?")
    else:
        print('Good night!')
        
print('Done')
