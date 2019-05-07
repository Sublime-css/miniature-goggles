import random

#List of instance names:
nameList = []

#Bigger --> slower deterioration of weight manuverability. 10,000 seems to work.
learnRate = 10000

#repeats, higher --> better.
count = 10000
#Data on which to perfect weights.
trainingSet = [
[1,0,1,0,1],
[0,0,1,0,1],
[0,1,0,1,0],
[0,1,0,1,0],
[0,0,1,0,1]
]

#For feedback loop:
trainingAnswers = [1,1,0,0,1]

#The basic learner:
class Neuron:

    def __init__(self, name):
        self.forwardWeight = (random.randint(0,100))/100
        self.backWeight = 0.01
        nameList.append(self)
        self.name = name
        print("instance Number: ", self.name, "says Hello, world!")

    #pass data down to the output stage:
    def dataForward(self, input):
        return(input * self.forwardWeight)
    #For the feedback loop
    def dataBack(self, guess, answer):
        if guess > answer:
            self.forwardWeight -= self.backWeight
            print(self.name , "Decreased data weight to compensate for error -- " , self.forwardWeight)
            self.backWeight = ((self.backWeight / learnRate) * (learnRate - 1))
        else:
            if guess < answer and self.forwardWeight > 0:
                self.forwardWeight += self.backWeight
                print(self.name , "Increased data weight to compensate for error" , self.forwardWeight)
                self.backWeight = ((self.backWeight / learnRate) * (learnRate + 1))
            else:
                pass

#to test the neurons, get their results, and give them feedback:
def manager(repeats):

    for i in range(0, len(trainingAnswers)):
        i = Neuron(i)

    for repitition in range(0,repeats):

        outerInt = 0
        for outerNames in nameList:

            result = 0
            innerInt = 0
            for innerNames in nameList:
                result += innerNames.dataForward(trainingSet[outerInt][innerInt])
                innerInt += 1

            outerNames.dataBack(result / len(nameList), trainingAnswers[outerInt])
            print("\r Guess:", result / len(nameList), "Answer:", trainingAnswers[outerInt])
            outerInt +=1

manager(count)