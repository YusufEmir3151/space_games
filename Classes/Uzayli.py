import Methods
import pygame
from Classes import Mermi, UzayliMermi
import random

pygame.init()

WIDTH = Methods.WIDTH
HEIGHT = Methods.HEIGHT

window = Methods.window

FPS = Methods.FPS
saat = Methods.saat
Mermi = Mermi.Mermi

class Uzayli(pygame.sprite.Sprite):
    def __init__(self, oyuncu, uzayli_mermi_grup):
        super().__init__()
        self.image = pygame.image.load("icons/alien.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50, WIDTH - 50)
        self.rect.centery = random.randint(50, HEIGHT // 2)
        self.hiz = random.randint(1, 3)
        self.oyuncu = oyuncu
        self.uzayli_mermi_grup = uzayli_mermi_grup
        self.yon = 1

    def update(self):
        self.rect.x += self.hiz * self.yon

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.yon *= -1

        self.ates_et()

    def ates_et(self):
        if random.randint(1, 100) == 1:
            for _ in range(10):  # 10 adet mermi ekleyelim
                mermi = UzayliMermi.UzayliMermi(self.rect.centerx, self.rect.bottom, self.uzayli_mermi_grup)
                self.uzayli_mermi_grup.add(mermi)

    def draw(self, window):
        window.blit(self.image, self.rect)