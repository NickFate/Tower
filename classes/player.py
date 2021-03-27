
import pygame as pp


MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.35

class Player(pp.sprite.Sprite):
    def __init__(self):
        pp.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.image = pp.Surface((64, 96))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        # self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным


    def update(self, left, right, up, platforms):
        key = pp.key.get_pressed()


        if key[pp.K_w]:
            self.yvel = -JUMP_POWER
        elif key[pp.K_s]:
            self.yvel = JUMP_POWER
        else:
            self.yvel = 0


        if key[pp.K_a]:
            self.xvel = -MOVE_SPEED # Лево = x- n
        elif key[pp.K_d]:
            self.xvel = MOVE_SPEED # Право = x + n
        else:
            self.xvel = 0


        self.rect.y += self.yvel # переносим свои положение на xvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pp.sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз       # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает
