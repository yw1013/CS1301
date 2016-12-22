##Yea Won Yoon
##B3
##903076043
##yyoon75/yw1013@gatech.edu
##I worked on the homework assignment alone, using only this semester's course materials.

from Graphics import *

win = Window("My Face", 500, 500)

face = Oval((250,220), 140, 160)
face.fill = Color("bisque")
face.draw(win)

eyeL = Oval((190, 220), 30, 15)
eyeL.fill = Color("white")
eyeL.draw(win)

eyeBallL = Circle((190, 220), 13)
eyeBallL.fill = Color("black")
eyeBallL.draw(win)

eyeR = Oval((310, 220), 30, 15)
eyeR.fill = Color("white")
eyeR.draw(win)

eyeBallR = Circle((310, 220), 13)
eyeBallR.fill = Color("black")
eyeBallR.draw(win)

nose = Polygon((250, 230), (240, 275), (260, 275))
nose.fill = Color("moccasin")
nose.draw(win)

mouth = Polygon((175, 320), (250, 350), (325,320), (250,320))
mouth.fill = Color("red")
mouth.draw(win)

hat = Pie((250, 160), 135, 180, 360-0)
hat.fill = Color("turquoise")
hat.draw(win)

hatOne = Polygon((116, 160), (250, 100), (384,160), (384,160))
hatOne.fill = Color("Blue")
hatOne.draw(win)
