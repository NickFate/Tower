
import pygame as pp

class Map():
    def __init__(self):
        self.image = pp.image.load("res\img\del\del.png")
        self.rect = self.image.get_rect()
        self.rect.center = (450, 450)
        self.mask = pp.mask.from_surface(self.image)
