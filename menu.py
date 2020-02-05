"""
Le module menu à pour fonction première de régir les différents menus et les interactions que l'utilisateur peux avoir avec ces derniers

"""

import pygame


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


def DrawMainMenu(window,MenuStatut,Event,Jeu,X,Y):
    if MenuStatut:

        bouton1 = text(50,"Jouer",(255,255,255),(0,0,0),X/2,5/9*Y)
        bouton2 = text(50,"Options",(255,255,255),(0,0,0),X/2,6/9*Y)
        bouton3 = text(50,"Quitter",(255,255,255),(0,0,0),X/2,7/9*Y)
        window.blit(bouton1.playBtn, bouton1.playRect)
        window.blit(bouton2.playBtn, bouton2.playRect)
        window.blit(bouton3.playBtn, bouton3.playRect)
        if Event.type == 5 and Event.button == 1:
            if bouton1.playRect.collidepoint(pygame.mouse.get_pos()):
                print("fozin")
            if bouton2.playRect.collidepoint(pygame.mouse.get_pos()):
                return True,False,True
            if bouton3.playRect.collidepoint(pygame.mouse.get_pos()):
                print("WESH NEGRO JE QUITTE")
                return False,False,False
    if Jeu != False:
        return True,MenuStatut,False