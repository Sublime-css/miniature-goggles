arenaMax = 10
scaleMax = 5
turnsMax = 500
accuracyMax = 1
count = 50
move = 1
nameList = []

import random

class instance:

    def __init__(self, name):
        self.name = name
        nameList.append(self.name)

#to give statistically improved performance based on sucessfullness of last round#
    def renew(self, scaleBias, turnsBias, accuracyBias):
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

    #for the unlucky ones#
##    def __del__(self):
##        print("Instance number" , self.name , "has been deleated due to poor performance :(")
##        nameList.remove(self.name)

def createBots(count,a,b,c):
    print("Instance data:")
    for i in range(0, count):
        instance(i)
        instance(i).renew(0,0,0)

def manager():
    while True:
        instanceX = 0
        instanceY = 0
        for i in nameList:

            instance(i).attempts += 1

            if instance(i).attempts == instance(i).turns:
                break

            if chaseY == instance(i).Ypos & chaseX == instance(i).chaseY:
                instance(i).sucess += 1
                break

            chaseX = chaseX + random.randint(-1 * move, move)
            chaseY = chaseY + random.randint(-1 * move, move)

            if chaseX > instance(i).Xpos:
                instance(i).Xpos += (1 * scale)
                if chaseX < instance(i).Xpos:
                    instance(i).Xpos = chaseX

            if chaseY > instance(i).Ypos:
                instance(i).Ypos += (1 * scale)
                if chaseY < instance(i).Ypos:
                    instance(i).Ypos = chaseY

            if chaseX < instance(i).Xpos:
                instance(i).Xpos -= (1 * scale)
                if chaseX > instance(i).Xpos:
                    instance(i).Xpos = chaseX

            if chaseY < instance(i).Ypos:
                instance(i).Ypos -= (1 * scale)
                if chaseY > instance(i).Ypos:
                    instance(i).Ypos = chaseY

        average = 0

        for a in nameList:

            #kill the failures
            if instance(a).sucess == 0:
                nameList.remove(a)

            #reset instance to 0 and count average
            else:
                average += instance(a).turns
                instance(a).turns = 0
                instance(a).sucess = 0

        #get average
        average /= len(nameList)

        #kill worst 50% of instances:
        for a in nameList:
            if a.turns < average:
                nameList.remove(a)

        #ensure half are dead becasue floats are weird:
        while len(nameList) > count / 2:
            del nameList[0]

        scaleBias = 0
        turnsBias = 0
        accuracyBias = 0

        for i in 0.5 * len(nameList):
            scaleBias += instance(i).scale
        scaleBias /= len(nameList)

        for i in 0.5 * len(nameList):
            turnsBias += instance(i).scale
        turnsBias /= len(nameList)

        for i in 0.5 * len(nameList):
            accuracyBias += instance(i).scale
        accuracyBias /= len(nameList)

        for i in 0.5 * len(nameList):
            instance(i).renew(scaleBias, turnsBias, accuracyBias)

        while len(nameList) < count:
            createBots(1, scaleBias, turnsBias, accuracyBias)

createBots(count, 0,0,0)
#manager()