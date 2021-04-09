from turtle import *
from Szam import Szam
from Clock import Clock
class main:
    screen = Screen()
    clk = Clock(screen)
    def Second(self):
        print(self.clk.sec())



    def __init__(self):
        self.screen.bgcolor("black")
        self.clk.setOnSecondChangeListener(self.Second)
        self.screen.mainloop()

main()