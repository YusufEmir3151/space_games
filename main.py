import pygame
import Methods
from Classes import Oyuncu, Mermi, Uzayli

pygame.init()

WIDTH = Methods.WIDTH
HEIGHT = Methods.HEIGHT

window = Methods.window

FPS = Methods.FPS
saat = Methods.saat
Mermi = Mermi.Mermi
Oyuncu = Oyuncu.Oyuncu
Uzayli = Uzayli.Uzayli

class Oyun():
    def __init__(self):
        self.oyuncu_mermi_grup = pygame.sprite.Group()
        self.uzayli_mermi_grup = pygame.sprite.Group()
        self.oyuncu = Oyuncu(self.oyuncu_mermi_grup)
        self.uzayli_grup = pygame.sprite.Group()

        for _ in range(10):
            uzayli = Uzayli(self.oyuncu, self.uzayli_mermi_grup)
            self.uzayli_grup.add(uzayli)

    def baslat(self):
        self.skor = 0
        self.game_over = False

        # Giriş ekranı
        self.giris_ekrani()

        while not self.game_over:
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.QUIT:
                    self.game_over = True
                if etkinlik.type == pygame.KEYDOWN:
                    if etkinlik.key == pygame.K_SPACE:
                        self.oyuncu.atesle()

            self.oyuncu_mermi_grup.update()
            self.uzayli_mermi_grup.update()
            self.oyuncu.update()
            self.uzayli_grup.update()

            if pygame.sprite.spritecollide(self.oyuncu, self.uzayli_mermi_grup, True):
                self.oyuncu.health -= 1
                if self.oyuncu.health == 0:
                    self.game_over = True

            carpisan_mermi = pygame.sprite.groupcollide(self.uzayli_grup, self.oyuncu_mermi_grup, True, True)
            self.skor += len(carpisan_mermi)

            if len(self.uzayli_grup) == 0:  # Tüm uzaylılar öldüğünde
                for _ in range(10):  # Yeni uzaylılar oluştur
                    uzayli = Uzayli(self.oyuncu, self.uzayli_mermi_grup)
                    self.uzayli_grup.add(uzayli)

                # Uzaylıların ateş etme sayısını 2 katına çıkar
                for uzayli in self.uzayli_grup:
                    uzayli.ates_et()

            window.fill((0, 0, 0))

            self.oyuncu_mermi_grup.draw(window)
            self.uzayli_mermi_grup.draw(window)
            self.oyuncu.draw(window)
            self.uzayli_grup.draw(window)

            # Mermi sayısını ekrana yazdır
            font = pygame.font.Font(None, 24)
            mermi_sayisi_text = font.render("Mermi Sayısı: " + str(self.oyuncu.mermi_sayisi), True, (255, 255, 255))
            window.blit(mermi_sayisi_text, (10, 10))
            can = font.render("Can : " + str(self.oyuncu.health), True, (255, 255, 255))
            can_loc = can.get_rect()
            can_loc.topright = (1270, 0)
            window.blit(can, can_loc)

            pygame.display.update()
            saat.tick(FPS)
        if self.oyuncu.mermi_sayisi == 0:
            self.oyuncu.mermi_sayisi = 1
        kd = self.skor / self.oyuncu.mermi_sayisi
        font = pygame.font.Font(None, 36)
        skor_text = font.render("Skor: " + str(round(self.skor, 2)) + "  kd: " + str(kd), True, (255, 255, 255))
        text_rect = skor_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(skor_text, text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        return

    def giris_ekrani(self):
        giris = True

        while giris:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        giris = False

            window.fill((0, 0, 0))
            font = pygame.font.Font(None, 72)
            baslik = font.render("Space-X", True, (255, 255, 255))
            text_rect = baslik.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            window.blit(baslik, text_rect)

            pygame.display.update()
            saat.tick(FPS)


oyun = Oyun()
oyun.baslat()
