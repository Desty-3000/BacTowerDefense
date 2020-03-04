import ennemis
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

fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

ennemis.differents_ennemis()    #j'appelle cette fonction pour avoir les type d'ennemis

Jeu = True

while Jeu :

    events = pygame.event.get()


    niveau = Mapping.Niveau

    fenetre.fill(couleurFond)
    #drawMap
    Mapping.GRID,Mapping.c,Mapping.d = Mapping.drawMap(Mapping.isMapDisplayed,X,Y,Mapping.nbreColonne,Mapping.nbreLigne,fenetre)
    #DrawMapAndGUI
    Mapping.GRID,Mapping.rectList,Mapping.caseList = Mapping.DrawMapAndGUI(fenetre,menu.IsPlaying,X,Y,0,score,niveau,Mapping.MAP,Mapping.nbreLigne,Mapping.nbreColonne,Mapping.rectList,Mapping.GRID,Mapping.c,Mapping.d,Mapping.caseList)

    Mapping.Refresh_Difficulty_Bar(Mapping.Curr_Difficulte,Mapping.Seuil_Difficulte,fenetre,menu.IsPlaying,X,Y) #Sert a refresh la barre de difficulté (TEMPORAIREMENT ICI POUR LES TESTS)
    #DrawMainMenu
    Jeu,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,Mapping.Mapping_Phase,menu.IsPlaying,menu.MappingPhaseIndex = menu.DrawMainMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,Jeu,X,Y,Mapping.Mapping_Phase,menu.IsPlaying,menu.MappingPhaseIndex) #Sert a gérer le menu principal
    #DrawOptionMenu
    menu.IsOptionMenuOpen,menu.IsMainMenuOpen = menu.DrawOptionMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,X,Y) #Sert a gérer le menu des options
    #DrawMappingMenu
    Mapping.nbreColonne,Mapping.nbreLigne,Mapping.Curr_Difficulte,Mapping.MAP,menu.MappingPhaseIndex = menu.DrawMappingMenu(fenetre,menu.MappingPhaseIndex,events,Mapping.nbreLigne,Mapping.nbreColonne,Mapping.Curr_Difficulte,Mapping.MAP,Mapping.GRID,X,Y)

    for case in Mapping.caseList:
        case.update()

    for event in events:
        if event.type == pygame.QUIT:
            Jeu = False
        if event.type == pygame.KEYDOWN and event.key == 27:
            Jeu = False
    pygame.display.update()

pygame.display.quit()
pygame.quit()







