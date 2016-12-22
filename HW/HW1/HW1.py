##Yea Won Yoon
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.

def machToFPS():
    mach = input("Enter the speed in mach")
    fps = float(mach)/float(1116.4370079)
    print(fps, "feet/second")

def sqPyramidVolume():
    length = input("Enter the length of the base of the square pyramid")
    height = input("Enter the height of the square pyramid in inches")
    volume = float(length)**2*float(height)/float(3)
    print("Volume of the square pyramid is", volume, "inches-cube")

def makeChange():
    cent = input("Enter the number of cents")
    dollars = float(cent)//100
    quarters = float(cent)%100//25
    dimes = float(cent)%100%25//10
    nickels = float(cent)%100%25%10//5
    pennies = float(cent)%100%25%10%5
    print(dollars, "dollars", quarters, "quarter", dimes, "dime", nickels, "nickel and", pennies, "pennies")

def PPIIndex():
    weight = input("Enter your weight in pounds")
    height = input("Enter your height in inches")
    PPI = float(weight)*1.125/float(height)
    print("Your corrected PPI is", "%.1f" %PPI)


def aStrin():
    aStr = "This is only a test!"
    for char in aStr:
        print(char*2)


def aString():
    aStr = "This is only a test!"
    index = 0
    while index < len(aStr):
        char = aStr[index]
        print(char*2)
        index = index + 1