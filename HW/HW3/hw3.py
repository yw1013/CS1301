##Yea Won Yoon
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.

def tallEnough(height):
    cm = int(height)/0.38370
    if cm < 120:
        return False
    elif cm > 190:
        return False
    else:
        return True


def whereIsWaldo(Int1,Int2):
    Int1 = input("Guess Waldo's x-coordinate")
    Int2 = input("Guess Waldo's y-coordinate")
    if int(Int1) == 5 and int(Int2) == 4:
        return 'You found Waldo.'
    else:
        return 'Couldn\'t find Waldo. Better luck next time'


import string
def allLetters(userString):
    newString = ""
    for letter in userString:
        if letter in string.ascii_letters:
            newString = newString + letter
    return newString


def replaceLetter(aString,aLetter):
    alphabet = input("Input a letter")
    num = 0
    while(num == 0):
        for letter in aString:
            if letter == alphabet:
                num = 1
        if num == 0:
            alphabet = input("Letter not in string. Input a letter")
    newString = ""
    for letter in aString:
        if letter != alphabet:
            newString = newString + letter
        else:
            newString = newString + aLetter
    print(newString)


def CountUp(start,end,increment):
    num = start
    while(num <= end):
        print(num)
        num = num+increment
    print("Done!")


def numMountainRange(X):
    num = 1
    while(num <= X):
        a = 1
        answer = ""
        while(a <= num):
            answer = answer + str(num)
            a = a+1
        a = 1
        while(a <= ((X-num)*2)):
            answer = answer + " "
            a = a+1
        a = 1
        while(a <= num):
            answer = answer + str(num)
            a = a+1
        print(answer)
        num = num + 1


def printTimestable():
    print("Times:  ",end = "")
    a = 1
    while(a < 10):
        print(a,"\t",end = "")
        a = a+1
    for b in range(1,10):
        print("\n",b,"\t",end = "")
        for c in range(1,10):
            d = c*b
            print(d,"\t",end = "")
    return None


def printTimes(N):
    print("Times:  ",end = "")
    a = 1
    while(a < N+1):
        print(a,"\t",end = "")
        a = a+1
    for b in range(1,N+1):
        print("\n",b,"\t",end = "")
        for c in range(1,N+1):
            d = c*b
            print(d,"\t",end = "")
    return None
