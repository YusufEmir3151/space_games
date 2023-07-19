import Methods
import pygame

pygame.init()

WIDTH = Methods.WIDTH
HEIGHT = Methods.HEIGHT

window = Methods.window

FPS = Methods.FPS
saat = Methods.saat

class Mermi(pygame.sprite.Sprite):
    def __init__(self, x, y, oyuncu_mermi_grup):
        super().__init__()
        self.image = pygame.image.load("icons/bullet_2.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.hiz = 12
        oyuncu_mermi_grup.add(self)

    def update(self):
        self.rect.y -= self.hiz
        if self.rect.bottom < 0:
            self.kill()

