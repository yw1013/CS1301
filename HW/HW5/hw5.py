##Yea Won Yoon
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.

from Graphics import*
from Myro import*
init("/dev/tty.Fluke2-0693-Fluke2")

win = Window("myMovements",500,500)
f = open("myMovements.txt", "w")
f.close()

def key(win,event): #part1,2
    f = open("myMovements.txt","a" )
    print(event.key)
    if event.key == "Up":
        forward(1,.1)
        f.write("forward    ")
        f.write(".1"+"\t")
        a = getLight("left") /(getLight("right")+getObstacle("right"))
        f.write(str(a)+"\n")
    if event.key == "Down":
        backward(1,.1)
        f.write("backward   ")
        f.write(".1"+"\t")
        a = getLight("left") /(getLight("right")+getObstacle("right"))
        f.write(str(a)+"\n")
    if event.key == "Left":
        turnLeft(1,.1)
        f.write("Left       ")
        f.write(".1"+"\t")
        a = getLight("left") /(getLight("right")+getObstacle("right"))
        f.write(str(a)+"\n")
    if event.key == "Right":
        turnRight(1,.1)
        f.write("Right      ")
        f.write(".1"+"\t")
        a = getLight("left") /(getLight("right")+getObstacle("right"))
        f.write(str(a)+"\n")
    if event.key == "b":
        beep(.2,800)
        f.write("Beep       ")
        f.write(".2"+"\n")

    f.close()


onKeyPress(key)

def collectData(file1,direction): #part3
    f = open(file1)
    data = f.read()
    dataList = data.split()
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for x in dataList:
        if x == "Beep":
            cnt1 = cnt1 + 1
        if x == direction:
            cnt2 += 1
        if x == "forward" or x == "backward" or x == "Right" or x =="Left":
            cnt3 += 1
            time = 0.1*cnt3
    m = "The robot traveled for {} seconds total, beeping {} times. This robot moved {}s a total of {} times"
    f.close()
    return m.format(time,cnt1,direction,cnt2)

def replay(files): #part4
    f = open(files)
    data= f.read()
    dataList = data.split()
    for x in dataList:
        if x == "Beep":
            print("beep")
            beep(.2,800)
        if x== "forward":
            print("move forwards")
            forward(1,.1)
        if x== "backward":
            print("move backwards")
            backward(1,.1)
        if x== "Right":
            print("turn right")
            turnRight(1,.1)
        if x== "Left":
            print("turn left")
            turnLeft(1,.1)
    f.close()