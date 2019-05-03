arenaMax = 10
scaleMax = 5
turnsMax = 500
accuracyMax = 1
count = 100
move = 1


import random

class instance:

    #here to make instances iterable#
    nameList = []

    def __init__(self, name, scaleBias, turnsBias, accuracyBias):
        self.name = name
        nameList.append(self.name)
        self.scale = random.randint(-1 * scaleMax, scaleMax) + scaleBias
        self.turns = random.randint(0, turnsMax) + turnsBias
        self.Ypos = 0
        self.Xpos = 0
        self.attempts = 0
        while self.turns <= 0:
            self.turns += 1
        self.accuracy = random.randint(0, 101) / 100 + accuracyBias
        while self.accuracy <= 0:
            self.accuracy += 0.01
        print("Instance Number:",self.name, "Scale:", self.scale, "Turns:", self.turns, "Accuracy:",self.accuracy)
        if self.name % 10 == 0:
            print("\r")

#to give statistically improved performance based on sucessfullness of last round#
##    def renew(self, newName, scaleBias, turnsBias, accuracyBias):
##        self.name = newName
##        nameList.append(self.name)
##        self.scale = random.randint(-1 * scaleMax, scaleMax) + scaleBias
##    self.turns = random.randint(0, turnsMax) + turnsBias
##    self.Ypos = 0
##    self.Xpos = 0
##    self.attempts = 0
##    while self.turns <= 0:
##        self.turns += 1
##    self.accuracy = random.randint(0, 101) / 100 + accuracyBias
##    while self.accuracy <= 0:
##        self.accuracy += 0.01
##    print("Instance Number:",self.name, "Scale:", self.scale, "Turns:", self.turns, "Accuracy:",self.accuracy)
##    if self.name % 10 == 0:
##        print("\r")
##
##    #for the unlucky ones#
##    def __del__(self):
##        print("Instance number" , self.name , "has been deleated due to poor performance :(")
##        nameList.remove(self.name)


def createBots(count,a,b,c):
    print("Instance data:")
    for i in range(0, count):
        instance(i,0,0,0)


def manager():
    instanceX = 0
    instanceY = 0
    for i in nameList:

        i.attempts += 1

        if i.attempts == i.turns:
            break

        if chaseY == i.Ypos & chaseX == i.chaseY:
            i.sucess += 1
            break

        chaseX = chaseX + random.randint(-1 * move, move)
        chaseY = chaseY + random.randint(-1 * move, move)

        if chaseX > i.Xpos:
            i.Xpos += (1 * scale)
            if chaseX < i.Xpos:
                i.Xpos = chaseX

        if chaseY > i.Ypos:
            i.Ypos += (1 * scale)
            if chaseY < i.Ypos:
                i.Ypos = chaseY

        if chaseX < i.Xpos:
            i.Xpos -= (1 * scale)
            if chaseX > i.Xpos:
                i.Xpos = chaseX

        if chaseY < i.Ypos:
            i.Ypos -= (1 * scale)
            if chaseY > i.Ypos:
                i.Ypos = chaseY

    average = 0

    for a in nameList:

        #kill the failures
        if a.sucess == 0:
            del a

        #reset instance to 0 and count average
        else:
            average += a.turns
            a.turns = 0
            a.sucess = 0

    #get average
    average /= len(nameList)

    #kill worst 50% of instances:
    for a in nameList:
        if a.turns < average:
            del a

    #ensure half are dead becasue floats are weird:
    while len(nameList) > count / 2:
        del nameList[0]

    scaleBias = 0
    turnsBias = 0
    accuracyBias = 0

    for i in 0.5 * len(nameList):
        scaleBias += i.scale
    scaleBias /= instance

    for i in 0.5 * len(nameList):
        turnsBias += i.scale
    turnsBias /= instance

    for i in 0.5 * len(nameList):
        accuracyBias += i.scale
    accuracyBias /= instance

    for i in 0.5 * len(nameList):
        i.renew(instance + 1, scaleBias, turnsBias, accuracyBias)

    while len(nameList) < count:
        createBots(1, scaleBias, turnsBias, accuracyBias)

createBots(count, 0,0,0)