"""
Le module menu à pour fonction première de régir les différents menus et les interactions que l'utilisateur peux avoir avec ces derniers

"""

import pygame
import Mapping
import math

#Classe pour simplifier l'écriture sur l'écran
class text:
    def __init__(self,width,text,color1,color2,x,y,fenetre):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.center = (x,y)
        fenetre.blit(self.playBtn, self.playRect)

#Les noms parlent d'eux même ...
IsMainMenuOpen = True
IsOptionMenuOpen = False
IsPauseMenuOpen = False

#Si l'écran affiche le jeu ou les menus
IsPlaying = False

#Onglet actuel du menu à gauche en jeu
MappingPhaseIndex = 0




#Affiche le menu principal
def DrawMainMenu(window,MenuStatut,OptionMenuStatut,Event,Jeu,X,Y,PlayingState,index):
    if MenuStatut:

        bouton1 = text(50,"Jouer",(255,255,255),(176,224,230),X/2,5/9*Y,window)
        bouton2 = text(50,"Options",(255,255,255),(176,224,230),X/2,6/9*Y,window)
        bouton3 = text(50,"Quitter",(255,255,255),(176,224,230),X/2,7/9*Y,window)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton1.playRect.collidepoint(pygame.mouse.get_pos()):
                    MenuStatut,PlayingState = False,True
                    index += 1
                if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                    MenuStatut,OptionMenuStatut,PlayingState = False,True,False
                if bouton3.playRect.collidepoint(pygame.mouse.get_pos()):
                    Jeu,MenuStatut,OptionMenuStatut = False,False,False
    return Jeu,MenuStatut,OptionMenuStatut,PlayingState,index

#Affiche le menu des options
def DrawOptionMenu(window,MainMenuState,MenuStatut,Event,X,Y):
    if MenuStatut:
        bouton = text(50,"Retour",(255,255,255),(176,224,230),X/2,7/9*Y,window)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton.playRect.collidepoint(pygame.mouse.get_pos()):
                    return False,True
    return MenuStatut,MainMenuState



#Affiche les onglets à gauche en jeu
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
                        colonne,matrice,curdif = Mapping.AddColonne(colonne,matrice,curdif,window)
                    if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                        ligne,matrice,curdif = Mapping.AddLigne(ligne,colonne,matrice,Mapping.caseLen,Mapping.caseWid,curdif,window)
                    if bouton3.playRect.collidepoint(pygame.mouse.get_pos()) and colonne>5:
                        colonne,matrice,curdif = Mapping.RemoveColonne(colonne,matrice,curdif)
                    if bouton4.playRect.collidepoint(pygame.mouse.get_pos())and ligne>5:
                        ligne,matrice,curdif = Mapping.RemoveLigne(ligne,matrice,curdif)
                    if bouton7.playRect.collidepoint(pygame.mouse.get_pos()):
                        index += 1
        if index == 2:
            textbuild = text(20,"Dessine le chemin",(255,255,255),(120,120,120),150,20,window)
            textbuild2 = text(20,"Sur le plateau",(255,255,255),(120,120,120),150,70,window)
            for event in Event:
                Mapping.pathNumber = Mapping.setPath(event,matrice,colonne,ligne,Mapping.pathNumber)

    return colonne,ligne,curdif,matrice,index
