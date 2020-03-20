"""
Le module menu à pour fonction première de régir les différents menus et les interactions que l'utilisateur peux avoir avec ces derniers

"""

import pygame
import Mapping
import math
import tower

#Classe pour simplifier l'écriture sur l'écran
class text:
    def __init__(self,width,text,color1,color2,x,y,fenetre):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.center = (x,y)
        fenetre.blit(self.playBtn, self.playRect)
#Classe pour créer des instances de messages en popup
class popup:

    def __init__(self,x,y,length,width,color,ligne1,ligne2,ligne3):
        self.x,self.y,self.length,self.width,self.color=x,y,length,width,color
        self.ligne1,self.ligne2,self.ligne3=ligne1,ligne2,ligne3
    def Draw(self,fenetre):
        pygame.draw.rect(fenetre,(80,80,80),(self.x-5,self.y-5,self.length+10,self.width+10))
        self.fen = pygame.draw.rect(fenetre,self.color,(self.x,self.y,self.length,self.width))
        bouton = text(20,"Clique sur l'écran pour fermer",(255,255,255),pygame.Color(120,120,120,0),self.fen.centerx,self.fen.bottom-(1/20*self.fen.bottom),fenetre)
        text1 = text(20,self.ligne1,(255,255,255),pygame.Color(120,120,120,0),self.fen.centerx,self.fen.centery-(1/20*self.fen.bottom),fenetre)
        text2 = text(20,self.ligne2,(255,255,255),pygame.Color(120,120,120,0),self.fen.centerx,self.fen.centery,fenetre)
        text3 = text(20,self.ligne3,(255,255,255),pygame.Color(120,120,120,0),self.fen.centerx,self.fen.centery+(1/20*self.fen.bottom),fenetre)


class btnTourelle:
    def __init__(self,nom,degats,vitesseA,element,distance,prix,tourelle1Rect,window):
         tourelle1Name = text(20,nom,(10,10,10),(150,150,150),tourelle1Rect.centerx+int(tourelle1Rect.width*1/4),tourelle1Rect.y+(1/7*tourelle1Rect.height),window)
         tourelle1Degats = text(15,"Degats : "+str(degats),(10,10,10),(150,150,150),tourelle1Rect.centerx+int(tourelle1Rect.width*1/4),tourelle1Rect.y+(2/7*tourelle1Rect.height),window)
         tourelle1vitesseA = text(15,"Cadence : "+str(vitesseA)+"tir/s",(10,10,10),(150,150,150),tourelle1Rect.centerx+int(tourelle1Rect.width*1/4),tourelle1Rect.y+(3/7*tourelle1Rect.height),window)
         tourelle1type = text(15,"Type : "+element,(10,10,10),(150,150,150),tourelle1Rect.centerx+int(tourelle1Rect.width*1/4),tourelle1Rect.y+(4/7*tourelle1Rect.height),window)
         tourelle1Distance = text(15,"Portée : "+str(distance)+" cases",(10,10,10),(150,150,150),tourelle1Rect.centerx+int(tourelle1Rect.width*1/4),tourelle1Rect.y+(5/7*tourelle1Rect.height),window)
         tourelle1Prix = text(15,"Prix : "+str(prix)+" $",(10,10,10),(150,150,150),tourelle1Rect.centerx+int(tourelle1Rect.width*1/4),tourelle1Rect.y+(6/7*tourelle1Rect.height),window)


#Les noms parlent d'eux même ...
IsMainMenuOpen = True
IsOptionMenuOpen = False
IsPauseMenuOpen = False

#Si l'écran affiche le jeu ou les menus
IsPlaying = False

#Onglet actuel du menu à gauche en jeu
MappingPhaseIndex = 0

#Liste des popup actifs
activesPop= []

#Menu des tourelles a gauche
leftGUI = pygame.Rect(0,0,0,0)

#Intermediaire pour les popups
clic = 0



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
def DrawMappingMenu(window,index,Event,ligne,colonne,curdif,matrice,grid,X,Y,pop,pathN,clic,gui,money,currentTower):
    if index != 0:
        if index !=3:
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
                        popp = popup(1/4*X,1/4*Y,1/2*X,1/2*Y,(120,120,120),"Etape 2 : Dessiner le chemin des ennemis","Clique gauche sur une case pour l'ajouter au chemin","Clique droit sur une case pour la retirer du chemin")
                        pop.append(popp)
        if index == 2:
            textbuild = text(20,"Dessine le chemin",(255,255,255),(120,120,120),1/13*X,8/20*Y,window)
            textbuild2 = text(20,"Sur le plateau",(255,255,255),(120,120,120),1/13*X,9/20*Y,window)
            for event in Event:
                if clic == 2:
                    Mapping.pathNumber = Mapping.setPath(event,matrice,colonne,ligne,Mapping.pathNumber)
                if event.type == 5 and event.button == 1:
                    if clic <2:
                        clic +=1
                    if bouton7.playRect.collidepoint(pygame.mouse.get_pos()) and pathN >1:

                        popp = popup(1/4*X,1/4*Y,1/2*X,1/2*Y,(120,120,120),"Etape 3 : Préparation de l'équipement","Achète des tourelles avec le menu défilant","Clique droit pour annuler la selection")
                        pop.append(popp)
                        index +=1
        if index == 3:
            next = text(20,"Lancer",(255,255,255),(120,120,120),gui.centerx,14/15*Y,window)

            arrowupRectB = pygame.draw.rect(window,(0,0,0),(leftGUI.x,leftGUI.y,1/6*X,1/8*Y),2)
            arrowupRect = pygame.draw.rect(window,(150,150,150),(leftGUI.x,leftGUI.y,1/6*X,1/8*Y))
            flecheHaut = pygame.image.load('flecheHautClean.png')
            flecheHaut = pygame.transform.scale(flecheHaut, (int(arrowupRect.width/2), int(arrowupRect.height/2)))
            positionFlecheHaut = flecheHaut.get_rect()
            positionFlecheHaut.center = (arrowupRect.centerx,arrowupRect.centery)
            window.blit(flecheHaut, positionFlecheHaut)

            tourelle1RectB = pygame.draw.rect(window,(0,0,0),(leftGUI.x,leftGUI.y+1/8*Y+2,1/6*X,1/5*Y),2)
            tourelle1Rect = pygame.draw.rect(window,(150,150,150),(leftGUI.x,leftGUI.y+1/8*Y+2,1/6*X,1/5*Y))
            tourelle1Disp = pygame.draw.rect(window,(255,255,255),(tourelle1Rect.x+(1/20*tourelle1Rect.width),tourelle1Rect.centery-(int(tourelle1Rect.height/8)),int(tourelle1Rect.width/4),int(tourelle1Rect.height/4)))
            tourelle1Desc = btnTourelle("Cannon",4,1,"Explosif",2,10,tourelle1Rect,window)


            tourelle2RectB = pygame.draw.rect(window,(0,0,0),(leftGUI.x,leftGUI.y+1/8*Y+1/5*Y+4,1/6*X,1/5*Y),2)
            tourelle2Rect = pygame.draw.rect(window,(150,150,150),(leftGUI.x,leftGUI.y+1/8*Y+1/5*Y+4,1/6*X,1/5*Y))
            tourelle2Disp = pygame.draw.rect(window,(49,140,231),(tourelle2Rect.x+(1/20*tourelle2Rect.width),tourelle2Rect.centery-(int(tourelle2Rect.height/8)),int(tourelle2Rect.width/4),int(tourelle2Rect.height/4)))
            tourelle2Desc = btnTourelle("Artefact",2,3,"Magique",1,60,tourelle2Rect,window)

            tourelle3RectB = pygame.draw.rect(window,(0,0,0),(leftGUI.x,leftGUI.y+1/8*Y+2/5*Y+6,1/6*X,1/5*Y),2)
            tourelle3Rect = pygame.draw.rect(window,(150,150,150),(leftGUI.x,leftGUI.y+1/8*Y+2/5*Y+6,1/6*X,1/5*Y))
            tourelle3Disp = pygame.draw.rect(window,(139,0,0),(tourelle3Rect.x+(1/20*tourelle3Rect.width),tourelle3Rect.centery-(int(tourelle3Rect.height/8)),int(tourelle3Rect.width/4),int(tourelle3Rect.height/4)))
            tourelle3Desc = btnTourelle("Tesla",1,1,"Electrique",6,100,tourelle3Rect,window)

            arrowdownRectB = pygame.draw.rect(window,(0,0,0),(leftGUI.x,leftGUI.y+1/8*Y+3/5*Y+8,1/6*X,1/8*Y),2)
            arrowdownRect = pygame.draw.rect(window,(150,150,150),(leftGUI.x,leftGUI.y+1/8*Y+3/5*Y+8,1/6*X,1/8*Y))
            flecheBas = pygame.image.load('flecheBasClean.png')
            flecheBas = pygame.transform.scale(flecheBas, (int(arrowdownRect.width/2), int(arrowdownRect.height/2)))
            positionFlecheBas = flecheBas.get_rect()
            positionFlecheBas.center = (arrowdownRect.centerx,arrowdownRect.centery)
            window.blit(flecheBas, positionFlecheBas)

            for event in Event:
                if event.type == 5 and event.button == 1:
                    if tourelle1Rect.collidepoint(pygame.mouse.get_pos()):
                        if tower.checkCost(money,10) == True:
                            currentTower = 1
                    if tourelle2Rect.collidepoint(pygame.mouse.get_pos()):
                        if tower.checkCost(money,60) == True:
                            currentTower = 2
                    if tourelle3Rect.collidepoint(pygame.mouse.get_pos()):
                        if tower.checkCost(money,100) == True:
                            currentTower = 3
                            #def createTower(liste,degats,element,vitesseA,currentTower,colorint,MAP,colonne,ligne):

                            #def __init__(self,nom,degats,vitesseA,element,distance,prix,tourelle1Rect,window):
                    if grid.collidepoint(pygame.mouse.get_pos()):
                        if currentTower == 1:
                            tower.currentTower,tower.listeTower,Mapping.MAP,money  = tower.createTower(tower.listeTower,4,"Explosif",1,currentTower,1,matrice,colonne,ligne,10,money)
                            currentTower = 0
                        if currentTower == 2:
                            tower.currentTower,tower.listeTower,Mapping.MAP,money  = tower.createTower(tower.listeTower,2,"Magique",3,currentTower,2,matrice,colonne,ligne,60,money)
                            currentTower = 0
                        if currentTower == 3:
                            tower.currentTower,tower.listeTower,Mapping.MAP,money = tower.createTower(tower.listeTower,1,"Electrique",1,currentTower,3,matrice,colonne,ligne,100,money)
                            currentTower = 0
                if event.type == 5 and event.button == 3:
                    currentTower = 0

    return colonne,ligne,curdif,matrice,index,pop,clic,currentTower,money

#Affiche le GUI comme l'argent , le niveau ect
def DrawGUI(window,PlayingState,X,Y,money,score,level,grid):
    if PlayingState:
        leftMenu = pygame.draw.rect(window,(120,120,120),(0,0,1/6*X,Y))
        pygame.draw.rect(window,(34,139,34),(grid.x,grid.y,4/6*X,5/6*Y))
        IntDif = text(20,str(money)+" $",(255,255,255),(176,224,230),7/10*X,20,window)
        IntDif = text(20,str(score)+" pts",(255,255,255),(176,224,230),8/10*X,20,window)
        IntDif = text(20,"lvl "+str(level),(255,255,255),(176,224,230),9/10*X,20,window)
        return leftMenu






#Fait disparaitre le popup quand on fait clic gauche
def DimissPopup(pop,Event):
    for event in Event:
        if event.type == 5 and event.button == 1:
            if len(pop) ==1:
                pop.pop()
    return pop


#Raffraichi la barre de difficulté
def Refresh_Difficulty_Bar(Curr_Difficulte,Seuil_Difficulte,fenetre,Show,X,Y):
    if Show:
        pygame.draw.rect(fenetre,(105,105,105),(2/6*X-1,19,2/6*X+2,22))
        if Curr_Difficulte/Seuil_Difficulte >= 1:
            pygame.draw.rect(fenetre,(255,255,0),(2/6*X,20,(2/6*X),20))
        elif Curr_Difficulte <= 0:
            pygame.draw.rect(fenetre,(255,255,0),(2/6*X,20,0,20))
        else:
            pygame.draw.rect(fenetre,(255,255,0),(2/6*X,20,(2/6*X)*(Curr_Difficulte/Seuil_Difficulte),20))
        IntDif = text(20,str(Curr_Difficulte)+"/"+str(Seuil_Difficulte),(255,255,255),(176,224,230),2/7*X,20,fenetre)