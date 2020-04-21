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
    def __init__(self,degats,element,vitesseA,colorint,sprite):
        self.degats,self.element,self.vitesseA,self.colorint,self.sprite = degats,element,vitesseA,colorint,sprite
    #pour la poser sur le grid
    def setPos(self,case):
        if self.colorint == 1:
            self.Pos = pygame.Rect(case.x+(1/4*case.width),case.y+(1/4*case.height),2/4*case.width,2/4*case.height)
        elif self.colorint == 2:
            self.Pos = pygame.Rect(case.x+(2/6*case.width),case.y-(1/8*case.height),2/6*case.width,case.height)
        elif self.colorint == 3:
            self.Pos = pygame.Rect(case.x+(1/4*case.width),case.y-(1/8*case.height),2/4*case.width,case.height)
    #pour l'afficher
    def Draw(self,window):
        self.sprite = pygame.transform.scale(self.sprite, (self.Pos.width, self.Pos.height))
        window.blit(self.sprite, (self.Pos.x,self.Pos.y))


#Au moment du clique sur le grid pour la poser dessus et retirer l'argent
def createTower(liste,degats,element,vitesseA,currentTower,colorint,MAP,colonne,ligne,price,money,sprite):
    if currentTower != 0:
        cursor = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        test = cursor.collidelist(Mapping.GetCaseRectList(colonne,ligne,MAP))
        if test != -1:
            if test < colonne:
                currCase = Mapping.GetCase(test,0,MAP)
            else:
                currCase = Mapping.GetCase(test-colonne*int(test/colonne),int(test/colonne),MAP)
            if currCase.IsPath == False and currCase.HasTower == False:
                sprite = pygame.transform.scale(sprite, (int(currCase.width), int(currCase.length)))
                newTower = tower(degats,element,vitesseA,colorint,sprite)
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
def TowerPlacement(window,currentTower,casel,casew):

    if currentTower != 0:
        if currentTower == 1:
            img = pygame.image.load('cannon.png')
            img = pygame.transform.scale(img, (int(2/4*casew),int(2/4*casel)))
        elif currentTower == 2:
            img = pygame.image.load('artefact.png')
            img = pygame.transform.scale(img, (int(2/6*casew),int(casel)))
        elif currentTower == 3:
            img = pygame.image.load('tesla.png')
            img = pygame.transform.scale(img, (int(2/4*casew),int(casel)))
        imgpos = img.get_rect()
        imgpos.center = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        window.blit(img,imgpos)


