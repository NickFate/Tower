
import pygame as pp

from classes.player import Player
from classes.border import Border
from classes.empy import Empy

FPS = 60



pp.init()

game = True

screen = pp.display.set_mode((800, 800)) # 25 x 25 map
clock = pp.time.Clock()

player = Player()

border = Border(500)
border1 = Border(300)
empy = Empy()
while game:

    screen.fill((255, 255, 255))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    screen.blit(player.attack_img, (player.attack_rect.x, player.attack_rect.y))
    screen.blit(empy.image, (empy.rect.x, empy.rect.y))
    screen.blit(border.image, (border.rect.x, border.rect.y))
    screen.blit(border1.image, (border1.rect.x, border1.rect.y))
    player.update([border, border1, empy])

    for e in pp.event.get():

        if e.type == pp.QUIT:
            game = False

    pp.display.flip()
    clock.tick(FPS)


pp.quit()
