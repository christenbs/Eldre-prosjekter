import pygame as pg

class Sikte:
    def __init__(self, musX, musY):
        self._xPos = musX
        self._yPos = musY

    def opprett(self, vindu):
        pg.draw.circle(vindu, (255,0,0), (self._xPos,self._yPos), 30)
        pg.draw.circle(vindu, (152,251,152), (self._xPos,self._yPos), 28)
        pg.draw.rect(vindu,(255,0,0), (self._xPos-1,self._yPos-30,2,60))
        pg.draw.rect(vindu,(255,0,0), (self._xPos-30,self._yPos-1,60,2))
        