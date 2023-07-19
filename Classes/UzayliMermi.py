import Methods
import pygame
from Classes import Mermi

pygame.init()

WIDTH = Methods.WIDTH
HEIGHT = Methods.HEIGHT

window = Methods.window

FPS = Methods.FPS
saat = Methods.saat
Mermi = Mermi.Mermi

class UzayliMermi(pygame.sprite.Sprite):
    def __init__(self, x, y, uzayli_mermi_grup):
        super().__init__()
        self.image = pygame.image.load("icons/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.hiz = 6
        uzayli_mermi_grup.add(self)

    def update(self):
        self.rect.y += self.hiz
        if self.rect.top > HEIGHT:
            self.kill()