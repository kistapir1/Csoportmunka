from turtle import *
from Szam import Szam
from Clock import Clock
class main:
    screen = Screen()
    clk = Clock(screen)
    secondleft=Szam()
    secondright=Szam()
    def Second(self):
        print(self.clk.sec())
        #self.secondright.two()
        #self.secondleft.five()





    def __init__(self):
        #self.screen.bgcolor("black")
        self.clk.setOnSecondChangeListener(self.Second)
        self.secondright.t.forward(150)
        self.secondright.five()
        self.secondright.five()


        self.screen.mainloop()

main()