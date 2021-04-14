from turtle import *
from Szam import Szam
from Clock import Clock

class main:
    screen = Screen()
    clk = Clock(screen)
    #secondleft=Szam()
    #secondright=Szam()
    Sz1 = Szam()
    Sz2 = Szam()
    Sz3 = Szam()
    Sz4 = Szam()
    points = Szam()

    Sz1.t.goto(-400, 0)
    Sz2.t.goto(-200, 0)
    Sz3.t.goto(100, 0)
    Sz4.t.goto(300, 0)
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
        self.Sz1.two()
        self.Sz2.two()
        self.points.pontok()
        self.Sz3.two()
        self.Sz4.two()




        self.screen.mainloop()

main()