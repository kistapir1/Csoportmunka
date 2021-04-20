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
    hourright=Szam()
    hourleft=Szam()

    # Sz1 = Szam()
    # Sz2 = Szam()
    # Sz3 = Szam()
    # Sz4 = Szam()
    points = Szam()

    hourleft.t.goto(-900, 0)
    hourright.t.goto(-700, 0)
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

    def Hour(self):
        print(self.clk.hour24())
        self.hourleft.Szamokxdd(self.clk.leftNumber(self.clk.hour24()))
        self.hourright.Szamokxdd(self.clk.rightNumber(self.clk.hour24()))




    def __init__(self):
        self.screen.bgcolor("black")
        self.clk.setOnSecondChangeListener(self.Second)
        self.clk.setOnMinuteChangeListener(self.Minute)
        self.clk.setOnHourChangeListener(self.Hour())





        self.screen.mainloop()

main()