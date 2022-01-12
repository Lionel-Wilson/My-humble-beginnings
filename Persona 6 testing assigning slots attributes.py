# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:11:47 2021

@author: Lione
"""

import random

class Hero:
    def __init__(self,name="Lionel",class_name="Hero",newmove_1= "Thorn Cage", newmove1_dmg = 2,newmove1_energy = 35 ):
        self.health = 100
        self.max_health = 100
        self.energy=100
        self.max_energy = 100
        self.name = name
        self.starting_level = 1
        self.max_level = 50
        self.normal_attack = "Sword Slash"
        self.normal_attack.na_energy = 10
        self.normal_attack.na_dmg = 8
        self.special_attack = "Soul Caliber Strike"
        self.special_attack.sa_energy=40
        self.special_attack.sa_dmg = 25
        self.restore_move="Heavenly Restoration"
        self.restore_move.restore = 15
        self.newmove_1= newmove_1
        self.newmove_1.newmove1_dmg = newmove1_dmg
        self.newmove_1.newmove1_energy = newmove1_energy 
        self.newmove_2 = None
        self.newmove2_descrip = None
        self.newmove2_dmg = None
        self.newmove2_energy = None
        self.class_name =class_name
        self.battle_slot1 = "Empty"
        self.battle_slot2 = "Empty"
        self.battle_slot3 = "Empty"
        self.battle_slot4 = "Empty"
        self.inven_slot1 = self.normal_attack
        self.inven_slot2 = self.special_attack
        self.inven_slot3 = self.restore_move
        self.inven_slot4 = self.newmove_1
        self.inven_slot5 = "Empty"
        self.inven_slot6 = "Empty"
        
    def hero_norm_attack(self,target):
        miss_chance = random.randint(0,100)
        if miss_chance<=80:
            if self.energy>=self.na_energy:
                self.energy = self.energy-self.na_energy
                print(f"{self.name} attacked {target.name} with {self.normal_attack} and dealt {self.na_dmg} damage to {target.name}")
                target.health = target.health-self.na_dmg
                if target.health <=0:
                    print(f"Well done! you defeated {target.name}")
                    return 
            else:
                print(f"\nYou haven't got enough energy to use '{self.normal_attack}'")
                return
        if miss_chance>80:
            if self.energy>=self.na_energy:
                self.energy = self.energy-self.na_energy
                print(f"{self.name} attacked {target.name} with {self.normal_attack} but missed!")
                target.health = target.health-0
                if target.health <=0:
                    print("Well done! you defeated {target.name}")
                    return 
            else:
                print(f"\nYou haven't got enough energy to use '{self.normal_attack}'")
                return
    def battle(self,foe):
        print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
        while True: 
            chosen_move = input(f"1. {self.battle_slot1}  - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2. {self.battle_slot2} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3. {self.battle_slot3} - Restores {self.restore} EP\n4. {self.battle_slot4}- Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n")
            if chosen_move == "1":
                self.hero_norm_attack(foe)
                if foe.health<=0:
                    break
                enemy_attack_choser = random.randint(1,4)
                if enemy_attack_choser>=2:
                    foe.enemy_na_attack(self)#Sort out what happens when you die. make a die function where it allows you to restart.
                    if self.health<=0:
                        game_over()
                        return 
                elif enemy_attack_choser<2:
                    foe.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
                        return
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
                
            elif chosen_move=="2":
                self.hero_sp_attack(foe)
                if foe.health<=0:
                    print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                    break
                enemy_attack_choser = random.randint(1,4)
                if enemy_attack_choser>=2:
                    foe.enemy_na_attack(self)
                    if self.health<=0:
                        game_over()
                        return 
                elif enemy_attack_choser<2:
                    foe.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
                        return
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
                
            elif chosen_move=="3":
                self.energy_restore()
                if foe.health<=0:
                    print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                    break
                enemy_attack_choser = random.randint(1,4)
                if enemy_attack_choser>=2:
                    foe.enemy_na_attack(self)
                    if self.health<=0:
                        game_over()
                        return 
                elif enemy_attack_choser<2:
                    foe.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
                        return
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
            elif chosen_move=="4":
                self.para_attack(foe)
                if self.health<=0:
                        game_over()
                        return 
                if foe.health<=0:
                    print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                    print("Well done! you defeated {target.name}")
                    break
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
            else:
                print("Please select 1,2,3 or 4")
        return
            
    def paralysed_enemy_battle(self,foe):
        remaining_turns = 2
        while True: 
            chosen_move = input(f"1. {self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2. {self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3. {self.restore_move} - Restores 15 EP\n4. {self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n")
            if chosen_move == "1":
                self.hero_norm_attack(foe)
                foe.health = foe.health-self.newmove1_dmg
                print(f"{foe.name} misses turn due to paralysis")
                remaining_turns-=1
                if remaining_turns==0:
                    return
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
                
            elif chosen_move=="2":
                self.hero_sp_attack(foe)
                foe.health = foe.health-self.newmove1_dmg
                print(f"{foe.name} misses turn due to paralysis")
                remaining_turns-=1
                if remaining_turns==0:
                    return
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
            elif chosen_move=="3":
                self.energy_restore()
                foe.health = foe.health-self.newmove1_dmg
                print(f"{foe.name} misses turn due to paralysis")
                remaining_turns-=1
                if remaining_turns==0:
                    return
                print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
            elif chosen_move=="4": #paralysis move
                self.para_attack(foe)
                return
            else:
                print("Please select 1,2 or 3")
    
    def hero_sp_attack(self,target):
        miss_chance = random.randint(0,100)
        if miss_chance<=70:
            if self.energy>=self.sa_energy:
                self.energy = self.energy-self.sa_energy
                print(f"{self.name} attacked {target.name} with {self.special_attack} and dealt {self.sa_dmg} damage to {target.name}")
                target.health = target.health-self.sa_dmg
                if target.health <=0:
                    print(f"Well done! You defeated {target.name}!")
                    return 
            else:
                print(f"You haven't got enough energy to use '{self.special_attack}'")
                return
        if miss_chance>70:
            if self.energy>=self.sa_energy:
                self.energy = self.energy-self.sa_energy
                print(f"{self.name} attacked {target.name} with {self.special_attack} but missed!")
                target.health = target.health-0
                if target.health <=0:
                    print(f"Well done! You defeated {target.name}!")
                    return 
            
    def energy_restore(self):
        if self.energy+self.restore<100:
            self.energy=self.energy+self.restore
            print(f"{self.name} restored {self.restore} energy points with '{self.restore_move}'")
            return
        else:
            print("You have enough energy")
            return
    def restore_all(self):# A function that restores all HP and EP. used after battles.
        if self.health!=self.max_health:
            self.health=self.max_health
        if self.energy!=self.max_energy:
            self.energy=self.max_energy
        return
            
    def para_attack(self,target): 
        miss_chance = random.randint(0,100)
        if miss_chance<=80: #Chance of not missing
            if self.energy>=self.newmove1_energy:
                self.energy = self.energy-self.newmove1_energy
                print(f"{self.name} attacked {target.name} with {self.newmove_1} and paralysed {target.name} for 2 turns")
                print(f"\n{hero.name}\t\t\t{target.name}\nHP: {hero.health}\t\t\tHP: {target.health}\nEP: {hero.energy}\n")
                self.paralysed_enemy_battle(target)
                return
            else:
                print(f"\nYou haven't got enough energy to use '{self.newmove_1}'")
                return
        if miss_chance>80:#chance of missing
            if self.energy>=self.newmove1_energy:
                self.energy = self.energy-self.newmove1_energy
                print(f"{self.name} attacked {target.name} with {self.newmove_1} but MISSED!")
                enemy_attack_choser = random.randint(1,4)
                if enemy_attack_choser>=2:
                    target.enemy_na_attack(self)
                    if self.health<=0:
                        game_over()
                        return 
                elif enemy_attack_choser<2:
                    target.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
                        return
                return
            else:
                print(f"\nYou haven't got enough energy to use '{self.newmove_1}'")
                return
    
    def prepare_screen(self):
        while True:
            choice_1 = input(f"Battle Preparation Screen\n\nEquip each battle slot with a move by typing the move's corresponding number.\nType 'D' to display description. And 'E' to exit the Description.\n\nBattle Slots:\n1. {self.battle_slot1} <-\n2. {self.battle_slot2}\n3. {self.battle_slot3}\n4. {self.battle_slot4}\n\nInventory:\n1.{self.inven_slot1}\n2.{self.inven_slot2}\n3.{self.inven_slot3}\n4.{self.inven_slot4}\n5.{self.inven_slot5}\n6.{self.inven_slot6}\n")
            if choice_1 == "1":
                self.battle_slot1 = self.inven_slot1
                break
            elif choice_1 == "2":
                self.battle_slot1 = self.inven_slot2
                break
            elif choice_1 == "3":
                self.battle_slot1 = self.inven_slot3
                break
            elif choice_1 == "4":
                self.battle_slot1 = self.inven_slot4
                break
            elif choice_1 =="d" or choice_1 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n")
                    if descrip_exit == "e" or descrip_exit == "E":
                        break
                    else:
                        print("Please press E to exit this screen")
            else:
                print("Please type 1-4 or 'd'")
                
        while True:  
            choice_2 = input(f"Battle Preparation Screen\n\nEquip each battle slot with a move by typing the move's corresponding number.\nType 'D' to display description. And 'E' to exit the Description.\n\nBattle Slots:\n1. {self.battle_slot1} \n2. {self.battle_slot2} <-\n3. {self.battle_slot3}\n4. {self.battle_slot4}\n\nInventory:\n1.{self.inven_slot1}\n2.{self.inven_slot2}\n3.{self.inven_slot3}\n4.{self.inven_slot4}\n5.{self.inven_slot5}\n6.{self.inven_slot6}\n")
            if choice_2 == "1":
                if self.battle_slot1 == self.inven_slot1:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot2 = self.inven_slot1
                break
            elif choice_2 == "2":
                if self.battle_slot1 == self.inven_slot2:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot2 = self.inven_slot2
                break
            elif choice_2 == "3":
                if self.battle_slot1 == self.inven_slot3:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot2 = self.inven_slot3
                break
            elif choice_2 == "4":
                if self.battle_slot1 == self.inven_slot4:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot2 = self.inven_slot4
                break
            elif choice_2 =="d" or choice_2 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n")
                    if descrip_exit == "e"or descrip_exit == "E":
                        break
                    else: 
                        print("Please press E to exit this screen")
            else:
                print("Please type 1-4 or 'd'")
        while True: 
            choice_3 = input(f"Battle Preparation Screen\n\nEquip each battle slot with a move by typing the move's corresponding number.\nType 'D' to display description. And 'E' to exit the Description.\n\nBattle Slots:\n1. {self.battle_slot1} \n2. {self.battle_slot2} \n3. {self.battle_slot3} <-\n4. {self.battle_slot4}\n\nInventory:\n1.{self.inven_slot1}\n2.{self.inven_slot2}\n3.{self.inven_slot3}\n4.{self.inven_slot4}\n5.{self.inven_slot5}\n6.{self.inven_slot6}\n")
            if choice_3 == "1":
                if self.battle_slot1== self.inven_slot1 or self.battle_slot2 == self.inven_slot1:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot3 = self.inven_slot1
                break
            elif choice_3 == "2":
                if self.battle_slot1== self.inven_slot2 or self.battle_slot2 == self.inven_slot2:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot3 = self.inven_slot2
                break
            elif choice_3 == "3":
                if self.battle_slot1== self.inven_slot3 or self.battle_slot2 == self.inven_slot3:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot3 = self.inven_slot3
                break
            elif choice_3 == "4":
                if self.battle_slot1== self.inven_slot4 or self.battle_slot2 == self.inven_slot4:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot3 = self.inven_slot4
                break
            elif choice_3 =="d" or choice_3 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n")
                    if descrip_exit == "e"or descrip_exit == "E":
                        break
                    else: 
                        print("Please press E to exit this screen")
            else:
                print("Please type 1-4 or 'd'")
        while True: 
            choice_4 = input(f"Battle Preparation Screen\n\nEquip each battle slot with a move by typing the move's corresponding number.\nType 'D' to display description. And 'E' to exit the Description.\n\nBattle Slots:\n1. {self.battle_slot1} \n2. {self.battle_slot2} \n3. {self.battle_slot3} \n4. {self.battle_slot4} <-\n\nInventory:\n1.{self.inven_slot1}\n2.{self.inven_slot2}\n3.{self.inven_slot3}\n4.{self.inven_slot4}\n5.{self.inven_slot5}\n6.{self.inven_slot6}\n")
            if choice_4 == "1":
                if self.battle_slot1== self.inven_slot1 or self.battle_slot2== self.inven_slot1 or self.battle_slot3 == self.inven_slot1:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot1
                break
            elif choice_4 == "2":
                if self.battle_slot1== self.inven_slot2 or self.battle_slot2== self.inven_slot2 or self.battleslot3 == self.inven_slot2:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot2
                break
            elif choice_4 == "3":
                if self.battle_slot1== self.inven_slot3 or self.battle_slot2== self.inven_slot3 or self.battleslot3 == self.inven_slot3:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot3
                break
            elif choice_4 == "4":
                if self.battle_slot1== self.inven_slot4 or self.battle_slot2== self.inven_slot4 or self.battleslot3 == self.inven_slot4:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot4
                break
            elif choice_4 =="d" or choice_4 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n")
                    if descrip_exit == "e"or descrip_exit == "E":
                        break
                    else: 
                        print("Please press E to exit this screen")
            else:
                print("Please type 1-4 or 'd'")
        print(f"Battle Preparation Screen\n\nEquip each battle slot with a move by typing the move's corresponding number.\nType 'D' to display description. And 'E' to exit the Description.\n\nBattle Slots:\n1. {self.battle_slot1} \n2. {self.battle_slot2} \n3. {self.battle_slot3} \n4. {self.battle_slot4} <-\n\nInventory:\n1.{self.inven_slot1}\n2.{self.inven_slot2}\n3.{self.inven_slot3}\n4.{self.inven_slot4}\n5.{self.inven_slot5}\n6.{self.inven_slot6}\n")
        ready = input("\nAre you ready for battle? y/n")
        while True:
            if ready == "y":
                break
            if ready == "n":
                pass
        return
    
hero = Hero()



def game_over(): #Needs working on.
    print("Game Over")
    while True:
        answer = input("Restart? Y/N ")
        if answer == "y" or "Y":
            return "I don't know how to make the game restart. Sorry"
        elif answer == "n" or "N":
            return "Game Ended"
        else:
            print("Please answer with 'y' or 'n'")
    

def startgame():
    hero.name = input("Please input your Hero's Name ")
    print(f"\nWelcome {hero.name},to Persona 6(Demo).\nLet's start off with a tutorial to get you used to the game mechanics\n")
    print("HP - Health Points\nEP - Energy Points\nDP - Damage points\n\n")
    print("A Hobbit has appeared infront of you!\nMission - Defeat the Hobbit\n\nPlease select what attack you want to use by typing '1','2','3' or '4'.")
    hero.battle(hobbit) #Sort out game over mechanics
    hero.restore_all()
    print(f"\nNice! Looks like you've got a hang of the controls {hero.name}!")
    input(f"\n{hero.name}: 'Huuh? What the....'")
    input("\n*Angel swoops down from the clouds and crash lands infront of you*")
    print(f"\n{hero.name}: 'Who are you??")
    input("\nRandom Angel: ...")
    print("\n*Angel charges towards you*")
    print("\n\nMission - Defeat Gabriel")
    hero.battle(Gabriel) #fix health resotration
    print(f"\n{hero.name}: 'what on earth was that all about...")
    print("\n*walks into dark forest*")
    return "Demo Complete"
















class Enemy:
    def __init__(self,name="None",class_name="none",na_dmg=5,sa_dmg=15):
        self.health = 100
        self.name = name
        self.normal_attack = None
        self.special_attack = None
        self.na_dmg = na_dmg
        self.sa_dmg = sa_dmg
        self.class_name =class_name
    def __str__(self):
        return f"This is {self.name}.A {self.class_name} type enemy.Their attacks are {self.Normal_attack} and {self.special_attack}."
    
    def enemy_na_attack(self,target):
        enemy_miss_chance = random.randint(0,100)
        if enemy_miss_chance<=90:
            print(f"{self.name} attacked {target.name} with {self.normal_attack} and dealt {self.na_dmg} damage to {target.name}")
            target.health = target.health-self.na_dmg
            if target.health <=0:
                print("You died!")
            return
        if enemy_miss_chance>90:
            print(f"{self.name} attacked {target.name} with {self.normal_attack} but MISSED!")
            target.health = target.health-0
            if target.health <=0:
                print("You died!")
            return
            
    def enemy_sp_attack(self,target):
        enemy_miss_chance = random.randint(0,100)
        if enemy_miss_chance<=80:
            print(f"{self.name} attacked {target.name} with {self.special_attack} and dealt {self.sa_dmg} damage to {target.name}")
            target.health = target.health-self.sa_dmg
            if target.health <=0:
                print("You died!")
            return
        if enemy_miss_chance>80:
            print(f"{self.name} attacked {target.name} with {self.special_attack} but MISSED!")
            target.health = target.health-0
            if target.health <=0:
                print("You died!")
            return
            
        
class Demon(Enemy):
    pass

hobbit = Demon("Hobbit","Demon")
hobbit.normal_attack = "Claw Scratch"
hobbit.special_attack = "Hell Fire Ball"


class Angel(Enemy):
    pass

Gabriel = Angel("Gabriel","Angel",7,16)
Gabriel.normal_attack = "Light Ray"
Gabriel.special_attack = "Eternal Purification"


class Human(Enemy):
    pass

thug = Human("Thug","Human")
thug.normal_attack = "knife stab"
thug.special_attack = "Shotgun shot"