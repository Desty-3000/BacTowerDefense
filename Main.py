import ennemis
import Mapping
import pygame
import menu
import tower

pygame.init()

class Player:
    niveau = 0
    score = 0
    argent = 800
    difficulte= 20
    difficulteMax= 10

couleurFond = (176,224,230)
X = pygame.display.Info().current_w
Y = pygame.display.Info().current_h

events = pygame.event.get()

fenetre = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

plyManager = Player()

Mapping.MAP = Mapping.InitMap(fenetre,Mapping.MAP)

Jeu = True

while Jeu :
    events = pygame.event.get()
    fenetre.fill(couleurFond)

    #DimissPopup
    menu.activesPop =  menu.DimissPopup(menu.activesPop,events)
    #drawMap
    Mapping.GRID,Mapping.caseWid,Mapping.caseLen = Mapping.drawMap(X,Y,Mapping.nbreColonne,Mapping.nbreLigne,fenetre)
    #DrawGUI
    menu.leftGUI = menu.DrawGUI(fenetre,menu.IsPlaying,X,Y,plyManager.argent,plyManager.score,plyManager.niveau,Mapping.GRID)
    #drawCases
    Mapping.drawCases(Mapping.MAP,Mapping.nbreColonne,Mapping.nbreLigne,Mapping.caseWid,Mapping.caseLen,Mapping.GRID,menu.IsPlaying,Mapping.pathNumber)
    #Refresh Difficulty Bar
    menu.Refresh_Difficulty_Bar(plyManager.difficulte,plyManager.difficulteMax,fenetre,menu.IsPlaying,X,Y) #Sert a refresh la barre de difficulté (TEMPORAIREMENT ICI POUR LES TESTS)
    #DrawMainMenu
    Jeu,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,menu.IsPlaying,menu.MappingPhaseIndex = menu.DrawMainMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,Jeu,X,Y,menu.IsPlaying,menu.MappingPhaseIndex) #Sert a gérer le menu principal
    #DrawOptionMenu
    menu.IsOptionMenuOpen,menu.IsMainMenuOpen = menu.DrawOptionMenu(fenetre,menu.IsMainMenuOpen,menu.IsOptionMenuOpen,events,X,Y)
    #DrawMappingMenu
    Mapping.nbreColonne,Mapping.nbreLigne,plyManager.difficulte,Mapping.MAP,menu.MappingPhaseIndex,menu.activesPop,menu.clic,tower.currentTower,plyManager.argent = menu.DrawMappingMenu(fenetre,menu.MappingPhaseIndex,events,Mapping.nbreLigne,Mapping.nbreColonne,plyManager.difficulte,Mapping.MAP,Mapping.GRID,X,Y,menu.activesPop,Mapping.pathNumber,menu.clic,menu.leftGUI,plyManager.argent,tower.currentTower)
    #TowerPlacement
    tower.TowerPlacement(fenetre,tower.currentTower,Mapping.caseLen,Mapping.caseWid)

    for popup in menu.activesPop:
        popup.Draw(fenetre)
    for tow in tower.listeTower:
        tow.Draw(fenetre)
    for event in events:
        if event.type == pygame.QUIT:
            Jeu = False
        if event.type == pygame.KEYDOWN and event.key == 27:
            Jeu = False
    pygame.display.update()

pygame.display.quit()
pygame.quit()







