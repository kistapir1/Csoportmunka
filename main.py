from turtle import *
from Szam import Szam
from Clock import Clock

class main:
    screen = Screen()
    clk = Clock(screen)
    secondleft=Szam()
    secondright=Szam()
    minuteleft=Szam()
    minuteright=Szam()
    # Sz1 = Szam()
    # Sz2 = Szam()
    # Sz3 = Szam()
    # Sz4 = Szam()
    points = Szam()

    minuteleft.t.goto(-400, 0)
    minuteright.t.goto(-200, 0)
    secondleft.t.goto(100, 0)
    secondright.t.goto(300, 0)
    def Second(self):
        print(self.clk.sec())
        self.secondleft.Szamok(self.clk.leftNumber(self.clk.sec()))
        self.secondright.Szamok(self.clk.rightNumber(self.clk.sec()))

    def Minute(self):
        print(self.clk.min())
        self.minuteleft.Szamokxd(self.clk.leftNumber(self.clk.min()))
        self.minuteright.Szamokxd(self.clk.rightNumber(self.clk.min()))




    def __init__(self):
        self.screen.bgcolor("black")
        self.clk.setOnSecondChangeListener(self.Second)
        self.clk.setOnMinuteChangeListener(self.Minute)
        #self.secondright.t.forward(150)
        #self.secondright.five()
        # self.Sz1.two()
        # self.Sz2.two()
        # self.points.pontok()
        #self.Sz3.two()
        #self.Sz4.two()




        self.screen.mainloop()

main()