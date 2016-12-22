##Yea Won Yoon, Nija Kurien
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.


from Graphics import*
from Myro import*
setPicSize("small")

#init("/dev/tty.Fluke2-069C-Fluke2")


def findColor(pic):

    myPic = makePicture(pic)
    show(myPic)

    countR = 0
    countG = 0
    countB = 0
    countY = 0

    for pix in getPixels(myPic):
        #
        a = getRGB(pix)
        print(a)

        if abs(((getRed(pix))-(getGreen(pix))))/(getRed(pix)+0.1) < 0.1 and abs(((getRed(pix))-(getBlue(pix))))/(getRed(pix)+0.1) > 0.6:
            countY = countY + 1

        elif abs(getRed(pix) - getGreen(pix))/(getRed(pix)+0.1)  > .6 and abs(getRed(pix) - getBlue(pix))/(getRed(pix)+0.1)  > .6 and getRed(pix)>100:
            countR = countR +1
        elif abs(getGreen(pix) - getRed(pix))/(getGreen(pix)+0.1)  > .6 and abs(getGreen(pix) - getBlue(pix))/(getGreen(pix)+0.1)  > .6 and getGreen(pix)>100:
            countG = countG + 1
        elif (getBlue(pix)) > (getRed(pix)) and (getBlue(pix)) > (getGreen(pix)):
            countB = countB +1

    print("r: " + str(countR)+ " , g: " + str(countG) + " , b: " + str(countB) + " , y: " + str(countY) )

    if countY > countR and countY > countG:
        return ("Yellow")

    elif countR > countG and countR > countB:
        return ("Red")

    elif countG > countR and countG > countB:
        return ("Green")

    #elif 0.6*countR < countB < 1.4*countR and 0.6*countR < countG < 1.4*countR:
        #return("White")

    else:
        return("White")


def turn():
    setLED("right", "off")
    setLED("left", "off")
    if heads() == True:
        setLED("left", "on")
        setLED("left", "off")
        setLED("left", "on")
        setLED("left", "off")
        setLED("left", "on")
        setLED("left", "off")
        turnRight(1,.65)
    else:
        setLED("right", "on")
        setLED("right", "off")
        setLED("right", "on")
        setLED("right", "off")
        setLED("right", "on")
        setLED("right", "off")
        turnLeft(1,.65)


def stopLight():
    s = findColor(takePicture())
    print (s)
    if s == "Green":
        forward(2,1)
        stopLight()

    elif s == "Yellow":
        forward(2,.5)
        stopLight()

    elif s == "White" :
        turn()
        stopLight()

    elif s == "Red":
        stop()
        beep(2,1000)




