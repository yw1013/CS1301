from Myro import *
init("COM6")
def avoidWalls():
    for t in timer(20):
        l = getIR("left")
        r = getIR("right")
        c = getIR("center")
        if l == 0 or r == 0 or c == 0:
            forward(1,1)
            turnRight(1,.75)
        else:
            backward(0.75)
    for t in timer(4):
        forward(1,1)
        beep(1,2200)
        backward(1,1)        