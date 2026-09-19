from turtle import *
class Face:
    def __init__(self,xpos,ypos):
        self.size=90
        self.coord=(xpos,ypos)
        self.noseSize="small"
    def setSize(self,radius):
        self.size=radius
    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawNose()
        self.drawMouth()
        pensize(5)
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)          




f1=Face(0,0)
f1.draw()
showturtle()