import pygame as pp

class Empy(pp.sprite.Sprite):

    def __init__(self):
        pp.sprite.Sprite.__init__(self)

        self.hp = 20

        self.image = pp.Surface((64, 96))
        self.image.fill((255, 0, 255))
        # self.image.set_colorkey()
        self.rect = self.image.get_rect()

        self.rect.x = 400
        self.rect.y = 500 - 96

    def update(self):
        if self.hp <= 0:
            print(444)
            self.kill()
