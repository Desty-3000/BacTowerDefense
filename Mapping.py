import pygame

pygame.init()

Curr_Difficulte = 20

Niveau = 0

GRID = pygame.Rect(1,1,1,1)
caseList = []
rectList = []

endCoordIndex =   []
startCoordIndex = []


isStartPlaced = False
gridinit = False


isMapDisplayed = False


nbreLigne = 10
nbreColonne = 10
class text:
    def __init__(self,width,text,color1,color2,x,y,fenetre):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.topleft = (x,y)
        fenetre.blit(self.playBtn, self.playRect)

class case:
    innerRect = pygame.Rect(1,1,1,1)

    def __init__(self,x,y,window,width,length,colorint):
        self.Colorint,self.x,self.y,self.window,self.width,self.length = colorint,x,y,window,width,length
        self.rect = pygame.Rect(x,y,width,length)
    def update(self):
        if self.Colorint != 0:
            if self.Colorint == 97:
                self.innerRect = pygame.draw.rect(self.window,(255,0,0),(self.x,self.y,self.width,self.length))
            elif self.Colorint == 99:
                self.innerRect = pygame.draw.rect(self.window,(0,0,255),(self.x,self.y,self.width,self.length))
            elif self.Colorint == 98:
                self.innerRect = pygame.draw.rect(self.window,(0,255,0),(self.x,self.y,self.width,self.length))
        else:
            self.innerRect = pygame.draw.rect(self.window,(255,0,0),(self.x,self.y,self.width,self.length),-1)
        self.rect = pygame.draw.rect(self.window,(0,0,0),(self.x,self.y,self.width,self.length),2)


MAP =[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]
]

c = 0
d = 0
def drawMap(display,X,Y,colonne,ligne,fenetre):

    grid = pygame.Rect(0,0,4/6*X,5/6*Y)
    grid.center = (X/2+1/10*X,Y/2)
    c = (grid.topright[0]-grid.topleft[0])/colonne
    d = (grid.bottomleft[1]-grid.topleft[1])/ligne

   # if not display:
    #    ligne = []
     #   for i in range(nbreLigne):
      #      for x in range(nbreColonne):
       #         ligne.append(case(1,1,fenetre,50,50,0))
        #MAP.append(ligne)
        #ligne.clear()
    return grid,c,d


#Phase 0 = Mapping , 1 = Attacking
Mapping_Phase = False

Seuil_Difficulte = 10

def Initiate_Mapping_Phase(Seuil_Difficulte,Niveau,Phase):
    Phase = False
    New_Seuil_Difficulte = 10 + Niveau * 2
    return New_Seuil_Difficulte,Phase

Seuil_Difficulte,Mapping_Phase = Initiate_Mapping_Phase(Seuil_Difficulte,Niveau,Mapping_Phase)

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

def DrawMapAndGUI(window,PlayingState,X,Y,money,score,level,matrice,ligne,colonne,rectlist,grid,c,d,caselist):

    if PlayingState:
        pygame.draw.rect(window,(120,120,120),(0,0,1/6*X,Y))
        pygame.draw.rect(window,(34,139,34),(grid.x,grid.y,4/6*X,5/6*Y))
        IntDif = text(20,str(money)+" $",(255,255,255),(176,224,230),7/10*X,20,window)
        IntDif = text(20,str(score)+" pts",(255,255,255),(176,224,230),8/10*X,20,window)
        IntDif = text(20,"lvl "+str(level),(255,255,255),(176,224,230),9/10*X,20,window)
        rectlist.clear()
        caselist.clear()
        for oui in range(ligne):
            for non in range(colonne):
                newR = case(grid.x+(c*non),grid.y+(d*oui),window,c,d,matrice[oui][non])
                caselist.append(newR)
                rectlist.append(newR.rect)
    return grid,rectlist,caselist