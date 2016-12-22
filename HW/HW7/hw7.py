##Yea Won Yoon
##Nija Kurien
##B3
##We worked on the homework assignment alone, using only this semester's course materials.


from Myro import*
from Graphics import*
#init("/dev/tty.Fluke2-069C-Fluke2")
#init("/dev/tty.Fluke2-0693-Fluke2")

def seeingRed():
    p = takePicture()
    savePicture(p, "seeingRed.jpg")
    show(p)
    p2 = makePicture("seeingRed.jpg")
    for pixel in getPixels(p2):
        setRed(pixel,255)
    savePicture(p2, "seeingRed2.jpg")
    show(p2)


def overlay():
    p = takePicture()
    savePicture(p, "overlay.jpg")
    show(p)
    turnLeft(1,1)
    p2 = takePicture()
    savePicture(p2,"overlayP.png")
    for x in range(200,251):
        for y in range(200,251):
            pixel = getPixel(p, x, y)
            pixel2 = getPixel(p2, x, y)
            setRed(pixel, getRed(pixel2))
            setGreen(pixel,getGreen(pixel2))
            setBlue(pixel,getBlue(pixel2))
    savePicture(p, "overlay2.jpg")
    show(p)


def fade():
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

    show(p1)
    wait(0.2)
    show(p2)
    wait(0.2)
    show(p3)
    wait(0.2)
    show(p4)
    wait(0.2)
    show(p5)
    wait(0.2)
    show(p6)
    wait(0.2)
    show(p7)
    wait(0.2)
    show(p8)
    wait(0.2)
    show(p9)
    wait(0.2)
    show(p10)
    wait(0.2)
    show(p11)

    pic = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
    savePicture(pic, "fade.gif")

def lensFlare():
    p = takePicture()
    savePicture(p, "lensFlare.jpg")
    show(p)
    p2 = makePicture("lensFlare.jpg")
    for x in range (1280):
        for y in range (800):
            if 600<x<700 and 300<y<400:
                pixel = getPixel(p2, x, y)
                setRed(pixel,getRed(pixel)*2)
                setGreen(pixel,getGreen(pixel)*2)
                setBlue(pixel,getBlue(pixel)*2)
    savePicture(p2, "lensFlare2.jpg")
    show(p2)


def splitScreen():
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
    p12 = takePicture()
    turnLeft(1,1)
    s1 = takePicture()
    s2 = takePicture()
    s3 = takePicture()
    s4 = takePicture()
    s5 = takePicture()
    s6 = takePicture()
    s7 = takePicture()
    s8 = takePicture()
    s9 = takePicture()
    s10 = takePicture()
    s11 = takePicture()
    s12 = takePicture()

    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p1, x, y)
            pixel2 = getPixel(s1, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p2, x, y)
            pixel2 = getPixel(s2, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p3, x, y)
            pixel2 = getPixel(s3, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p4, x, y)
            pixel2 = getPixel(s4, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p5, x, y)
            pixel2 = getPixel(s5, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p6, x, y)
            pixel2 = getPixel(s6, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p7, x, y)
            pixel2 = getPixel(s7, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p8, x, y)
            pixel2 = getPixel(s8, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p9, x, y)
            pixel2 = getPixel(s9, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p10, x, y)
            pixel2 = getPixel(s10, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p11, x, y)
            pixel2 = getPixel(s11, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))
    for x in range (0,1281):
        for y in range (0,401):
            pixel1 = getPixel(p12, x, y)
            pixel2 = getPixel(s12, x, y)
            setRed (pixel1,getRed(pixel2))
            setGreen (pixel1,getGreen(pixel2))
            setBlue (pixel1,getBlue(pixel2))

    show(p1)
    wait(0.3)
    show(p2)
    wait(0.3)
    show(p3)
    wait(0.3)
    show(p4)
    wait(0.3)
    show(p5)
    wait(0.3)
    show(p6)
    wait(0.3)
    show(p7)
    wait(0.3)
    show(p8)
    wait(0.3)
    show(p9)
    wait(0.3)
    show(p10)
    wait(0.3)
    show(p11)
    wait(0.3)
    show(p12)

    pic = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
    savePicture(pic, "splitScreen.gif")


