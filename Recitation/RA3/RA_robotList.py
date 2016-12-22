##Yea Won Yoon
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.


from Myro import *
init("/dev/tty.Fluke2-0693-Fluke2")


def getValues(numSamples):
    i = 0
    sensorList = []
    for i in range(numSamples):
        sensorList.append(getLight("center"))
        turnLeft(1,0.25)
    return(sensorList)


import math
def printStatistics(numbers):
    a = len(numbers)
    b = sum(numbers)/float(len(numbers))
    c = max(numbers)
    d = min(numbers)
    e = len([i for i in numbers if i%2==0])
    print("You gave me a list of",a,"numbers. Their average was",b,".The largest was",c,",the smallest was",d,".Only",e,"of them were even numbers.")


