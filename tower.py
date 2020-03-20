import pygame
import Mapping

pygame.init()

#Liste des towers sur le grid
listeTower = []

#Int de la tour séléctionée : 0 = none , 1 = cannon , 2 = artefact , 3 = tesla
currentTower = 0

#Prévisualisation de la tourelle pour la placer
towerRect = pygame.Rect(0,0,0,0)

#classe d'une tourelle type
class tower:
    def __init__(self,degats,element,vitesseA,colorint):
        self.degats,self.element,self.vitesseA,self.colorint = degats,element,vitesseA,colorint
    #pour la poser sur le grid
    def setPos(self,case):
        self.Pos = pygame.Rect(case.x+(1/4*case.width),case.y+(1/4*case.height),1/2*case.width,1/2*case.height)
    #pour l'afficher
    def Draw(self,window):
        if self.colorint == 1:
            self.Pos = pygame.draw.rect(window,(255,255,255),self.Pos)
        if self.colorint == 2:
            self.Pos = pygame.draw.rect(window,(49,140,231),self.Pos)
        if self.colorint == 3:
            self.Pos = pygame.draw.rect(window,(139,0,0),self.Pos)

#Au moment du clique sur le grid pour la poser dessus et retirer l'argent
def createTower(liste,degats,element,vitesseA,currentTower,colorint,MAP,colonne,ligne,price,money):
    if currentTower != 0:
        cursor = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        test = cursor.collidelist(Mapping.GetCaseRectList(colonne,ligne,MAP))
        if test != -1:
            if test < colonne:
                currCase = Mapping.GetCase(test,0,MAP)
            else:
                currCase = Mapping.GetCase(test-colonne*int(test/colonne),int(test/colonne),MAP)
            if currCase.IsPath == False and currCase.HasTower == False:
                newTower = tower(degats,element,vitesseA,colorint)
                newTower.setPos(currCase.innerRect)
                liste.append(newTower)
                currentTower = 0
                currCase.Lock()
                MAP[int(test/colonne)][test-colonne*int(test/colonne)] = currCase
                money = money - price
    return currentTower,liste,MAP,money



    return liste

#Check si on a assez d'argent
def checkCost(money,price):
    if money-price<0:
        return False
    else:
        return True

#Affiche la prévisualisation de la tourelle
def TowerPlacement(window,currentTower,towerRect,casel,casew):

    if currentTower != 0:
        if currentTower == 1:
            couleur = (255,255,255)
        elif currentTower == 2:
            couleur = (49,140,231)
        elif currentTower == 3:
            couleur = (139,0,0)
        towerRect = pygame.draw.rect(window,couleur,(pygame.mouse.get_pos()[0]-int(casew/4),pygame.mouse.get_pos()[1]-int(casel/4),int(casew/2),int(casel/2)))
    else :
        towerRect = pygame.Rect(0,0,0,0)

    return towerRect


