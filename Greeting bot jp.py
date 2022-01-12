# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Greeting Bot that also checks if you've had lunch in the afternoon.Includes loop if wrong input is entered. (Japanese version) COMPLETE

名前 = input('名前を入力してください')
print(f"こんにちは{名前}さん。はじめまして!")
while True:
    try:
        時間 = int(input('今は何時ですか?'))
        break
    except (ValueError):
        print('数字だけ入力してください. 例 - 09:00 = 0900')


if 時間<1200:
    print('おはようございます！今日は頑張りましょう！')
else:
    if 時間<1800:
        while True:
            答え = input("こんにちは！お昼ごはんを食べましたか('はい'と'いいえ'で答えてください)")
            if 答え == 'はい':
                昼ごはん = input('何を食べましたか')
                print(f'{昼ごはん}は美味しいですねー。私も食べいたいなー')
                break
            elif 答え == 'いいえ':
                print('早く食べなさい！')
                break
            else:
                print('はいかいいえで答えなさい')
    else:
        print('おやすみなさい!')
        
print('終了')
