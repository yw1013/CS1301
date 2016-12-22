##Yea Won Yoon
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.

from Myro import *
init("/dev/tty.Fluke2-0693-Fluke2")


def morningRoutine(numTrick):
    if numTrick == 0:
        return none

    elif numTrick == 1:
        rotate(1,2)  #Scribby moves forward and returns to me (fetch)
        forward(3,2)
        rotate(1,2)
        forward(3,2)

    elif numTrick == 2:
        rotate(1,1.8)  #Scribby moves forward and returns to me (fetch)
        forward(3,2)
        rotate(1,1.8)
        forward(3,2)
        wait(1)

        rotate(1,1.8)  #Scribby spins around (chasing its own tail)
        forward(2,1)
        rotate(3,8)
        forward(2,1)

    elif numTrick == 3:
        rotate(1,2)  #Scribby moves forward and returns to me (fetch)
        forward(3,2)
        rotate(1,2)
        forward(3,2)
        wait(1)

        rotate(1,2)  #Scribby spins around (chasing its own tail)
        forward(2,1)
        rotate(3,6)
        forward(2,1)
        wait(1)

        rotate(1,1)    #Scribby moves around the room very slowly (crawling on its belly)
        forward(0.4,2)
        rotate(1,1)
        forward(0.4,2)
        rotate(1,1)
        forward(0.4,2)
        rotate(1,1)
        forward(0.4,2)
        turnRight(1,0.2)
