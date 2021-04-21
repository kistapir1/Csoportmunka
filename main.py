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
    points = Szam()
    screen._delay(0)

    hourleft.t.goto(-500, 0)
    hourright.t.goto(-300, 0)
    points.t.goto(-100, 0)
    minuteleft.t.goto(0, 0)
    minuteright.t.goto(200, 0)
    secondleft.t.goto(375, 280)
    secondright.t.goto(475, 280)
    def Second(self):
        print(self.clk.sec())
        self.secondleft.Szamokmini(self.clk.leftNumber(self.clk.sec()))
        self.secondright.Szamokmini(self.clk.rightNumber(self.clk.sec()))

    def Minute(self):
        print(self.clk.min())
        self.minuteleft.Szamok(self.clk.leftNumber(self.clk.min()))
        self.minuteright.Szamok(self.clk.rightNumber(self.clk.min()))

    def Hour(self):
        print(self.clk.hour24())
        self.hourleft.Szamok(self.clk.leftNumber(self.clk.hour24()))
        self.hourright.Szamok(self.clk.rightNumber(self.clk.hour24()))




    def __init__(self):
        self.screen.bgcolor("black")
        self.clk.setOnSecondChangeListener(self.Second)
        self.clk.setOnMinuteChangeListener(self.Minute)
        self.clk.setOnHourChangeListener(self.Hour)
        self.points.pontok()


        self.screen.mainloop()

main()