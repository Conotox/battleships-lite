# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:35:00 2019

@author: Tom.Balcombe
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

#Create the player ship.
player = battleShip()

#Gather coordinates for the Player ship and start the game.
def initiateGame():
    initiateComputerMap(ship.coord1,ship.coord2)
    print("This is a 5x5 Grid game. The ships are 1x1 and 2x2.")
    print("First, type in the coordinates for your ship.")
#Asking the player to type in the coordinates for their ship.
    playerxA = input("Enter your ship co-ordinate 1: ")
    player.coord1 = int(playerxA)
    playeryA = input("Enter your ship co-ordinate 1: ")
    player.coord2 = int(playeryA)
#If the player types in coords which are outside the 5x5 grid, we ask them to try again.
    if player.coord1 > 5 or player.coord1 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame()
    if player.coord2 > 5 or player.coord2 < 1:
        print("It's a 5x5 Game, so pick a number between 1 and 5!")
        initiateGame()
    initiatePlayerMap(player.coord1,player.coord2)    
    playGame()

#You guess where the computer ship is.
def playGame():
    print("Try and sink the battleship!")
    print("So far you have used these coordinates:")
    yourzlist = list(zip(yourxlist,yourylist))
    print(yourzlist)
    xxA = input("Guess coordinate 1:" )
    xx = int(xxA)
    yyA = input("Guess  coordinate 2:" )
    yy = int(yyA)
    if xx == ship.coord1 and yy == ship.coord2:
        print("You sunk the ship!")
        print("Good game.")
        time.sleep(3)
        exit()
    if xx != ship.coord1 or yy != ship.coord2: 
        if xx > 5 or xx < 1:
            print("It's a 5x5 Game.")
            time.sleep(1)
            playGame()
        if yy > 5 or yy < 1:
            print("It's a 5x5 Game.")
            time.sleep(1)
            playGame()
        print("Your shot missed the enemy ship. Now it is my turn.")
        yourylist.append(yy)
        yourxlist.append(xx)
        playComputerMap(xx,yy)
        time.sleep(1)
        enemyThinks()

#the computer will come up with two numbers to throw in for coordinates.
def enemyThinks():
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    zlist = list(zip(xlist,ylist))
    print(zlist)
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
    print("I haven't tried:",x,y,".")
    enemyTries(x,y)
    return()

#The computer will now attempt to blow up your ship.
def enemyTries(x,y):
    if x == player.coord1 and y == player.coord2:
        print("I blew up your ship!")
        print("Good game.")
        time.sleep(3)
        exit()
    if x != player.coord1 or y != player.coord2:
        print("I missed.")
        time.sleep(1)
        xlist.append(x)
        ylist.append(y)
        playPlayerMap(x,y)
#If it misses, it's your turn again.
        playGame()
    
#The enemy coords are stored here.
xlist = []
ylist = [] 
zlist = []

#The player coords are stored here.
yourxlist = []
yourylist = []
yourzlist = []

#these are the player and enemy maps
playerMap = ([0,1,2,3,4,5],[1,0,0,0,0,0],[2,0,0,0,0,0],[3,0,0,0,0,0],[4,0,0,0,0,0],[5,0,0,0,0,0])
computerMap = ([0,1,2,3,4,5],[1,0,0,0,0,0],[2,0,0,0,0,0],[3,0,0,0,0,0],[4,0,0,0,0,0],[5,0,0,0,0,0])

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
    drawPlayerMap()

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
    drawComputerMap()

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
                      print("HIT!!!")
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
                      print("HIT!!!")
                      i[xindex] = 5
                    i[xindex] = 7
    drawComputerMap()
                    
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

initiateGame()


    


                                