import pygame as pg
from random import randrange

# Initialisation de Pygame
pg.init()


# Définition de la taille de la fenêtre et des tuiles
window_size = 700
tile_size = 30
tile_range = (tile_size // 2, window_size - tile_size // 2, tile_size)

# Fonction pour obtenir une position aléatoire dans les limites des tuiles
get_random_position = lambda: [randrange(*tile_range), randrange(*tile_range)]

# Initialisation du serpent
snake = pg.Rect(0, 0, tile_size - 2, tile_size - 2)
snake.center = get_random_position()
length = 1
segments = [snake.copy()]

# Initialisation de la nourriture
food = snake.copy()
food.center = get_random_position()

# Configuration de l'écran
screen = pg.display.set_mode([window_size] * 2)
clock = pg.time.Clock()

# Dictionnaire des directions possibles avec les touches correspondantes
dirs = {pg.K_s: (0, -tile_size), pg.K_w: (0, tile_size), pg.K_a: (-tile_size, 0), pg.K_d: (tile_size, 0)}
snake_dir = (0, 0)  # Initialisation de la direction du serpent

# Ajout d'une variable pour suivre le nombre de carrés rouges mangés (score)
score = 0
# Utilisation de la police par défaut de Pygame
font = pg.font.Font(pg.font.get_default_font(), 36)
# Boucle principale du jeu
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN and event.key in dirs:
            # Vérification pour éviter de revenir sur soi-même
            if dirs[event.key] != (-snake_dir[0], -snake_dir[1]):
                snake_dir = dirs[event.key]

    # Remplissage de l'écran avec une couleur (noir dans ce cas)
    screen.fill((0, 0, 0))

    # Vérification de la collision avec lui-même ou les bords
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if (
        snake.left < 0
        or snake.right > window_size
        or snake.top < 0
        or snake.bottom > window_size
        or self_eating
    ):
        # Réinitialisation de la position du serpent et de la nourriture
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

        # Réinitialisation du score
        score = 0

    # Vérification de la collision avec la nourriture
    if snake.colliderect(food):
        food.center = get_random_position()
        length += 1
        # Incrémentation du score à chaque fois que la nourriture est mangée
        score += 1

    # Dessin de la nourriture en rouge
    pg.draw.rect(screen, (255, 0, 0), food)

    # Déplacement du serpent et mise à jour des segments
    snake.move_ip(snake_dir)
    segments.append(snake.copy())
    segments = segments[-length:]
    
     # Affichage du score en haut à gauche de l'écran
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Dessin des segments du serpent en vert
    for segment in segments:
        pg.draw.rect(screen, (0, 255, 0), segment)

       

    # Mise à jour de l'affichage
    pg.display.flip()

    # Contrôle de la vitesse du serpent en ajustant la valeur du tick
    clock.tick(10)