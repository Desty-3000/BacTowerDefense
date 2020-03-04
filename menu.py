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
IsPauseMenuOpen = False
IsPlaying = False
MappingPhaseIndex = 0





def DrawMainMenu(window,MenuStatut,OptionMenuStatut,Event,Jeu,X,Y,M,PlayingState,index):
    if MenuStatut:

        bouton1 = text(50,"Jouer",(255,255,255),(176,224,230),X/2,5/9*Y,window)
        bouton2 = text(50,"Options",(255,255,255),(176,224,230),X/2,6/9*Y,window)
        bouton3 = text(50,"Quitter",(255,255,255),(176,224,230),X/2,7/9*Y,window)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton1.playRect.collidepoint(pygame.mouse.get_pos()):
                    MenuStatut,M,PlayingState = False,True,True
                    index += 1
                if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                    MenuStatut,OptionMenuStatut,M,PlayingState = False,True,False,False
                if bouton3.playRect.collidepoint(pygame.mouse.get_pos()):
                    Jeu,MenuStatut,OptionMenuStatut,M = False,False,False,False
    return Jeu,MenuStatut,OptionMenuStatut,M,PlayingState,index


def DrawOptionMenu(window,MainMenuState,MenuStatut,Event,X,Y):
    if MenuStatut:
        bouton = text(50,"Retour",(255,255,255),(176,224,230),X/2,7/9*Y,window)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton.playRect.collidepoint(pygame.mouse.get_pos()):
                    return False,True
    return MenuStatut,MainMenuState




def DrawMappingMenu(window,index,Event,ligne,colonne,curdif,matrice,grid,X,Y):
    if index != 0:
        bouton7 = text(20,"Suivant",(255,255,255),(120,120,120),1/20*X,14/15*Y,window)
        if index == 1:
            bouton = text(20,"Rajouter une colonne à droite",(255,255,255),(120,120,120),1/13*X,5/20*Y,window)
            bouton2 = text(20,"Rajouter une ligne en bas",(255,255,255),(120,120,120),1/13*X,6/20*Y,window)
            bouton3 = text(20,"Retirer une colonne à droite",(255,255,255),(120,120,120),1/13*X,7/20*Y,window)
            bouton4 = text(20,"Retirer une ligne en bas",(255,255,255),(120,120,120),1/13*X,8/20*Y,window)

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
                    if bouton7.playRect.collidepoint(pygame.mouse.get_pos()):
                        index += 1
        if index == 2:
            textbuild = text(20,"Dessine le chemin",(255,255,255),(120,120,120),150,20,window)
            textbuild2 = text(20,"Sur le plateau",(255,255,255),(120,120,120),150,70,window)

    return colonne,ligne,curdif,matrice,index
