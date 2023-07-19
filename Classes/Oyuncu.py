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

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self, oyuncu_mermi_grup):
        super().__init__()
        self.image = pygame.image.load("icons/uzay_gemi.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.top = 850
        self.hiz = 10
        self.oyuncu_mermi_grup = oyuncu_mermi_grup
        self.health = 3
        self.mermi_sayisi = 0  # Mermi sayısı değişkeni

    def update(self):
        tus = pygame.key.get_pressed()
        if tus[pygame.K_UP] and self.rect.top > 660 and tus[pygame.K_RIGHT] and self.rect.right < 1280:
            self.rect.x += self.hiz
            self.rect.y -= self.hiz
        elif tus[pygame.K_UP] and self.rect.top > 660 and tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.y -= self.hiz
            self.rect.x -= self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom < 960 and tus[pygame.K_RIGHT] and self.rect.right < 1280:
            self.rect.y += self.hiz
            self.rect.x += self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom < 960 and tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.y += self.hiz
            self.rect.x -= self.hiz
        if tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        elif tus[pygame.K_RIGHT] and self.rect.right < 1280:
            self.rect.x += self.hiz
        elif tus[pygame.K_UP] and self.rect.top > 660:
            self.rect.y -= self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom < 960:
            self.rect.y += self.hiz

    def atesle(self):
        if len(self.oyuncu_mermi_grup) < 5:
            Mermi(self.rect.centerx, self.rect.top, self.oyuncu_mermi_grup)
            self.mermi_sayisi += 1  # Her ateş ettiğinde mermi sayısını bir artır

    def draw(self, window):
        window.blit(self.image, self.rect)

    def kill(self):
        self.oyuncu_mermi_grup.empty()
        super().kill()







