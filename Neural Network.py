import random

nameList = []

trainingSet = [
[1,0,1,0,1],
[0,0,1,0,1],
[0,1,0,1,0],
[0,1,0,1,0],
[0,0,1,0,1]
]

trainingAnswers = [1,1,0,0,1]

class Neuron:

    def __init__(self, name):
        self.forwardWeight = (random.randint(0,100))/100
        self.backWeight = 0.01
        nameList.append(self)
        self.name = name
        print("instance Number: ", self.name, "says Hello, world!")

    def dataForward(self, input):
        return(input * self.forwardWeight)

    def dataBack(self, guess, answer):
        if guess > answer:
            self.forwardWeight -= self.backWeight
            print(self.name , "Decreased data weight to compensate for error -- " , self.forwardWeight)
            self.backWeight = ((self.backWeight / 10000) * 9999)
        else:
            if guess < answer and self.forwardWeight > 0:
                self.forwardWeight += self.backWeight
                print(self.name , "Increased data weight to compensate for error" , self.forwardWeight)
                self.backWeight = ((self.backWeight / 10000) * 10001)
            else:
                pass

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

manager(10000)