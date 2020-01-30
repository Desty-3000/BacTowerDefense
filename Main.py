import Mapping
import pygame

pygame.init()

score = 0
niveau = 0

X = 800
Y = 600

XMINGRID = 100
YMINGRID = 100

XMAXGRID = 1000
YMAXGRID = 1000


fenetre = pygame.display.set_mode((X, Y))


Jeu = True

while Jeu :

    Mapping.Refresh_Difficulty_Bar(Mapping.Curr_Difficulte,Mapping.Seuil_Difficulte,fenetre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Jeu = False

    pygame.display.update()

pygame.display.quit()
pygame.quit()