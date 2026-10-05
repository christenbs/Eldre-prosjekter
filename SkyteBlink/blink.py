from random import randint
import math
import pygame as pg

class Blink_mal:
    def __init__(self):
        self._xPos = -10
        self._yPos = randint(0,500)
        self._xFart = randint(5,20)/3
        self._yFart = randint(5,20)/3
        self._tilstand = True

    def blir_skutt(self, musX, musY):
        xAvstand = abs(self._xPos) - abs(musX)
        yAvstand = abs(self._yPos) - abs(musY)
        totAvstand = math.sqrt((xAvstand**2)+(yAvstand**2))
        if totAvstand < 20:
            self._tilstand = False
            return True

    def beveg_ned(self):
        self._yPos += self._yFart

    def beveg_hoyre(self):
        self._xPos += self._xFart

    def utenfor(self):
        if self._yPos > 800:
            self._tilstand = False
        elif self._xPos > 1000:
            self._tilstand = False

    def hent_tilstand(self):
        return self._tilstand
    

class Blink(Blink_mal):
    def __init__(self):
        super().__init__()
        self._poeng = 0
        self._farge = 0

    def hent_poeng(self):
        return self._poeng
    
    def sett_farge_og_poeng(self, farge):
        if farge == "blaa":
            self._farge = ((0,0,255))
            self._poeng = 1
        elif farge == "groenn":
            self._farge = ((0,255,0))
            self._poeng = 3
        elif farge == "roed":
            self._farge = ((255,0,0))
            self._poeng = 5
        else:
            self._farge = ((0,0,0))
            self._poeng = -5

    def opprett(self, vindu):
        pg.draw.circle(vindu, self._farge, (self._xPos,self._yPos), 10)

