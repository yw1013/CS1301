#Gyungyoon Yoo, Ik tae Kim, and Yea Won Yoon
#CS-1301-B03
#903076043/yw1013@gatech.edu
#We worked on the homework assignment alone, using only this semester's course materials.

from Myro import*
#init("/dev/tty.Fluke2-0693-Fluke2")

setPicSize("small")

def filmingCode1(): #robot and dog are playing
    piclist = []
    for t in timer(37):
        pic = takePicture()
        piclist.append(pic)
    savePicture (piclist, "1filmingCode1.gif")

def seeingRed(): #robot and dog found snakes
    p = takePicture()
    savePicture(p, "2seeingRed.jpg")
    p2 = makePicture("2seeingRed.jpg")
    for pixel in getPixels(p2):
        setRed(pixel,255)
    savePicture(p2, "3seeingRed2.jpg")


def others ():
    snake1 = takePicture ()
    savePicture (snake1, "snake1.jpg")
    show (snake1)
    wait(5)

    robot =  takePicture()
    savePicture (robot , "robot.jpg")
    show (robot)

def screenShake1 (): #snake face shakes
    n = takePicture()
    o = savePicture (n, "snake1.jpg")
    p = makePicture("snake1.jpg")
    n1 = takePicture()
    o2 = savePicture (n, "snake1.jpg")
    p2 = makePicture("snake1.jpg")
    pic = []
    li = []
    c = getHeight(p)
    d = getWidth(p)

    for t in range(4):
        for n in [10,-10]:
            for x in range(d):
                for y in range (c):
                        a = x -n
                        b = y -n
                        pix = getPixel(p,x,y)
                        values = getRGB(pix)
                        pix2= getPixel(p2,a,b)
                        setRGB(pix2,values)

            pic.append(copyPicture(p2))


    savePicture(pic,"4snake1Shake.gif")

def screenShake2(): #robot face shakes
    n = takePicture()
    o = savePicture (n, "robot.jpg")
    p = makePicture("robot.jpg")
    n1 = takePicture()
    o2 = savePicture (n, "robot.jpg")
    p2 = makePicture("robot.jpg")
    pic = []
    li = []
    c = getHeight(p)
    d = getWidth(p)

    for t in range(4):
        for n in [10,-10]:
            for x in range(d):
                for y in range (c):
                        a = x -n
                        b = y -n
                        pix = getPixel(p,x,y)
                        values = getRGB(pix)
                        pix2= getPixel(p2,a,b)
                        setRGB(pix2,values)

            pic.append(copyPicture(p2))


    savePicture(pic,"5robotShake.gif")


def filmingCode105(): #robot and dog turn and run away
    wait (3)
    piclist = []
    for t in timer(22):
        pic = takePicture()
        piclist.append(pic)
    savePicture (piclist, "6filmingCode1-5.gif")

def filmingCode2(): #robot and dog turn and disappear
    piclist = []
    for t in timer(15):
        pic = takePicture()
        piclist.append(pic)
    savePicture (piclist, "7filmingCode2.gif")

def filmingCode3(): #robot and dog appear again
    wait (3)
    piclist = []
    for t in timer(15):
        pic = takePicture()
        piclist.append(pic)
    savePicture (piclist, "8filmingCode3.gif")

def fade():
    wait (3)
    p1 = takePicture()
    p2 = takePicture()
    p3 = takePicture()
    p4 = takePicture()
    p5 = takePicture()
    p6 = takePicture()
    p7 = takePicture()
    p8 = takePicture()
    p9 = takePicture()
    p10 = takePicture()
    p11 = takePicture()

    for pixel in getPixels(p1):
        setRed(pixel, getRed(pixel))
        setGreen(pixel, getGreen(pixel))
        setBlue(pixel, getBlue(pixel))
    for pixel in getPixels(p2):
        setRed(pixel, getRed(pixel)*0.9)
        setGreen(pixel, getGreen(pixel)*0.9)
        setBlue(pixel, getBlue(pixel)*0.9)
    for pixel in getPixels(p3):
        setRed(pixel, getRed(pixel)*0.8)
        setGreen(pixel, getGreen(pixel)*0.8)
        setBlue(pixel, getBlue(pixel)*0.8)
    for pixel in getPixels(p4):
        setRed(pixel, getRed(pixel)*0.7)
        setGreen(pixel, getGreen(pixel)*0.7)
        setBlue(pixel, getBlue(pixel)*0.7)
    for pixel in getPixels(p5):
        setRed(pixel, getRed(pixel)*0.6)
        setGreen(pixel, getGreen(pixel)*0.6)
        setBlue(pixel, getBlue(pixel)*0.6)
    for pixel in getPixels(p6):
        setRed(pixel, getRed(pixel)*0.5)
        setGreen(pixel, getGreen(pixel)*0.5)
        setBlue(pixel, getBlue(pixel)*0.5)
    for pixel in getPixels(p7):
        setRed(pixel, getRed(pixel)*0.4)
        setGreen(pixel, getGreen(pixel)*0.4)
        setBlue(pixel, getBlue(pixel)*0.4)
    for pixel in getPixels(p8):
        setRed(pixel, getRed(pixel)*0.3)
        setGreen(pixel, getGreen(pixel)*0.3)
        setBlue(pixel, getBlue(pixel)*0.3)
    for pixel in getPixels(p9):
        setRed(pixel, getRed(pixel)*0.2)
        setGreen(pixel, getGreen(pixel)*0.2)
        setBlue(pixel, getBlue(pixel)*0.2)
    for pixel in getPixels(p10):
        setRed(pixel, getRed(pixel)*0.1)
        setGreen(pixel, getGreen(pixel)*0.1)
        setBlue(pixel, getBlue(pixel)*0.1)
    for pixel in getPixels(p11):
        setRed(pixel, 0)
        setGreen(pixel, 0)
        setBlue(pixel, 0)

    pic = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
    savePicture(pic, "9fade.gif")

