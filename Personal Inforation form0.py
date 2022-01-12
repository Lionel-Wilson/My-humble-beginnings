# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:00:37 2021

@author: Lione
"""

#Personal information form. Returns all personal inforomation after filled. (English version) COMPLETE

print('Please fill in the form for our records')

First_name = input('First Name - ')

Middle_name = input("Middle name (If you don't have one please type n/a) - ")

Surname = input('Surname - ')

Street_Address = input('Street Address - ')

pcode = input('Post code - ')

while True:
    try:
        Phone_number = int(input('Phone number - '))
        break
    except (ValueError):
        print('Please insert only numbers. e.g. 07543291918')

while True:
    Gender = input("Gender(Male/Female) - ")
    if Gender == 'male':
        print(f"Gender(Male/Female) - {Gender}")
        break
    elif Gender == 'female':
        print(f"Gender(Male/Female) - {Gender}")
        break
    else:
        print('Please choose male or female')

print(f"\n\n\nFirst Name - {First_name}\nMiddle Name - {Middle_name}\nSurname - {Surname}\nAddress - {Street_Address} {pcode}\nPhone Number - {Phone_number}\nGender - {Gender}")
print('\nForm Complete')