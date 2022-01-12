# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:07:34 2021

@author: Lionel
"""
def guesser(maxnum, minnum):#This function generates the guesses of the computer.
    return ((maxnum-minnum)//2)+minnum

def liedetect(maxnum,minnum): #This is a function that does the lie detection. I tried to capture most of the posisble situations where the user could be lying. It may miss some situations however.
    if guess==(maxnum-1):
        if answer=='>':
            print(f'YOU LIAR! Earlier you said your number was less than {maxnum}')
            return False
        else:
            return
    if guess==(minnum+1):
        if answer=='<':
            print(f'YOU LIAR! Earlier you said your number was greater than {minnum}')
            return False
        else:
            return
    if guess==minnum and guess==maxnum:
        if answer=='<' or '>':
            print("YOUR'E LYING!")
            return False
    if guess==(minnum+1) and guess==(maxnum-1):
        if answer=='<' or '>':
            print('YOU LIAR! THIS IS THE NUMBER YOU WERE THINKING OF!')
            return False
        else:
            return
            
minimum =1 #Set the minimum that your number could posssibly be
maximum = 100 #set the maximum that your number could possibly be
count = 0
guess= guesser(maximum,minimum)

print(f'Think of a number between {minimum} and {maximum}')
while True:
    answer = input(f"is your number greater(>), equal(=), or less(<) than {guess}")
    if liedetect(maximum, minimum)==False: 
        break
    if answer=='>':
        minimum=guess
        guess = guesser(maximum,minimum)
        count+=1
        continue
    elif answer=='<':
        maximum = guess 
        guess=guesser(maximum,minimum)
        count+=1
        continue
    elif answer=='=':
        count+=1
        print(f'I have guessed it!\nI needed {count} attempts')
        break
    else:
        print("Please answer with '>','< or '='")
        continue
print('End')