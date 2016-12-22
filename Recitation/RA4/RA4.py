##Yea Won Yoon, Nija Kurien
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.

from Graphics import*
from Myro import*


def colorSwap(pic):

    myPic = makePicture( pic )
    show(myPic)

    for pix in getPixels(myPic):

        if getRed(pix) > getGreen(pix) and getRed(pix) > getBlue(pix):
            setGreen(pix, 255)
            setBlue(pix, 0)
            setRed(pix, 0)
        elif getGreen(pix) > getRed(pix) and getGreen(pix) > getBlue(pix):
            setBlue(pix, 255)
            setRed(pix, 0)
            setGreen(pix, 0)
        elif getBlue(pix) > getRed(pix) and getBlue(pix) > getGreen(pix):
            setRed(pix, 255)
            setGreen(pix, 0)
            setBlue(pix, 0)

    savePicture(myPic, 'colorSwap.jpg')








