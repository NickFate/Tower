
import pygame as pp

class Border(pp.sprite.Sprite):

    def __init__(self, y):
        pp.sprite.Sprite.__init__(self)

        self.image = pp.Surface((1024, 32))
        # self.image.set_colorkey()
        self.rect = self.image.get_rect()

        self.rect.x = 20
        self.rect.y = y
