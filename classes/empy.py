import pygame as pp

class Empy(pp.sprite.Sprite):

    def __init__(self):
        pp.sprite.Sprite.__init__(self)

        self.image = pp.Surface((64, 96))
        # self.image.set_colorkey()
        self.rect = self.image.get_rect()
