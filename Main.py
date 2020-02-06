﻿import ennemis
import Mapping
import pygame
import menu

pygame.init()

score = 0
niveau = 0
couleurFond = (176,224,230)
X = pygame.display.Info().current_w
Y = pygame.display.Info().current_h

events = pygame.event.get()

XMINGRID = 2/7*X
YMINGRID = 2/7*Y

XMAXGRID = 6/7*X
YMAXGRID = 6/7*Y


fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

ennemis.differents_ennemis()    #j'appelle cette fonction pour avoir les type d'ennemis

Jeu = True

while Jeu :
    events = pygame.event.get()
    menu.IsMappingMenuOpen = Mapping.Mapping_Phase
    fenetre.fill(couleurFond)
    Mapping.DrawMapAndGUI(fenetre,X,Y)
    Mapping.Refresh_Difficulty_Bar(Mapping.Curr_Difficulte,Mapping.Seuil_Difficulte,fenetre,menu.IsMappingMenuOpen,X,Y) #Sert a refresh la barre de difficulté (TEMPORAIREMENT ICI POUR LES TESTS)
    Jeu,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,Mapping.Mapping_Phase = menu.DrawMainMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,Jeu,X,Y,Mapping.Mapping_Phase) #Sert a gérer le menu principal
    menu.IsOptionMenuOpen,menu.IsMainMenuOpen = menu.DrawOptionMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,X,Y) #Sert a gérer le menu des options
    menu.DrawMappingMenu(fenetre,Mapping.Mapping_Phase)
    for event in events:
        if event.type == pygame.QUIT:
            Jeu = False

    pygame.display.update()

pygame.display.quit()
pygame.quit()







