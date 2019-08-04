# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:35:00 2019

@author: Conotox
"""

# The game prerequisites
import random
import time

#This is a battleship with two coordinates.
class battleShip():
    def __ini__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

#Gather coordinates for the computer ship.
ship = battleShip()
ship.coord1 = random.randint(1, 5)
ship.coord2 = random.randint(1, 5)
ship2 = battleShip()
ship2.coord1 = random.randint(1, 5)
ship2.coord2 = random.randint(1, 5)
ship3 = battleShip()
ship3.coord1 = random.randint(1, 5)
ship3.coord2 = random.randint(1, 5)


#Create the player ship.
player = battleShip()
player2 = battleShip()
player3 = battleShip()

#All the lists / maps are here:
xlist = []
ylist = [] 
zlist = []

x1list = []
y1list = [] 

yourxlist = []
yourylist = []
yourzlist = []

playerMap = ([0,1,2,3,4,5],[1,0,0,0,0,0],[2,0,0,0,0,0],[3,0,0,0,0,0],[4,0,0,0,0,0],[5,0,0,0,0,0])
computerMap = ([0,1,2,3,4,5],[1,0,0,0,0,0],[2,0,0,0,0,0],[3,0,0,0,0,0],[4,0,0,0,0,0],[5,0,0,0,0,0])
playMap = ([0,1,2,3,4,5],[1,0,0,0,0,0],[2,0,0,0,0,0],[3,0,0,0,0,0],[4,0,0,0,0,0],[5,0,0,0,0,0])

#Gather coordinates for the Player ship and start the game.
def initiateGame():
    initiateComputerMap(ship.coord1,ship.coord2)
    initiateComputerMap(ship2.coord1,ship2.coord2)
    initiateComputerMap(ship3.coord1,ship3.coord2)
    print("===BATTLESHIPS LITE===")
    print("This is a 5x5 Grid game. You have three 1x1 ships.")
    drawPlayerMap()
    print("Here is the map. Your ships will be drawn on this map as 8's")
    print("Enemy shots will be displayed as 7's.")
    print("First, type in the coordinates for your three ships.")
    initiateGame2()

def initiateGame2():
#Asking the player to type in the coordinates for their ship.
    playerxA = input("Enter your first ship co-ordinate 1: ")
    if playerxA.isdigit():
      player.coord1 = int(playerxA)
    else:
      print("Type in numbers only.")
      initiateGame2()
    playeryA = input("Enter your first ship co-ordinate 2: ")
    if playeryA.isdigit():
      player.coord2 = int(playeryA)
    else:
      print("Type in numbers only.")
      initiateGame2()
#If the player types in coords which are outside the 5x5 grid, we ask them to try again.
    if player.coord1 > 5 or player.coord1 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame2()
    if player.coord2 > 5 or player.coord2 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame2()
    x1list.append(player.coord1)
    y1list.append(player.coord2)
    initiatePlayerMap(player.coord1,player.coord2)  
    drawPlayerMap()
    initiateGame3()

def initiateGame3():
#Asking the player to type in the coordinates for their ship.
    playerxAA = input("Enter your second ship co-ordinate 1: ")
    if playerxAA.isdigit():
      player2.coord1 = int(playerxAA)
    else:
      print("Type in numbers only.")
      initiateGame3()
    playeryAA = input("Enter your second ship co-ordinate 2: ")
    if playeryAA.isdigit():
      player2.coord2 = int(playeryAA)
    else:
      print("Type in numbers only.")
      initiateGame3()
#If the player types in coords which are outside the 5x5 grid, we ask them to try again.
    if player2.coord1 > 5 or player2.coord1 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame3()
    if player2.coord2 > 5 or player2.coord2 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame3()
    checkplayerNumbers1(player2.coord1,player2.coord2)  
    x1list.append(player2.coord1)
    y1list.append(player2.coord2)
    initiatePlayerMap(player2.coord1,player2.coord2)  
    drawPlayerMap()
    initiateGame4()

def initiateGame4():
#Asking the player to type in the coordinates for their ship.
    playerxAAA = input("Enter your third and final ship co-ordinate 1: ")
    if playerxAAA.isdigit():
      player3.coord1 = int(playerxAAA)
    else:
      print("Type in numbers only.")
      initiateGame4()
    playeryAAA = input("Enter your third and final ship co-ordinate 2: ") 
    if playeryAAA.isdigit():
      player3.coord2 = int(playeryAAA)
    else:
      print("Type in numbers only.")
      initiateGame4() 
#If the player types in coords which are outside the 5x5 grid, we ask them to try again.
    if player3.coord1 > 5 or player3.coord1 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame4()
    if player3.coord2 > 5 or player3.coord2 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame4()
    checkplayerNumbers2(player3.coord1,player3.coord2)    
    x1list.append(player3.coord1)
    y1list.append(player3.coord2)    
    initiatePlayerMap(player3.coord1,player3.coord2)  
    drawPlayerMap()
    playGame()

#You guess where the computer ship is.
def playGame():
    time.sleep(1)
    print("Try and sink the enemy battleships!")
    print("'9' is where shot has been fired.")
    print("So far you have used these coordinates:")
    drawPlayMap()
    yourzlist = list(zip(yourxlist,yourylist))
    xxA = input("Guess coordinate 1:" )
    if xxA.isdigit():
      xx = int(xxA)
    else:
      print("Type in numbers only.")
      playGame()
    yyA = input("Guess  coordinate 2:" )
    if yyA.isdigit():
      yy = int(yyA)
    else:
      print("Type in numbers only.")
      playGame()
    if yy > 5 or yy < 1:
      print("It's a 5x5 Grid. Try again.")
      playGame()
    if xx > 5 or xx < 1:
      print("It's a 5x5 Grid. Try again.")
      playGame()
    yourylist.append(yy)
    yourxlist.append(xx)
    playComputerMap(xx,yy)
    initiatePlayMap(xx,yy)
    verifyComputerMap()

#the computer will come up with two numbers to throw in for coordinates.
def enemyThinks():
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    time.sleep(1)
#We'll check to see if the computer has already used those numbers.
    checkNumbers(x,y)
    
#Lets check to see if the computer has already tried those coords before.
def checkNumbers(x,y):
    countx = 0
    county = 0
    for i in xlist[countx:]:
            countx = countx+1
            if i == x:
                for i in ylist[county:]:
                    county = county+1
                    if county == countx:
                        if i == y:
                            print("Already used", x,y, "...trying again.")
                            enemyThinks()
                            return
                        if i != y:
                            break
    print("Computer hasn't tried:",x,y,".")
    print("Computer fires cannons!")
    enemyTries(x,y)
    return()

def checkplayerNumbers1(x,y):
    countx = 0
    county = 0
    for i in x1list[countx:]:
            countx = countx+1
            if i == x:
                for i in y1list[county:]:
                    county = county+1
                    if county == countx:
                        if i == y:
                            print("You've already put a ship here!")
                            initiateGame3()
                            return
                        if i != y:
                            break
    return()

def checkplayerNumbers2(x,y):
    countx = 0
    county = 0
    for i in x1list[countx:]:
            countx = countx+1
            if i == x:
                for i in y1list[county:]:
                    county = county+1
                    if county == countx:
                        if i == y:
                            print("You've already put a ship here!")
                            initiateGame4()
                            return
                        if i != y:
                            break
    return()

#The computer will now attempt to blow up your ship.
def enemyTries(x,y):
    playPlayerMap(x,y)
    verifyPlayerMap()
#If it misses, it's your turn again.

def initiatePlayerMap(x,y):
    xindex = 0
    yindex = 0
    for i in playerMap[yindex:]:
        yindex = yindex+1
        if yindex == y+1:
            for a in i[xindex:]:
                xindex = xindex+1
                if xindex == x:
                    i[xindex] = 8

def initiatePlayMap(x,y):
    xindex = 0
    yindex = 0
    for i in playMap[yindex:]:
        yindex = yindex+1
        if yindex == y+1:
            for a in i[xindex:]:
                xindex = xindex+1
                if xindex == x:
                    i[xindex] = 9
                               
def initiateComputerMap(x,y):
    xindex = 0
    yindex = 0
    for i in computerMap[yindex:]:
        yindex = yindex+1
        if yindex == y+1:
            for a in i[xindex:]:
                xindex = xindex+1
                if xindex == x:
                    i[xindex] = 6

def playPlayerMap(x,y):
    xindex = 0
    yindex = 0
    for i in playerMap[yindex:]:
        yindex = yindex+1
        if yindex == y+1:
            for a in i[xindex:]:
                xindex = xindex+1
                if xindex == x:
                    if i[xindex] == 8:
                      print("Once of your ships was destroyed!!")
                      time.sleep(2)
                      i[xindex] = 9
                    i[xindex] = 7             
    drawPlayerMap()

def playComputerMap(x,y):
    xindex = 0
    yindex = 0
    for i in computerMap[yindex:]:
        yindex = yindex+1
        if yindex == y+1:
            for a in i[xindex:]:
                xindex = xindex+1
                if xindex == x:
                    if i[xindex] == 6:
                      print("You sunk an enemy ship!")
                      time.sleep(2)
                      i[xindex] = 5
                    i[xindex] = 7            

def verifyPlayerMap():
    yindex = 0
    for i in playerMap[yindex:]:
        yindex = yindex+1
        for a in i:
            if a == 8:
                playGame()
    print("The computer has sunk all your ships. Better luck next time!")
    time.sleep(2)
    exit()   

def verifyComputerMap():
    yindex = 0
    for i in computerMap[yindex:]:
        yindex = yindex+1
        for a in i:
            if a == 6:
                print("There are still more enemy ships. Keep firing!")
                enemyThinks()
    print("You blew up all the computer ships. Good game.")           
    time.sleep(2)
    exit()

def drawPlayerMap():
    print("--- PLAYER MAP ---")
    for i in playerMap:
        print(i)
    print("--- PLAYER MAP ---")

def drawComputerMap():
    print("-- COMPUTER MAP --")
    for i in computerMap:
        print(i)
    print("-- COMPUTER MAP --")

def drawPlayMap():
    print("-- SHOTS TAKEN --")
    for i in playMap:
        print(i)
    print("-- SHOTS TAKEN --")

initiateGame()
