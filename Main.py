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

Mapping.MAP = Mapping.InitMap(fenetre,Mapping.MAP)

Jeu = True

while Jeu :
    events = pygame.event.get()
    print(Mapping.pathNumber)
    niveau = Mapping.Niveau

    fenetre.fill(couleurFond)
    #drawMap
    Mapping.GRID,Mapping.caseWid,Mapping.caseLen = Mapping.drawMap(X,Y,Mapping.nbreColonne,Mapping.nbreLigne,fenetre)
    #DrawMapAndGUI
    Mapping.DrawGUI(fenetre,menu.IsPlaying,X,Y,0,score,niveau,Mapping.GRID)
    #drawCases
    Mapping.drawCases(Mapping.MAP,Mapping.nbreColonne,Mapping.nbreLigne,Mapping.caseWid,Mapping.caseLen,Mapping.GRID,menu.IsPlaying,Mapping.pathNumber)
    #Refresh Difficulty Bar
    Mapping.Refresh_Difficulty_Bar(Mapping.Curr_Difficulte,Mapping.Seuil_Difficulte,fenetre,menu.IsPlaying,X,Y) #Sert a refresh la barre de difficulté (TEMPORAIREMENT ICI POUR LES TESTS)
    #DrawMainMenu
    Jeu,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,menu.IsPlaying,menu.MappingPhaseIndex = menu.DrawMainMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,Jeu,X,Y,menu.IsPlaying,menu.MappingPhaseIndex) #Sert a gérer le menu principal
    #DrawOptionMenu
    menu.IsOptionMenuOpen,menu.IsMainMenuOpen = menu.DrawOptionMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,X,Y) #Sert a gérer le menu des options
    #DrawMappingMenu
    Mapping.nbreColonne,Mapping.nbreLigne,Mapping.Curr_Difficulte,Mapping.MAP,menu.MappingPhaseIndex = menu.DrawMappingMenu(fenetre,menu.MappingPhaseIndex,events,Mapping.nbreLigne,Mapping.nbreColonne,Mapping.Curr_Difficulte,Mapping.MAP,Mapping.GRID,X,Y)


    for event in events:
        if event.type == pygame.QUIT:
            Jeu = False
        if event.type == pygame.KEYDOWN and event.key == 27:
            Jeu = False
    pygame.display.update()

pygame.display.quit()
pygame.quit()







