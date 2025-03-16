import pygame
import random

from pygame.locals import *

largeur_ecran = 800
hauteur_ecran = 600

class Vaisseau(pygame.sprite.Sprite):
    def __init__(self):
        super(Vaisseau, self).__init__()
        self.surf = pygame.image.load("vaisseau.jpg").convert()
        self.surf.set_colorkey((255, 255, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            if len(le_missile.sprites()) < 1:
                missile = Missile(self.rect.center)
                tous_sprites.add(missile)
                le_missile.add(missile)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largeur_ecran:
            self.rect.right = largeur_ecran
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > hauteur_ecran:
            self.rect.bottom = hauteur_ecran

class Missile(pygame.sprite.Sprite):
    def __init__(self, center_missile):
        super(Missile, self).__init__()
        self.surf = pygame.Surface((10, 5))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=center_missile)

    def update(self):
        self.rect.move_ip(15, 0)
        if self.rect.left > largeur_ecran:
            self.kill()

class Ennemi(pygame.sprite.Sprite):  # Correction : Utilisation du nom correct de la classe
    def __init__(self):
        super(Ennemi, self).__init__()  # Correction : Utilisation correcte de super()
        self.surf = pygame.image.load("meteorite.jpg").convert()
        self.surf.set_colorkey((255, 255, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                largeur_ecran + 50,
                random.randint(0, hauteur_ecran)  # Correction : Utilisation correcte du nom de la variable
            )
        )

        self.speed = random.randint(5, 20)  # Correction : Correction du nom de la méthode randint

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Initialiser Pygame
pygame.init()

pygame.display.set_caption("the shoot en up 1.0")

AJOUT_ENNEMI = pygame.USEREVENT + 1  # Correction : Utilisation du nom correct de l'événement
pygame.time.set_timer(AJOUT_ENNEMI, 500)

ecran = pygame.display.set_mode([largeur_ecran, hauteur_ecran])

clock = pygame.time.Clock()

tous_sprites = pygame.sprite.Group()
le_missile = pygame.sprite.Group()
les_ennemis = pygame.sprite.Group()  # Correction : Utilisation du nom correct du groupe d'ennemis

vaisseau = Vaisseau()
tous_sprites.add(vaisseau)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == AJOUT_ENNEMI:  # Correction : Utilisation du nom correct de l'événement
            nouvel_ennemi = Ennemi()  # Correction : Utilisation du nom correct de la classe
            les_ennemis.add(nouvel_ennemi)
            tous_sprites.add(nouvel_ennemi)
    
    ecran.fill((0, 0, 0))

    touche_appuyee = pygame.key.get_pressed()

    vaisseau.update(touche_appuyee)
    le_missile.update()
    les_ennemis.update()  # Correction : Utilisation du nom correct de la méthode update pour les ennemis

    for mon_sprite in tous_sprites:
        ecran.blit(mon_sprite.surf, mon_sprite.rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()