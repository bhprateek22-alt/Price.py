# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:12:37 2021

@author: PRATIK BHARDWAJ
"""
#importing libraries
import matplotlib.pyplot as x
import random
import os
#TITLE SCREEN
title='''
                                                                                  ____         _               _____
                                                                                 |  _ \  _ __ (_)  ___   ___  |_   _|  __ _   __ _
                                                                                 | |_) || '__|| | / __| / _ \   | |   / _` | / _` |
                                                                                 |  __/ | |   | || (__ |  __/   | |  | (_| || (_| |
                                                                                 |_|    |_|   |_| \___| \___|   |_|   \__,_| \__, |
                                                                                                                             |___/

                                                                                                 ___    __    __  __  ____
                                                                                                / __)  /__\  (  \/  )( ___)
                                                                                               ( (_-. /(__)\  )    (  )__)
                                                                                                \___/(__)(__)(_/\/\_)(____)

 '''
space="                                                "
print("*  "*211)
for i in range(14):
    print(" ")
print(title)
for i in range(14):
    print(" ")
print("*  "*211)
input()
os.system("cls")
#STARTING DIALOGUES
print("_"*200)
print("REVEAL THE PRICE TAG ..\n_Lets Begin the Game!!_")
print("Give a Right answer & You Won A Discount Coupon!")
print("GAME of Brains !")
print("_"*200)
#Instructions
print("Follow the Instructions:\n")
print("1.Do not use Google")
print("2.For 3 successive Correct answer :1+bonus coupon")
print("3.For every wrong answer :-1 coupon")
print("4.Includes Sikkim And Delhi exclusive dishes only")
print("\t*Press 1 to continue")
print("\t*Press 2 to show hint( for that question )")
print("\t*Prss 3 to display coupons in possession")
print("\t*Press 0 to exit\n ")
print("-"*200)
for i in range(1,10):
    print("\t"*8,"      ","I"*10,"          ","I"*10)
spaces=1
for i in range(15,0,-5):
    print("\t"*8,"   "*spaces,"I"*i,"     "*spaces,"I"*i)
    spaces+=1

#Data
recipe={"Vegetable Thukpa":range(60,81),"Dal Bhatt Special Thali":range(150,181)
,"Choole Bhature":range(70,111),"Sausage":range(90,111),
"Sael Roti(1 piece)":range(8,16),"Phagshapa":range(180,201),"Vegetable Momos":range(15,41)
,"Kwati":range(90,111),"Sekuwa":range(140,161),"Pani puri":range(10,26),
"Chhurpi Cheeze soup/100 gm":range(130,141),"Wachipa":range(190,211),"Phambi":range(25,36),"Dosa":range(100,150)}
sikkim=['Vegetable Thukpa', 'Dal Bhatt Special Thali', 'Sausage', 'Sael Roti(1 piece)', 'Phagshapa', 'Vegetable Momos', 'Kwati', 'Sekuwa', 'Pani puri', 'Chhurpi Cheeze soup/100 gm', 'Wachipa', 'Phambi']
delhi=["Choole Bhature","Pani Puri","Dosa"]
#HInts
hint=["Tibetan Noodles & Meat Soup","Includes all tastes of sikkim ,BHATT=RICE "
      ,"NO hint available","Beef,Pork and stuffed Breadcrumbs"
      ,"Ring shaped rice bread ","Pork with chillies","No hint available"
      ,"Beans soup",'Barbecued Meat',"No hint available ","No hint available"
      ,"Minced Chicken including rice and burned feathers of hen"
      ,"Square shaped Mung Beans including red chillies"
      ,"NO HINT"]
hintbox=dict(zip(recipe.keys(),hint))
#Variables
bonus=0
item=True
coupons=0
no=0
dpoints=0
spoints=0
bpoints=0
items=list(recipe.keys())

#Main Program
def points():
    global bonus
    global coupons
    global bpoints
    bonus+=1
    if bonus==3:
        bpoints+=1
        bonus=0
        print("Impressive!")
        print("You won A bonus coupon also ")
        coupons+=1
def win():
    global bonus
    global spoints
    global dpoints
    if ans in recipe.get(item):
         print("Congrats!You Won a Discount Coupon!!")
         global coupons
         coupons+=1
         print(coupons)
         points()
         if item in delhi:
             dpoints+=1
         else:
             spoints+=1
    else:
         bonus=0
         print("Wrong Answer..")
         if  coupons>0:
             print("You lost one coupon")
             coupons-=1
    print('The Price is B/W:',min(recipe[item]),"&",max(recipe[item]))

try:
    while len(items)!=0:
        player=int(input("Enter your Command"))
        if player==1:
            no+=1
            item=random.choice(items)
            print(f"Quest{no}.Predict The Price Tag Of:",item)
            items.remove(item)
            ans=int(input("Your Answer:₹"))
            if ans==2:
                print("HINT:")
                print("💡"+hintbox.get(item))
                ans=int(input("Your answer"))
                win()
            else:
                win()
        elif player==3:
            print("The Coupons in Possession:",coupons)
        elif player==0:
            exit=str(input("DO You Want to Exit(yes/no)"))
            if exit in ("YES","yes","Yes"):
                break
        else:
            print("Wrong Command")
        input()
        os.system("cls")
        print("Commands::")
        print("*Press 1 to continue")
        print("*Press 2 to show hint( for that question )")
        print("*Prss 3 to display coupons in possession")
        print("*Press 0 to exit\n ")
        print("-"*200)
        for i in range(1,10):
            print("\t"*8,"      ","I"*10,"          ","I"*10)
        spaces=1
        for i in range(15,0,-5):
            print("\t"*8,"   "*spaces,"I"*i,"     "*spaces,"I"*i)
            spaces+=1
    dpoints=dpoints/len(delhi)
    spoints=spoints/len(sikkim)
    if dpoints!=0 or spoints!=0:
        axis2=[dpoints,spoints,bpoints]
        axis1=["Delhi","Sikkim","Bonus"]
        x.title("Result Anaylsis")
        x.xlabel("FOOD(State)")
        x.ylabel("Right Answers")
        a=x.pie(axis2,labels=axis1,autopct='%1.1f%%',colors=["c","m","g","b","r"],shadow=1)
        x.show()

    if coupons>=8:
         print("You are a PRO PLAYER !")
    elif coupons>=4 and coupons<8:
         print("You are better than 50% people")
    else:
            print("Better luck next time")
    print("Your Total Score:",coupons,"won")
    print('Thanks for participation')
    a=input("press enter")
except:
    print("User has entered wrong command\nRun the program again")
