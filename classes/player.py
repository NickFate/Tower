
import pygame as pp

from func.func import sign

class Player(pp.sprite.Sprite):
    def __init__(self):
        pp.sprite.Sprite.__init__(self)

        self.wight = 64

        self.grav = 0.35
        self.jump = 10
        self.speed = 7
        self.onGround = False

        self.x_dir = 0
        self.y_dir = 0

        self.image = pp.Surface((64, 96))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

        self.pull = 20
        self.pull_time = 180
        self.pull_timer = 0

        self.attack_rect = pp.Surface((64, 96)).get_rect()
        self.attack_rect.x = self.rect.x - self.wight
        self.attack_rect.y = self.rect.y
        self.attack_timer = 0
        self.attack_time = 45

        self.last_sign = 1
        self.attack_img.set_colorkey((0, 0, 0))


        # self.image.set_colorkey(Color(COLOR))




    def update(self, platforms, enemy):

        key = pp.key.get_pressed()

        if key[pp.K_z]:
            if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
                self.y_dir = -self.jump

        if key[pp.K_LEFT]:
            self.x_dir = -self.speed # Лево = x- n

        elif key[pp.K_RIGHT]:
            self.x_dir = self.speed # Право = x + n

        else:
            self.x_dir = 0



        if key[pp.K_LSHIFT]:
            if self.pull_timer >= self.pull_time:
                self.x_dir = self.last_sign * 100
                self.pull_timer = 0
        self.pull_timer += 1


        if not self.onGround:
            self.y_dir += self.grav

        self.onGround = False
        self.rect.y += self.y_dir
        self.collide(0, self.y_dir, platforms)

        self.rect.x += self.x_dir
        self.collide(self.x_dir, 0, platforms)

        self.last_sign = sign(self.x_dir) or self.last_sign
        self.attack_rect.x = self.rect.x + self.wight * self.last_sign
        self.attack_rect.y = self.rect.y

        if key[pp.K_x]:
            if self.attack_timer == 0:
                for i in enemy:
                    if self.attack_rect.colliderect(i.rect):
                        if i.hp:
                            i.hp -= 7
                self.attack_timer += 1
        if self.attack_timer != 0:
            self.attack_timer += 1
            self.attack_img.fill((255, 0, 0))
            print(1)
        else:
            print(2, self.attack_timer)
            self.attack_img.set_colorkey((255, 0, 0))

        if self.attack_timer > self.attack_time:
            self.attack_timer = 0

            # self.attack_img.set_colorkey((0, 0, 0))

            # print(999999999999999999999999)
        # print(self.attack_timer, self.attack_time)



    def collide(self, xvel, yvel, plat):
        for platforms in plat:
            for p in platforms:
                if pp.sprite.collide_rect(self, p):

                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.y_dir = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.y_dir = 0
