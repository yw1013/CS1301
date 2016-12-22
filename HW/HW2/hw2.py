##Yea Won Yoon, Kiyokuni Yamada
##yw1013@gatech.edu, kiyokuniyamada@gatech.edu
##We worked on the homework assignment alone, using only this semester's course materials.


def quesoForFishy(dollar):
    dollar = int(float(dollar)//2.98)
    return (dollar)


def mailboxes(mailbox):
    lifespan = int(float(mailbox)*2), "to", int(float(mailbox)*6)
    print("Because you have run into", mailbox, "mailbox(es), your car's life has been shortened by anywhere from", int(float(mailbox)*2), "to", int(float(mailbox)*6), "months.")


def concertTicket():
    ticketprice = input("Enter the ticket price:")
    hourlyrate = input("Enter the hourly rate:")
    numhours = float(ticketprice) / float(hourlyrate)
    print("You need to work", "%.2f" % numhours, "hours to buy your ticket")


import math

def boringInterlude(r):
    volumeSphere = 4*math.pi*(r/12)**3/(3)
    return (volumeSphere)


def trafficJam(a,b):
    lanes = int(a)
    milesInFront = float(b)
    return((5280*b*a)/15)


def timeLeft(t):
    batteryPercent = int(input("What is the number of hours that the flashlight battery lasts?"))
    print("%.0f" % float((((float(batteryPercent)*60)-t))*100//(float(batteryPercent)*60)))
    return((float(batteryPercent)*60)-t)


def daffodils(a,b,c):
    numFlower = int(a)
    willingPrice = float(b)
    twelveFlower = float(c)
    print("You will need to contribute $", "%.2f" % float((c*math.ceil(a/12))-b),".")
