from turtle import *
from Szam import Szam
from Clock import Clock

class main:
    screen = Screen()
    clk = Clock(screen)
    points_keret = Szam()
    secondleft=Szam()
    secondright=Szam()
    minuteleft=Szam()
    minuteright=Szam()
    hourright=Szam()
    hourleft=Szam()


    points_keret.t.goto(-600, -100)
    hourleft.t.goto(-500, -50)
    hourright.t.goto(-300, -50)
    minuteleft.t.goto(0, -50)
    minuteright.t.goto(200, -50)
    secondleft.t.goto(375, 230)
    secondright.t.goto(475, 230)
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
        self.points_keret.pontok_keret()
        self.clk.setOnSecondChangeListener(self.Second)
        self.clk.setOnMinuteChangeListener(self.Minute)
        self.clk.setOnHourChangeListener(self.Hour)


        self.screen.mainloop()

main()