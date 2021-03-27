
import pygame as pp

class Player(pp.sprite.Sprite):

    def __init__(self):
        pp.sprite.Sprite.__init__(self)

        self.image = pp.Surface((64, 96))
        # self.image.set_colorkey()
        self.rect = self.image.get_rect()

        self.x_dir = 0
        self.y_dir = 0
        self.speed = 1

    def update(self):
        keys = pp.key.get_pressed()

        if keys[pp.K_a]:
            self.x_dir = -1
        elif keys[pp.K_d]:
            self.x_dir = 1
        else:
            self.x_dir = 0

        if keys[pp.K_w]:
            self.y_dir = -1
        elif keys[pp.K_s]:
            self.y_dir = 1
        else:
            self.y_dir = 0



        self.rect = self.rect.move(self.speed * self.x_dir, self.speed * self.y_dir)
