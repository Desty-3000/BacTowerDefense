import ennemis
import Mapping
import pygame
import menu

pygame.init()

score = 0
niveau = 0

X = pygame.display.Info().current_w
Y = pygame.display.Info().current_h

Curevent = pygame.event.Event()

XMINGRID = 100
YMINGRID = 100

XMAXGRID = 1000
YMAXGRID = 1000


fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

ennemis.differents_ennemis()    #j'appelle cette fonction pour avoir les type d'ennemis

Jeu = True

while Jeu :
    fenetre.fill((0,0,0))
    Mapping.Refresh_Difficulty_Bar(Mapping.Curr_Difficulte,Mapping.Seuil_Difficulte,fenetre,menu.IsMappingMenuOpen)
    Jeu,menu.IsMainMenuOpen,menu.IsOptionMenuOpen = menu.DrawMainMenu(fenetre,menu.IsMainMenuOpen,Curevent,Jeu,X,Y)
    for event in pygame.event.get():
        print(Curevent)
        if event.type == pygame.QUIT:
            Jeu = False

    pygame.display.update()

pygame.display.quit()
pygame.quit()

