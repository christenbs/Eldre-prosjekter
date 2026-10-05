from blink import Blink
from sikte import Sikte
from random import randint

import pygame as pg

pg.init()
vindu = pg.display.set_mode((1000,800))
clock = pg.time.Clock()

blinker = []
poeng = 0
font = pg.font.SysFont("Arial", 50)

def bestem_farge():
    n = randint(1,31)
    if n < 21:
        return "blaa"
    elif 20 < n < 29:
        return "groenn"
    elif n == 30:
        return "roed"
    elif n > 30:
        return "svart"

for i in range(10):
    ny_blink = Blink()
    blinker.append(ny_blink)

for blink in blinker:
    farge = bestem_farge()
    blink.sett_farge_og_poeng(farge)

fortsett = True
while fortsett:

    vindu.fill((152,251,152))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    musX, musY = pg.mouse.get_pos()

    sikte = Sikte(musX,musY)
    sikte.opprett(vindu)
    
    for blink in blinker:
        blink.opprett(vindu)
        blink.blir_skutt(musX, musY)
        if blink.blir_skutt(musX,musY) == True:
            poeng += blink.hent_poeng()
        blink.beveg_hoyre()
        blink.beveg_ned()
        blink.utenfor()

        if blink.hent_tilstand() == False:
            blinker.remove(blink)
            ny_blink = Blink()
            farge = bestem_farge()
            ny_blink.sett_farge_og_poeng(farge)
            blinker.append(ny_blink)

    poengsum = font.render(str(poeng), True, (255,255,255))
    vindu.blit(poengsum, (920, 20))


    clock.tick(60)

    pg.display.flip()
pg.quit()