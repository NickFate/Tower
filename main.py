
import pygame as pp

from classes.player import Player
from classes.empy import Empy


FPS = 60



pp.init()

game = True

screen = pp.display.set_mode((800, 800)) # 25 x 25 map
clock = pp.time.Clock()

player = Player()

empy = Empy()

while game:

    screen.fill((255, 255, 255))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    screen.blit(empy.image, (empy.rect.x, empy.rect.y))
    player.update(1, 1, 0, [empy])

    for e in pp.event.get():

        if e.type == pp.QUIT:
            game = False

    pp.display.flip()
    clock.tick(FPS)


pp.quit()
