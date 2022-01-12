# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

# refactoring

while True:
    difficulty = input('Please choose your difficulty - easy, medium or hard ')
    count = 0
#Easy difficulty block
    if difficulty == 'easy':
        maxnume = 20
        minnume = 0
        secreteasy = random.randint(minnume,maxnume)
        while True:
            try:
                guess = int(input("Guess the number I'm thinking of..."))
            except ValueError:
                print("Please insert a number!")
                continue
            if guess<minnume or guess>maxnume:
                print('The easy difficulty sets the number between 1 and 20. Try again')
                continue
            count = count + 1
            if guess>secreteasy:
                print('My number is lower. Try again')
            elif guess<secreteasy:
                print('My number is higher. Try again')
            else:
                print(f'WELL DONE! you got it in {count} attempts')
                break

#Medium difficulty      
    if difficulty == 'medium':
        maxnumm = 50
        minnumm = 0
        secretmedium = random.randint(minnumm,maxnumm)
        while True:
            try:
                guess = int(input("Guess the number I'm thinking of..."))
            except ValueError:
                print("Please insert a number!")
                continue
            if guess<minnumm or guess>maxnumm:
                print('The medium difficulty sets the number between 1 and 50. Try again')
                continue
            count = count + 1
            if guess>secretmedium:
                print('My number is lower. Try again')
            elif guess<secretmedium:
                print('My number is higher. Try again')
            else:
                print(f'WELL DONE! you got it in {count} attempts')
                break
    
#Hard difficulty
    if difficulty == 'hard':
        maxnumh = 200
        minnumh = 0
        secrethard = random.randint(minnumh,maxnumh)
        while True:
            try:
                guess = int(input("Guess the number I'm thinking of..."))
            except ValueError:
                print("Please insert a number!")
                continue
            if guess<minnumh or guess>maxnumh:
                print('The hard difficulty sets the number between 1 and 200. Try again')
                continue
            count = count + 1
            if guess>secrethard:
                print('My number is lower. Try again')
            elif guess<secrethard:
                print('My number is higher. Try again')
            else:
                print(f'WELL DONE! you got it in {count} attempts')
                break
    elif difficulty != 'easy'or'medium'or'hard' :
        print("Please type 'easy','medium' or 'hard'")
        continue
    
