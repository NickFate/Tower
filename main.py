
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

enemy = pp.sprite.Group()
enemy.add(empy)
while game:

    screen.fill((255, 255, 255))
    screen.blit(player.image, (player.rect.x, player.rect.y))
    screen.blit(border.image, (border.rect.x, border.rect.y))
    screen.blit(border1.image, (border1.rect.x, border1.rect.y))
    screen.blit(player.attack_img, (player.attack_rect.x, player.attack_rect.y))

    player.update([[border, border1], enemy], [empy])
    enemy.draw(screen)
    enemy.update()

    for e in pp.event.get():

        if e.type == pp.QUIT or (e.type == pp.KEYDOWN and e.key == pp.K_ESCAPE):
            game = False

    pp.display.flip()
    clock.tick(FPS)


pp.quit()
