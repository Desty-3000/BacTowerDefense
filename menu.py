"""
Le module menu à pour fonction première de régir les différents menus et les interactions que l'utilisateur peux avoir avec ces derniers

"""

import pygame
import Mapping

class text:
    def __init__(self,width,text,color1,color2,x,y):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.center = (x,y)



IsMainMenuOpen = True
IsOptionMenuOpen = False
IsMappingMenuOpen = False
IsAttackMenuOpen = False
IsPauseMenuOpen = False


def DrawMainMenu(window,MenuStatut,OptionMenuStatut,Event,Jeu,X,Y,M):
    if MenuStatut:

        bouton1 = text(50,"Jouer",(255,255,255),(176,224,230),X/2,5/9*Y)
        bouton2 = text(50,"Options",(255,255,255),(176,224,230),X/2,6/9*Y)
        bouton3 = text(50,"Quitter",(255,255,255),(176,224,230),X/2,7/9*Y)
        window.blit(bouton1.playBtn, bouton1.playRect)
        window.blit(bouton2.playBtn, bouton2.playRect)
        window.blit(bouton3.playBtn, bouton3.playRect)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton1.playRect.collidepoint(pygame.mouse.get_pos()):
                    return True,MenuStatut,OptionMenuStatut,True
                if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                    return True,False,True,False
                if bouton3.playRect.collidepoint(pygame.mouse.get_pos()):
                    return False,False,False,False
    if Jeu != False:
        return True,MenuStatut,OptionMenuStatut,M


def DrawOptionMenu(window,MainMenuState,MenuStatut,Event,X,Y):
    if MenuStatut:
        bouton = text(50,"Retour",(255,255,255),(176,224,230),X/2,7/9*Y)
        window.blit(bouton.playBtn, bouton.playRect)
        for event in Event:
            if event.type == 5 and event.button == 1:
                if bouton.playRect.collidepoint(pygame.mouse.get_pos()):
                    return False,True
    return MenuStatut,MainMenuState

def DrawMappingMenu(window,Mapping_Phase):
    if Mapping_Phase:
        bouton = text(20,"Rajouter une colonne à droite",(255,255,255),(120,120,120),150,20)
        bouton2 = text(20,"Rajouter une ligne en bas",(255,255,255),(120,120,120),130,70)
        bouton3 = text(20,"Retirer une colonne à droite",(255,255,255),(120,120,120),150,120)
        bouton4 = text(20,"Retirer une ligne en bas",(255,255,255),(120,120,120),130,170)

        window.blit(bouton2.playBtn,bouton2.playRect)
        window.blit(bouton.playBtn,bouton.playRect)
        window.blit(bouton3.playBtn,bouton3.playRect)
        window.blit(bouton4.playBtn,bouton4.playRect)

        for event in Event:
            if event.type == 5 and event.button = 1:
                if bouton.playRect.collidepoint(pygame.mouse.get_pos()):
