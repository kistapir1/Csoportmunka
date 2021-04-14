from turtle import *
from Szam import Szam
from Clock import Clock

class main:
    screen = Screen()
    clk = Clock(screen)
    Sz1 = Szam()
    Sz2 = Szam()
    Sz3 = Szam()
    Sz4 = Szam()
    Sz5 = Szam()
    Sz6 = Szam()
    points = Szam()

    Sz1.t.goto(-640, 0)
    Sz2.t.goto(-440, 0)
    points.t.goto(-265, 0)
    Sz3.t.goto(-190, 0)
    Sz4.t.goto(10, 0)
    Sz5.t.goto(260, 0)
    Sz6.t.goto(460, 0)


    def Second(self):
        print(self.clk.sec())
        #self.secondright.two()
        #self.secondleft.five()

    def Minute(self):
        print(self.clk.min())

    def __init__(self):
        self.screen.bgcolor("black")
        self.clk.setOnSecondChangeListener(self.Second)
        self.clk.setOnMinuteChangeListener(self.Minute)
        #self.secondright.t.forward(150)
        #self.secondright.five()
        self.Sz1.six()
        self.Sz2.six()
        self.points.pontok()
        self.points.t.goto(185, 0)
        self.Sz3.six()
        self.Sz4.three()
        self.points.pontok()
        self.Sz5.three()
        self.Sz6.three()



        self.screen.mainloop()

main()