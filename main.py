from turtle import *

class Szam:
    screen = Screen()
    t = Turtle()
    screen.bgcolor("black")

    def __init__(self):
        self.screen.delay(0)
        self.trapez()
        self.nulla()
        self.egy()
        self.nine()
        self.screen.mainloop()


    def trapez(self):
        self.t.color("green")
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

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
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

    def nulla(self):
        self.t.color("green")
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

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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
    def egy(self):

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

    def six(self):
        self.t.color("green")
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

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
        self.t.fillcolor("lightgreen")
        self.t.begin_fill()
        self.t.forward(130)
        self.t.right(135)
        self.t.forward(50)
        self.t.right(45)
        self.t.forward(60)
        self.t.right(45)
        self.t.forward(50)
        self.t.end_fill()




        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
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

    def nine(self):
        self.t.color("green")
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



        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
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

    def three(self):
        self.t.color("green")
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

        self.t.penup()
        self.t.right(45)
        self.t.forward(10)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.right(90)
        self.t.forward(10)
        self.t.pendown()
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

        self.t.penup()
        self.t.right(135)
        self.t.forward(140)
        self.t.pendown()
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

        self.t.penup()
        self.t.left(45)
        self.t.forward(5)
        self.t.left(90)
        self.t.forward(17)
        self.t.right(45)
        self.t.pendown()
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

Szam()