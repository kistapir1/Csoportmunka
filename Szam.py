from turtle import *
from Clock import Clock


class Szam:
    screen = Screen()
    t = Turtle
    clk = Clock(screen)

    def __init__(self):
        self.t=Turtle()
        self.screen._delay(0)
        self.t.speed(0)
        # self.t.backward(400)
        # self.position()
        # self.zero()
        # self.one()
        # self.two()
        # self.three()
        # self.four()
        # self.five()
        # self.six()
        # self.seven()
        # self.eight()
        #self.nine()
    def Szamok(self, Szam:int):
        if Szam == 0:
            self.zero()
        if Szam== 1:
            self.one()
        if Szam== 2:
            self.two()
        if Szam== 3:
            self.three()
        if Szam == 4:
            self.four()
        if Szam== 5:
            self.five()
        if Szam== 6:
            self.six()
        if Szam== 7:
            self.seven()
        if Szam== 8:
            self.eight()
        if Szam== 9:
            self.nine()
    def Szamokxd(self, Szam:int):
        if Szam == 0:
            self.zero()
        if Szam== 1:
            self.one()
        if Szam== 2:
            self.two()
        if Szam== 3:
            self.three()
        if Szam == 4:
            self.four()
        if Szam== 5:
            self.five()
        if Szam== 6:
            self.six()
        if Szam== 7:
            self.seven()
        if Szam== 8:
            self.eight()
        if Szam== 9:
            self.nine()


    def trapez(self):
        self.t.fillcolor("light green")
        self.t.begin_fill()
        self.t.forward(130)
        self.t.left(135)
        self.t.forward(50)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(50)
        self.t.end_fill()

    def trapez2(self):
        self.t.fillcolor("light green")
        self.t.begin_fill()
        self.t.forward(130)
        self.t.right(135)
        self.t.forward(50)
        self.t.right(45)
        self.t.forward(60)
        self.t.right(45)
        self.t.forward(50)
        self.t.end_fill()

    def trapezgone(self):
        self.t.fillcolor(0, 0.1, 0)
        self.t.begin_fill()
        self.t.forward(130)
        self.t.left(135)
        self.t.forward(50)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(50)
        self.t.end_fill()

    def trapez2gone(self):
        self.t.fillcolor(0, 0.1, 0)
        self.t.begin_fill()
        self.t.forward(130)
        self.t.right(135)
        self.t.forward(50)
        self.t.right(45)
        self.t.forward(60)
        self.t.right(45)
        self.t.forward(50)
        self.t.end_fill()

    def middle(self):
        self.t.fillcolor("light green")
        self.t.begin_fill()
        self.t.forward(40)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(40)
        self.t.left(90)
        self.t.forward(40)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(40)
        self.t.end_fill()

    def middlegone(self):
        self.t.fillcolor(0, 0.1, 0)
        self.t.begin_fill()
        self.t.forward(40)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(40)
        self.t.left(90)
        self.t.forward(40)
        self.t.left(45)
        self.t.forward(60)
        self.t.left(45)
        self.t.forward(40)
        self.t.end_fill()

    def circle(self):
        self.t.fillcolor("light green")
        self.t.begin_fill()
        for a in range(90):
            self.t.forward(1)
            self.t.right(4)
        self.t.end_fill()


    def zero(self):
        x = self.t.xcor()
        y = self.t.ycor()
        rot = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middlegone()
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(rot)

    def one(self):
        x1 = self.t.xcor()
        y1 = self.t.ycor()
        rot1 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapezgone()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middlegone()
        self.t.penup()
        self.t.goto(x1, y1)
        self.t.setheading(rot1)

    def two(self):
        x2 = self.t.xcor()
        y2 = self.t.ycor()
        rot2 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x2, y2)
        self.t.setheading(rot2)

    def three(self):
        x3 = self.t.xcor()
        y3 = self.t.ycor()
        rot3 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()
        self.t.end_fill()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x3, y3)
        self.t.setheading(rot3)

    def four(self):
        x4 = self.t.xcor()
        y4 = self.t.ycor()
        rot4 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapezgone()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x4, y4)
        self.t.setheading(rot4)

    def five(self):
        x5 = self.t.xcor()
        y5 = self.t.ycor()
        rot5 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x5, y5)
        self.t.setheading(rot5)

    def six(self):
        x6 = self.t.xcor()
        y6 = self.t.ycor()
        rot6 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x6, y6)
        self.t.setheading(rot6)

    def seven(self):
            x7 = self.t.xcor()
            y7= self.t.ycor()
            rot7 = self.t.heading()
            self.t.pendown()
            self.t.color("black")
            self.trapezgone()

            self.t.penup()
            self.t.right(45)
            self.t.forward(10)
            self.t.right(90)
            self.t.forward(10)
            self.t.pendown()
            self.trapez2gone()

            self.t.penup()
            self.t.right(135)
            self.t.forward(140)
            self.t.pendown()
            self.trapez2gone()

            self.t.penup()
            self.t.right(135)
            self.t.forward(140)
            self.t.right(90)
            self.t.forward(10)
            self.t.pendown()
            self.trapez2()

            self.t.penup()
            self.t.right(135)
            self.t.forward(140)
            self.t.right(90)
            self.t.forward(10)
            self.t.pendown()
            self.trapez2()

            self.t.penup()
            self.t.right(135)
            self.t.forward(140)
            self.t.pendown()
            self.trapez2()

            self.t.penup()
            self.t.left(45)
            self.t.forward(5)
            self.t.left(90)
            self.t.forward(17)
            self.t.right(45)
            self.t.pendown()
            self.middlegone()
            self.t.penup()
            self.t.goto(x7, y7)
            self.t.setheading(rot7)

    def eight(self):
        x8 = self.t.xcor()
        y8 = self.t.ycor()
        rot8 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x8, y8)
        self.t.setheading(rot8)

    def nine(self):
        x9 = self.t.xcor()
        y9 = self.t.ycor()
        rot9 = self.t.heading()
        self.t.pendown()
        self.t.color("black")
        self.trapez()

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2gone()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
        self.trapez2()

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
        self.middle()
        self.t.penup()
        self.t.goto(x9, y9)
        self.t.setheading(rot9)

    def pontok(self):
        rot10 = self.t.heading()
        self.t.left(90)
        self.t.forward(80)
        self.circle()
        self.t.forward(100)
        self.circle()
        self.t.penup()
        self.t.goto(0, 1000)
        self.t.setheading(rot10)



