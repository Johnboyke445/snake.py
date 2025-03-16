import pygame

pygame.init()

ecran = pygame.display.set_mode([800, 600])

continuer = True 
while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer  = False

    ecran.fill((255, 255, 255))

    pygame.draw.circle(ecran, (255, 0, 0), (200, 200), 100)

    pygame.draw.rect(ecran, (0, 0, 255), (400, 300, 100, 100))

    pygame.display.flip()

pygame.quit() 