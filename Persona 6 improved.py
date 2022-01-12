# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 12:11:47 2021

@author: Lione
"""

import random
import sys

class Hero:
    def __init__(self,name="Lionel",class_name="Hero",newmove_1= "Thorn Cage", newmove1_dmg = 2,newmove1_energy = 35,heal_move = "Apple of Eden", heal_energy = 15,heal = 30 ):
        self.health = 100
        self.max_health = 100
        self.energy=100
        self.max_energy = 100
        self.starting_crit = 15
        self.name = name
        self.current_xp = 0
        self.max_xp = 500
        self.starting_level = 1
        self.max_level = 50
        self.normal_attack = "Light Slash"
        self.na_energy = 7
        self.na_dmg = 14
        self.special_attack = "Soul Caliber Strike"
        self.sa_energy=25
        self.sa_dmg = 30
        self.restore_move="Heavenly Restoration"
        self.restore = 12
        self.heal_move= heal_move
        self.heal_energy = heal_energy 
        self.heal = heal
        self.newmove_1= newmove_1
        self.newmove1_dmg = newmove1_dmg
        self.newmove1_energy = newmove1_energy 
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
        self.inven_slot5 = self.heal_move
        self.inven_slot6 = "Empty"
    
    def healing(self):
        sucessful_heal_message = "{self.name} used '{self.heal_move}' and restored {self.heal}HP!"
        sucessful_maxheal_message = "{self.name} used '{self.heal_move}' and maxed out their HP"
        unsucessful_heal_message = f"\n{self.name} tried to use '{self.heal_move}' but didn't have enough energy. {self.name}'s guard is now OPEN!"
        if (self.health+self.heal)<=self.max_health:
            if self.energy>=self.heal_energy:
                self.energy-= self.heal_energy
                self.health +=self.heal 
                print(f"{sucessful_heal_message}")
                return
            else:
                print(f"{unsucessful_heal_message}")
                return
        else:
            if self.energy>=self.heal_energy:
                self.energy-= self.heal_energy
                self.health = self.max_health
                print(f"{sucessful_maxheal_message}")
                return
            else:
                print(f"{unsucessful_heal_message}")
                return
        
    
    def hero_norm_attack(self,target):
        na_no_energy_msg = f"\n{self.name} tried to use '{self.normal_attack}' but didn't have enough energy. {self.name}'s guard is now OPEN!"
        miss_chance = random.randint(0,100) #generates chance of missing
        critical_chance = random.randint(0,100) #genereates chance of hitting critical attack
        if miss_chance<=80: #below is what happens when i dont miss
            if critical_chance<=10: #checks if i land critical. 1/10 chance
                if self.energy>=self.na_energy: #checks if I have enough energy to even use the normal attack and land the critical
                    global critical_counter
                    critical_counter +=1 #increases critical hit counter for xp reward calculator at end of battle
                    self.energy = self.energy-self.na_energy
                    total_dmg = self.na_dmg+self.starting_crit
                    print(f"{self.name} attacked {target.name} with {self.normal_attack} and landed a CRITICAL HIT! Dealing a total of {total_dmg} damage!")
                    target.health = target.health-total_dmg
                    if target.health <=0: #checks if target is dead after that attack
                        return 
                else:#what happens if i dont have enough energy
                    print(f"{na_no_energy_msg}")
                    return
            else: #what happens if its not a critical hit
                if self.energy>=self.na_energy:
                    self.energy = self.energy-self.na_energy
                    print(f"{self.name} attacked {target.name} with '{self.normal_attack}' and dealt {self.na_dmg} damage")
                    target.health = target.health-self.na_dmg
                    if target.health <=0:
                        print(f"Well done! You defeated {target.name}")
                        return 
                    return
                else: # what happens if i ont have enough energy for normal attack
                    print(f"{na_no_energy_msg}")
                    return
        else:#what happens if you miss
            if self.energy>=self.na_energy:#check if you have enough energy
                self.energy = self.energy-self.na_energy
                print(f"{self.name} tried to use '{self.normal_attack}' on {target.name} but MISSED! {self.name}'s guard is now OPEN!")
                return 
            else:
                print(f"{na_no_energy_msg}")
                return
            
    def battle(self,foe,bs1,bs2,bs3,bs4):
        global critical_counter
        critical_counter = 0
        print("Press 'D' to view move descriptions\n")
        print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
        while True: 
            selection = input(f"1. {self.battle_slot1}\n2. {self.battle_slot2}\n3. {self.battle_slot3}\n4. {self.battle_slot4}\n")
            if selection =="d" or selection =="D":
                while True:
                    descrip_exit = input(f"Move Description Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n5.{self.heal_move} - Restores {self.heal} HP. Costs {self.heal_energy} EP")
                    if descrip_exit == "e" or descrip_exit == "E":
                        break
            elif selection == "1":
                self.move_selector(bs1,foe,bs1,bs2,bs3,bs4)
                if bs1 == self.newmove_1:
                    if self.health<=0:
                        game_over()
                        return 
                    if foe.health<=0:
                        print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                        print(f"Well done! you defeated {foe.name}")
                        break
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                else:
                    if foe.health<=0:
                        break
                    enemy_attack_choser = random.randint(1,4)
                    if enemy_attack_choser>=2:
                        foe.enemy_na_attack(self)#!Sort out what happens when you die. make a die function where it allows you to restart.!
                        if self.health<=0:
                            game_over()
                            return 
                    elif enemy_attack_choser<2:
                        foe.enemy_sp_attack(self)
                        if self.health<=0:
                            game_over()
                            return
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
                
            elif selection=="2":
                self.move_selector(bs2,foe,bs1,bs2,bs3,bs4)
                if bs2 == self.newmove_1:
                    if self.health<=0:
                        game_over()
                        return 
                    if foe.health<=0:
                        print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                        print("Well done! you defeated {target.name}")
                        break
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                else:
                    if foe.health<=0:
                        print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                        print(f"Well done! You defeated the {foe.name}")
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
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
                
            elif selection=="3":
                self.move_selector(bs3,foe,bs1,bs2,bs3,bs4)
                if bs3 == self.newmove_1:
                    if self.health<=0:
                        game_over()
                        return 
                    if foe.health<=0:
                        print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                        print(f"Well done! you defeated {foe.name}")
                        break
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                else:
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
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
            elif selection=="4":
                self.move_selector(bs4,foe,bs1,bs2,bs3,bs4)
                if bs4 == self.newmove_1:
                    if self.health<=0:
                        game_over()
                        return 
                    if foe.health<=0:
                        print(f"\n{self.name}\t\t\t{foe.name}\nHP: {self.health}\t\t\tHP: 0\nEP: {self.energy}\n")
                        print(f"Well done! You defeated the {foe.name}")
                        break
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                else:
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
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
        return
    
    def move_selector(self, battleslot,foe,bs1,bs2,bs3,bs4):
        if battleslot == self.normal_attack:
            self.hero_norm_attack(foe)
            return
        elif battleslot == self.special_attack:
            self.hero_sp_attack(foe)
            return
        elif battleslot == self.restore_move:
            self.energy_restore()
            return
        elif battleslot == self.newmove_1:
            self.para_attack(foe,bs1,bs2,bs3,bs4)
            return
        elif battleslot == self.heal_move:
            self.healing()
            return
        
        
    def paralysed_enemy_battle(self,foe,bs1,bs2,bs3,bs4):
        global critical_counter
        remaining_turns = 2
        while True: 
            selection = input(f"1. {self.battle_slot1}\n2. {self.battle_slot2}\n3. {self.battle_slot3}\n4. {self.battle_slot4}\n")
            if selection == "1":
                self.move_selector(bs1,foe,bs1,bs2,bs3,bs4)
                if bs1 == self.newmove_1:
                    return
                else:
                    foe.health = foe.health-self.newmove1_dmg
                    print(f"{foe.name} misses turn due to paralysis")
                    remaining_turns-=1
                    if remaining_turns==0:
                        return
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
                
            elif selection=="2":
                self.move_selector(bs2,foe,bs1,bs2,bs3,bs4)
                if bs2 == self.newmove_1:
                    return
                else:
                    foe.health = foe.health-self.newmove1_dmg
                    print(f"{foe.name} misses turn due to paralysis")
                    remaining_turns-=1
                    if remaining_turns==0:
                        return
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
            elif selection=="3":
                self.move_selector(bs3,foe,bs1,bs2,bs3,bs4)
                if bs3 == self.newmove_1:
                    return
                else:
                    foe.health = foe.health-self.newmove1_dmg
                    print(f"{foe.name} misses turn due to paralysis")
                    remaining_turns-=1
                    if remaining_turns==0:
                        return
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
                
            elif selection=="4":
                self.move_selector(bs4,foe,bs1,bs2,bs3,bs4)
                if bs4 == self.newmove_1:
                    return
                else:
                    foe.health = foe.health-self.newmove1_dmg
                    print(f"{foe.name} misses turn due to paralysis")
                    remaining_turns-=1
                    if remaining_turns==0:
                        return
                    print(f"\n{self.name} Lvl {self.starting_level}\t\t{foe.name} Lvl {foe.level}\nHP: {self.health}\t\t\t\tHP: {foe.health}\nEP: {self.energy}\n")
            else:
                print("Please select 1,2,3 or 4")
    
    def hero_sp_attack(self,target):
        miss_chance = random.randint(0,100)
        critical_chance = random.randint(0,100)
        if miss_chance<=75: #check i dont miss
            if critical_chance<=10: #check if i can hit critical
                if self.energy>=self.sa_energy:# what happens when i have enough energy and have a critical hit chance
                    global critical_counter
                    critical_counter +=1 
                    self.energy = self.energy-self.sa_energy
                    total_dmg = self.sa_dmg+self.starting_crit
                    print(f"{self.name} attacked {target.name} with {self.special_attack} and landed a CRITICAL HIT! Dealing a total of {total_dmg} damage!")
                    target.health = target.health-total_dmg
                    if target.health <=0: #checks if enemy is still breathing after that disgusting critical attack
                        print(f"Well done! You defeated {target.name}!")
                        return 
                    return
                else: #what happens when I dont have enough energy.
                    print(f"\n{self.name} tried to use '{self.special_attack}' but didn't have enough energy. {self.name}'s guard is now OPEN!")
                    return
            else: #what happens when dont have a crtiical
                if self.energy>=self.sa_energy: #check if you have energy
                    self.energy = self.energy-self.sa_energy
                    print(f"{self.name} attacked {target.name} with {self.special_attack} and dealt {self.sa_dmg} damage")
                    target.health = target.health-self.sa_dmg
                    if target.health <=0:
                        print(f"Well done! You defeated {target.name}!")
                        return 
                    return
                else:#not enough energy
                    print(f"\n{self.name} tried to use '{self.special_attack}' but didn't have enough energy. {self.name}'s guard is now OPEN!")
                    return
        else:#what happens when you miss
            if self.energy>=self.sa_energy:
                self.energy = self.energy-self.sa_energy
                print(f"{self.name} attacked {target.name} with {self.special_attack} but MISSED!")
                return 
            else:
                print(f"\n{self.name} tried to use '{self.special_attack}' but didn't have enough energy. {self.name}'s guard is now OPEN!")
                return
            
    def energy_restore(self):
        if self.energy+self.restore<=self.max_energy:
            self.energy=self.energy+self.restore
            print(f"{self.name} restored {self.restore} EP with '{self.restore_move}'")
            return
        else:
            self.energy = self.max_energy
            print(f"{self.name} used '{self.restore_move}' and maxed out their HP")
            return
        
    def restore_all(self):# A function that restores all HP and EP. used after battles.
        if self.health!=self.max_health:
            self.health=self.max_health
        if self.energy!=self.max_energy:
            self.energy=self.max_energy
        return
            
    def para_attack(self,target,bs1,bs2,bs3,bs4): 
        miss_chance = random.randint(0,100)
        if miss_chance<=80: #what happens when you dont miss
            if self.energy>=self.newmove1_energy:
                self.energy = self.energy-self.newmove1_energy
                print(f"{self.name} attacked {target.name} with {self.newmove_1} and paralysed {target.name} for 2 turns")
                print(f"\n{hero.name}\t\t\t{target.name}\nHP: {hero.health}\t\t\tHP: {target.health}\nEP: {hero.energy}\n")
                self.paralysed_enemy_battle(target,bs1,bs2,bs3,bs4)
                return
            else: #what happens when you don't miss but haven't got enough energy!
                print(f"\n{self.name} tried to use '{self.newmove_1}' but didn't have enough energy. {self.name}'s guard is now OPEN!")
                enemy_attack_choser = random.randint(1,4) #this randomly generates what move the enemy uses
                if enemy_attack_choser>=2: 
                    target.enemy_na_attack(self)
                    if self.health<=0:
                        game_over()
                    return 
                else:
                    target.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
                    return
        else:#what happens when you miss
            if self.energy>=self.newmove1_energy: #Checks if you have enough energy
                self.energy = self.energy-self.newmove1_energy
                print(f"{self.name} tried to use {self.newmove_1} on {target.name} but MISSED! {self.name}'s guard is now OPEN!")
                enemy_attack_choser = random.randint(1,4)#this randomly generates what move the enemy uses
                if enemy_attack_choser>=2:
                    target.enemy_na_attack(self)
                    if self.health<=0:
                        game_over()
                    return 
                else:
                    target.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
                    return
            else: #What happens when you dont have enough energy
                print(f"\n{self.name} tried to use '{self.newmove_1}' but didn't have enough energy.{self.name}'s guard is now open!")
                enemy_attack_choser = random.randint(1,4)#this randomly generates what move the enemy uses
                if enemy_attack_choser>=2:
                    target.enemy_na_attack(self)
                    if self.health<=0:
                        game_over()
                    return 
                else:
                    target.enemy_sp_attack(self)
                    if self.health<=0:
                        game_over()
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
            elif choice_1 == "5":
                self.battle_slot1 = self.inven_slot5
                break
            elif choice_1 =="d" or choice_1 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n5.{self.heal_move} - Restores {self.heal} HP. Costs {self.heal_energy} EP")
                    if descrip_exit == "e"or descrip_exit == "E":    
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
            elif choice_2 == "5":
                if self.battle_slot1 == self.inven_slot5:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot2 = self.inven_slot5
                break
            elif choice_2 =="d" or choice_2 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n5.{self.heal_move} - Restores {self.heal} HP. Costs {self.heal_energy} EP")
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
            elif choice_3 == "5":
                if self.battle_slot1== self.inven_slot5 or self.battle_slot2 == self.inven_slot5:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot3 = self.inven_slot5
                break
            elif choice_3 =="d" or choice_3 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n5.{self.heal_move} - Restores {self.heal} HP. Costs {self.heal_energy} EP")
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
                if self.battle_slot1== self.inven_slot2 or self.battle_slot2== self.inven_slot2 or self.battle_slot3 == self.inven_slot2:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot2
                break
            elif choice_4 == "3":
                if self.battle_slot1== self.inven_slot3 or self.battle_slot2== self.inven_slot3 or self.battle_slot3 == self.inven_slot3:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot3
                break
            elif choice_4 == "4":
                if self.battle_slot1== self.inven_slot4 or self.battle_slot2== self.inven_slot4 or self.battle_slot3 == self.inven_slot4:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot4
                break
            elif choice_4 == "5":
                if self.battle_slot1== self.inven_slot5 or self.battle_slot2== self.inven_slot5 or self.battle_slot3 == self.inven_slot5:
                    print("This move has already been chosen. Please choose another move")
                    continue
                self.battle_slot4 = self.inven_slot5
                break
            elif choice_4 =="d" or choice_4 =="D":
                while True:
                    descrip_exit = input(f"Battle Preparation Screen\n\nSee details of your moves below.\nType 'E' to exit the Description Screen.\n\nMoves:\n1.{self.normal_attack} - Deals {self.na_dmg} DP. Costs {self.na_energy} EP\n2.{self.special_attack} - Deals {self.sa_dmg} DP. Costs {self.sa_energy} EP\n3.{self.restore_move} - Restores {self.restore} EP\n4.{self.newmove_1} - Paralyses enemy for 2 turns and deals {self.newmove1_dmg} DP per turn. Costs {self.newmove1_energy} EP\n5.{self.heal_move} - Restores {self.heal} HP. Costs {self.heal_energy} EP")
                    if descrip_exit == "e"or descrip_exit == "E":
                        break
                    else: 
                        print("Please press E to exit this screen")
            else:
                print("Please type 1-4 or 'd'")
        print(f"Battle Preparation Screen\n\nEquip each battle slot with a move by typing the move's corresponding number.\nType 'D' to display description. And 'E' to exit the Description.\n\nBattle Slots:\n1. {self.battle_slot1} \n2. {self.battle_slot2} \n3. {self.battle_slot3} \n4. {self.battle_slot4} <-\n\nInventory:\n1.{self.inven_slot1}\n2.{self.inven_slot2}\n3.{self.inven_slot3}\n4.{self.inven_slot4}\n5.{self.inven_slot5}\n6.{self.inven_slot6}\n")
        ready = input("\nAre you ready for battle? y/n\n")
        while True:
            if ready == "y":
                break
            if ready == "n": #!find a way to reset the battle slots so they can choose again!
                pass
        return
    
    def beginner_hero(self):
        self.normal_attack = "Pocket Knife Slash"
        self.na_energy = 2
        self.na_dmg = 6
        self.special_attack = "Double Knife Throw"
        self.sa_energy=4
        self.sa_dmg = 12
        self.restore_move="Drink Water"
        self.restore = 15
        self.energy= 70
        self.current_xp = 0
        self.max_xp = 500
        self.heal_move='Aloe Vera Bandage'
        self.heal_energy = 10
        self.heal = 20
        self.starting_level = 1
        self.battle_slot1 = "Empty"
        self.battle_slot2 = "Empty"
        self.battle_slot3 = "Empty"
        self.battle_slot4 = "Empty"
        self.inven_slot1 = self.normal_attack
        self.inven_slot2 = self.special_attack
        self.inven_slot3 = self.restore_move
        self.inven_slot4 = self.heal_move
        self.inven_slot5 = "Empty"
        self.inven_slot6 = "Empty"
        return
    

    def gamerestart(self):
        self.health = 100
        self.max_health = 100
        self.energy=100
        self.max_energy = 100
        self.starting_crit = 15
        self.current_xp = 0
        self.max_xp = 500
        self.max_level = 50
        self.normal_attack = "Light Slash"
        self.na_energy = 7
        self.na_dmg = 14
        self.special_attack = "Soul Caliber Strike"
        self.sa_energy=25
        self.sa_dmg = 30
        self.restore_move="Heavenly Restoration"
        self.restore = 12
        self.heal_move= "Apple of Eden"
        self.heal_energy = 15
        self.heal = 30
        self.battle_slot1 = "Empty"
        self.battle_slot2 = "Empty"
        self.battle_slot3 = "Empty"
        self.battle_slot4 = "Empty"
        self.inven_slot1 = self.normal_attack
        self.inven_slot2 = self.special_attack
        self.inven_slot3 = self.restore_move
        self.inven_slot4 = self.newmove_1
        self.inven_slot5 = self.heal_move
        self.inven_slot6 = "Empty"
        hobbit.health = 100
        Angel.health = 100
        thug.health = 100
        return
    
    def battle_complete_screen(self): #Not working properly. Notleveling up past level 2.
        thug.enemyreset()
        global critical_counter
        max_xp_increase = 500
        hp_multiplier = 5
        crit_multiplier = 20
        base_xp_reward = 200 
        hp_xp  = hp_multiplier*self.health
        critical_xp = crit_multiplier*critical_counter
        total_reward_xp = base_xp_reward+hp_xp+critical_xp
        input(f"Battle Complete - VICTORY!\n\nVictory:\t\t\t\t+{base_xp_reward} XP\nRemaining HP = {self.health}/{self.max_health}:\t+{hp_xp} XP\nCritical Attacks = {critical_counter}:\t+{critical_xp} XP\n\nTotal:\t\t\t\t\t+{total_reward_xp} XP\n\n*Press Enter to continue*")
        critical_counter = 0
        self.current_xp +=total_reward_xp
        if total_reward_xp>=self.max_xp:
            remainder_xp = total_reward_xp-self.max_xp
            self.current_xp=0
            self.max_xp+=max_xp_increase
            self.current_xp+=remainder_xp
            xp_4_levelup = self.max_xp-remainder_xp
            input(f"Level {self.starting_level}--->Level {self.starting_level+1}\n\nLEVEL UP!\n\nRemaining XP until next level - {xp_4_levelup}")
            self.starting_level+=1
            self.max_xp+=max_xp_increase
            return
        else:
            self.current_xp+=total_reward_xp
            xp_4_levelup = self.max_xp-total_reward_xp
            input(f"Current Level - {self.starting_level}\n\nNext Level - {self.starting_level+1}\n\nRemaining XP until next level - {xp_4_levelup}")
            return
            
            
            

hero = Hero()
hero.starting_level = 10


def game_over(): #Needs working on.
    while True:
        answer = input("Restart? Y/N ")
        if answer == "y":
            startgame()
            return
        elif answer == "n":
            sys.exit("Game Over")
        else:
            print("Please answer with 'y' or 'n'")
    




def startgame():
    if hero.health<0:
        hero.gamerestart()#not srure about this
        startgame()
        return
    hero.name = input("Please input your Hero's Name ")
    print(f"\nWelcome {hero.name},to Persona 6(Demo).\nLet's start off with a tutorial to get you used to the game mechanics\n")
    input("\n*Press Enter to continue*")
    print("\nBelow are some abbreviations that will come up often in battle.\n")
    input("HP - Health Points\nEP - Energy Points\nDP - Damage points\n\n\n")
    print("*Below is the 'Battle Preparation Screen'. Here you can select what moves you want to equip when going into battle. Give it a try!*\n\n")
    hero.prepare_screen()
    print("\n\nA Hobbit has appeared infront of you!\nMission - Defeat the Hobbit\n\nPlease select what attack you want to use by typing '1','2','3' or '4'.")
    hero.battle(hobbit,hero.battle_slot1,hero.battle_slot2,hero.battle_slot3,hero.battle_slot4)
    hero.battle_complete_screen()#Sort out game over mechanics
    hero.restore_all()
    print(f"\nNice! Looks like you've got a hang of the controls {hero.name}!")
    hero.beginner_hero()
    print("\n\n\n\t\t\t\t\t\t\t\tCHAPTER 1 - 'Predestined Fate'\n\n") #Need someone to write a good story to set the scene
    input(f"\n{hero.name}: 'Huuh? What the....'")
    input("\n*A weird creature swoops down from the clouds and crash lands infront of you*")
    print(f"\n{hero.name}: 'Who are you??")
    input("\nRandom Angel: ...")
    input("\n*Angel charges towards you*")
    hero.prepare_screen()
    print("\n\nMission - Defeat Angel looking creature")
    hero.battle(Angel,hero.battle_slot1,hero.battle_slot2,hero.battle_slot3,hero.battle_slot4) 
    hero.battle_complete_screen()
    print(f"\n\n\n{hero.name}: *panting*")
    input(f"\n{hero.name}: *Slowly walks up to Angels body*")
    input("\nThe Angel's body was covered in blue blood and knife wounds")
    input("\nAngel: *coughs blood while lying on the cold hard ground*")
    input(f"\n{hero.name}: 'You're still alive???'")
    input(f"\n{hero.name}: *sigh*")
    input(f"\n{hero.name}: *Pulls out knife from pouch and sprints towards half dead angel*")
    print(f"\n{hero.name}: 'AAAHHHHHHH!!!!!'")
    print(f"\n{hero.name}: 'TAKE THIS!'")
    print(f"\n{hero.name}: *JUMPS INTO THE AIR AND RAISES KNIFE ABOVE HEAD*")
    input(f"\n{hero.name}: *swings blade down towards Angels chest*")
    print(f"\n{hero.name}: *thrusts knife into chest*")
    input("*SPLAT*")
    print(f"\n{hero.name}: *twists and turns blade inside Angel's chest*")
    input(f"\n{hero.name}: 'ARGHHHHHH'")
    input(f"\n{hero.name}: *thrusts knife multiple times into Angels chest in anger*")
    input(f"\n{hero.name}: *THRUST*")
    input(f"\n{hero.name}: *THRUST*")
    input(f"\n{hero.name}: *THRUST*")
    input(f"\n{hero.name}: *THRUST*")
    input(f"\n{hero.name}: *THRUST*")
    input(f"\n{hero.name}: ....")
    input(f"\n{hero.name}: .....")
    input(f"\n{hero.name}: ........?")
    input(f"\n{hero.name}: *looks down at stomach")
    input(f"\n{hero.name}: *sees gaping hole in stomach*")
    input(f"\n{hero.name}: When did he..?")
    input(f"\n{hero.name}: *passes out*")
    input("............")
    input("........................")
    print("\n\n\n\t\t\t\t\t\t\t\tCHAPTER 2 - 'The Awakening'\n\n")
    input(f"\n{hero.name}: .....")
    hero.prepare_screen()
    print("\n\nMission - Survive against the wave of Thugs")
    hero.battle(thug,hero.battle_slot1,hero.battle_slot2,hero.battle_slot3,hero.battle_slot4) 
    hero.battle_complete_screen()
    hero.prepare_screen()
    hero.battle(thug,hero.battle_slot1,hero.battle_slot2,hero.battle_slot3,hero.battle_slot4) 
    hero.battle_complete_screen()
    hero.prepare_screen()
    hero.battle(thug,hero.battle_slot1,hero.battle_slot2,hero.battle_slot3,hero.battle_slot4) 
    hero.battle_complete_screen()
    hero.prepare_screen()
    hero.battle(thug,hero.battle_slot1,hero.battle_slot2,hero.battle_slot3,hero.battle_slot4) 
    hero.battle_complete_screen()
    return "Demo Complete - To be continued"









class Enemy:
    def __init__(self,name,class_name,level, normal_attack,na_dmg,special_attack,sa_dmg):
        self.health = 100
        self.level = level
        self.name = name
        self.normal_attack = normal_attack
        self.special_attack = special_attack
        self.na_dmg = na_dmg
        self.sa_dmg = sa_dmg
        self.class_name =class_name
    
    def __str__(self):
        return f"This is {self.name}.A {self.class_name} type enemy.Their attacks are {self.Normal_attack} and {self.special_attack}."
    
    def enemyreset(self):
        thug.health = 100 
        Angel.health = 100 
        hobbit.health = 100
        return
    
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

hobbit = Demon("Hobbit","Demon",1,"Claw Scratch",5,"Hell Fire Ball",15)


class Angel(Enemy):
    pass

Angel = Angel("Angel","Angel",3,"Light Ray",7,"Eternal Purification",14)


class Human(Enemy):
    pass

thug = Human("Thug","Human",1,"Rusty blade Stab",5,"Molotov throw",8)

startgame()


