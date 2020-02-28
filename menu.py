"""
Le module menu à pour fonction première de régir les différents menus et les interactions que l'utilisateur peux avoir avec ces derniers

"""

import pygame
import Mapping
import math

class text:
    def __init__(self,width,text,color1,color2,x,y,fenetre):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.center = (x,y)
        fenetre.blit(self.playBtn, self.playRect)


IsMainMenuOpen = True
IsOptionMenuOpen = False
IsMappingMenuOpen = False
IsAttackMenuOpen = False
IsPauseMenuOpen = False
IsPlaying = False
IsPainting = False
# 0 = nul , 97 = début chemin , 98 = chemin et 99 = fin chemin
paintPhase = 0

endCoordIndex = [-1,-1]

def DrawMainMenu(window,MenuStatut,OptionMenuStatut,Event,Jeu,X,Y,M,PlayingState):
    if MenuStatut:

        bouton1 = text(50,"Jouer",(255,255,255),(176,224,230),X/2,5/9*Y,window)
        bouton2 = text(50,"Options",(255,255,255),(176,224,230),X/2,6/9*Y,window)
        bouton3 = text(50,"Quitter",(255,255,255),(176,224,230),X/2,7/9*Y,window)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton1.playRect.collidepoint(pygame.mouse.get_pos()):
                    MenuStatut,M,PlayingState = False,True,True
                if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                    MenuStatut,OptionMenuStatut,M,PlayingState = False,True,False,False
                if bouton3.playRect.collidepoint(pygame.mouse.get_pos()):
                    Jeu,MenuStatut,OptionMenuStatut,M = False,False,False,False
    return Jeu,MenuStatut,OptionMenuStatut,M,PlayingState


def DrawOptionMenu(window,MainMenuState,MenuStatut,Event,X,Y):
    if MenuStatut:
        bouton = text(50,"Retour",(255,255,255),(176,224,230),X/2,7/9*Y,window)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton.playRect.collidepoint(pygame.mouse.get_pos()):
                    return False,True
    return MenuStatut,MainMenuState


def PaintMap(state,grid,matrice,paintPhase,X,Event,colonne,window,listerect,isPlaced,ligne,eci):
    if state:
        for event in Event:
            if event.type == 5 and event.button == 1:
                if grid.collidepoint(pygame.mouse.get_pos()):
                    mouseRect = pygame.draw.rect(window,(0,0,0),(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1),-1)
                    test = mouseRect.collidelist(listerect)
                    if paintPhase == 97:
                        if test != -1 and isPlaced != True:
                            print("test = "+str(test))
                            if test<=9:
                                matrice[0][test] = 97
                                isPlaced = True
                            else:
                                matrice[int(str(test)[0])][int(str(test)[1])] = 97
                                isPlaced = True
                    if paintPhase == 99:
                        if test != -1:
                            if test<=9:
                                if eci[1] != -1:
                                    matrice[eci[0]][eci[1]] = 98
                                matrice[0][test] = 99
                                eci[0] = 0
                                eci[1] = test
                            else:
                                if eci[1] != -1:
                                    matrice[eci[0]][eci[1]] = 98
                                matrice[int(str(test)[0])][int(str(test)[1])] = 99
                                eci[0] = int(str(test)[0])
                                eci[1] = int(str(test)[1])
    return matrice,isPlaced,eci

def DrawMappingMenu(window,Mapping_Phase,Event,ligne,colonne,curdif,matrice,grid,IsPainting,paintphase):
    if Mapping_Phase:
        bouton = text(20,"Rajouter une colonne à droite",(255,255,255),(120,120,120),150,20,window)
        bouton2 = text(20,"Rajouter une ligne en bas",(255,255,255),(120,120,120),130,70,window)
        bouton3 = text(20,"Retirer une colonne à droite",(255,255,255),(120,120,120),150,120,window)
        bouton4 = text(20,"Retirer une ligne en bas",(255,255,255),(120,120,120),130,170,window)
        bouton5 = text(20,"Placer le début du chemin",(255,255,255),(120,120,120),140,220,window)
        bouton6 = text(20,"Placer une case chemin",(255,255,255),(120,120,120),130,270,window)
    if not IsPainting:
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton.playRect.collidepoint(pygame.mouse.get_pos()):
                    for i in range(len(matrice)):
                        matrice[i].append(0)
                    colonne += 1
                    curdif -= 1
                if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                    newLine = []
                    for i in range(colonne):
                        newLine.append(0)
                    matrice.append(newLine)
                    ligne += 1
                    curdif -= 1
                if bouton3.playRect.collidepoint(pygame.mouse.get_pos()) and colonne>5:
                    for i in range(len(matrice)):
                        matrice[i].pop()
                    colonne -= 1
                    curdif += 1
                if bouton4.playRect.collidepoint(pygame.mouse.get_pos())and ligne>5:
                    matrice.pop()
                    ligne -= 1
                    curdif += 1
                if bouton5.playRect.collidepoint(pygame.mouse.get_pos()):
                    paintphase = 97
                if bouton6.playRect.collidepoint(pygame.mouse.get_pos()):
                    paintphase = 99
    return colonne,ligne,curdif,matrice,IsPainting,paintphase
