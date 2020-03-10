import pygame

pygame.init()

#Difficulté actuelle et à atteindre a virer dans la classe joueur dans le main
Curr_Difficulte = 20
Seuil_Difficulte = 10

#Niveau a virer dans la classe joueur dans le main
Niveau = 0

#Int qui permet de connaitre le nombre de cases chemin (il vaut donc le dernier PathInt)
pathNumber = -1

#Grille qui représente le fond du plateau de jeu
GRID = pygame.Rect(1,1,1,1)

#Est ce que la grille à été initialisée ?
gridinit = False

#Nombre de ligne et de colonnes présents
nbreLigne = 10
nbreColonne = 10

#Taille en pixel que fait chaque case
caseWid = 20
caseLen = 20


#Classe pour simplifier l'écriture sur l'écran
class text:
    def __init__(self,width,text,color1,color2,x,y,fenetre):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.topleft = (x,y)
        fenetre.blit(self.playBtn, self.playRect)

#Classe du behavior d'une case
class case:
    #innerRect est le rectangle interieur a la case, celui qui se colorie
    innerRect = pygame.Rect(1,1,1,1)
    #Si la case fait partie du chemin ou non
    IsPath = False
    #Int qui permet de connaitre l'ordre des cases chemin
    PathInt = -1
    def __init__(self,x,y,window,width,length):
        self.x,self.y,self.window,self.width,self.length = x,y,window,width,length
        #rect est la bordure noire de chaque case
        self.rect = pygame.Rect(x,y,width,length)
    #Cette fonction est apellée pour afficher les cases
    def draw(self,x,y,w,l,colonne,ligne,grid,pathN):
        self.width = w
        self.length = l
        self.x = x
        self.y = y
        if self.IsPath:
            #PathInt == 0 est le début du chemin affiché en rouge
            if self.PathInt == 0:
                self.innerRect = pygame.draw.rect(self.window,(255,0,0),(self.x,self.y,self.width,self.length))
            #PathInt == PathN est le nombre total de cases chemin , donc la fin qui est affichée en bleu
            elif self.PathInt == pathN:
                self.innerRect = pygame.draw.rect(self.window,(0,0,255),(self.x,self.y,self.width,self.length))
            #Sinon le chemin est afficher en vert clair
            else:
                self.innerRect = pygame.draw.rect(self.window,(0,255,0),(self.x,self.y,self.width,self.length))
        else:
            self.innerRect = pygame.draw.rect(self.window,(255,0,0),(self.x,self.y,self.width,self.length),1)
        self.rect = pygame.draw.rect(self.window,(0,0,0),(self.x,self.y,self.width,self.length),2)
    #Cette fonction est apellée pour rajouter la case au chemin
    def AddToPath(self,PathInt):
        if self.PathInt == -1:
            self.IsPath = True
            self.PathInt = PathInt+1
            return PathInt+1
        return PathInt
    #Cette fonction est apellée pour retirer la case du chemin
    def RemoveFromPath(self):
        self.IsPath = False
        self.PathInt = -1
        return PathInt-1

#Matrice qui stocke toute les cases et leur ordre
MAP =[]


#Fonction qui initialise un plateau 10x10
def InitMap(window,MAP):
    for x in range(10):
        ligne = []
        for y in range(10):
            ligne.append(case(0,0,window,caseWid,caseLen))
        MAP.append(ligne)
    return MAP


#Renvoie l'objet case grâce à sa ligne et à sa colonne dans la matrice MAP
def GetCase(colonne,ligne,MAP):
    return MAP[ligne][colonne ]

#Renvoie la liste de toutes les cases de la matrice MAP
def GetCaseRectList(colonne,ligne,MAP):
    liste = []
    for x in range(ligne):
        for y in range(colonne):
            liste.append(MAP[x][y].innerRect)

    return liste
#Renvoie la matrice de tout les PathInt de chaque case sur le modèle de la matrice MAP
def GetCasePathIntList(colonne,ligne,MAP):
    liste = []
    for x in range(ligne):
        ligne = []
        for y in range(colonne):
            ligne.append(MAP[x][y].PathInt)
        liste.append(ligne)
    return liste

#Permet de rajouter une colonne à la matrice MAP
def AddColonne(colonne,MAP,curdif,window):
    colonne +=1
    for i in range(len(MAP)):
        MAP[i].append(case(0,0,window,caseLen,caseWid))
    return colonne,MAP,curdif-1

#Permet de rajouter une ligne à la matrice MAP
def AddLigne(ligne,colonne,MAP,caseLen,caseWid,curdif,window):
    ligne +=1
    newLine = []
    for i in range(colonne):
        newLine.append(case(0,0,window,caseLen,caseWid))
    MAP.append(newLine)
    return ligne,MAP,curdif-1

#Permet de retirer une colonne à la matrice MAP
def RemoveColonne(colonne,MAP,curdif):
    colonne -=1
    for i in range(len(MAP)):
        MAP[i].pop()
    return colonne,MAP,curdif+1

#Permet de retirer une ligne à la matrice MAP
def RemoveLigne(ligne,MAP,curdif):
    ligne -=1
    MAP.pop()
    return ligne,MAP,curdif+1

#Calcule la taille du grid et la taille des cases par rapport à la taille de l'écran et du nombre de colonne/ligne
def drawMap(X,Y,colonne,ligne,fenetre):

    grid = pygame.Rect(0,0,4/6*X,5/6*Y)
    grid.center = (X/2+1/10*X,Y/2)
    caseLen = (grid.topright[0]-grid.topleft[0])/colonne
    caseWid = (grid.bottomleft[1]-grid.topleft[1])/ligne
    return grid,caseLen,caseWid

#Actualise l'affichage des cases
def drawCases(MAP,colonne,ligne,w,l,grid,IsGridInit,pathN):
    if IsGridInit:
        for x in range(ligne):
            for y in range(colonne):
                currCase = GetCase(y,x,MAP)
                currCase.draw(grid.x+(w*y),grid.y+(l*x),w,l,colonne,ligne,grid,pathN)

#[A OPTIMISER PSK DEGEU]
#Grosse fonction pas belle à lire du tout qui check avant le placement d'une case chemin si il y en a bien une deja adjacente
def checkPathBuild(colonne,ligne,MAP,x,y,pathN):

    if pathN == -1: return True
    if y == colonne-1:
        if GetCasePathIntList(colonne,ligne,MAP)[x][y-1] == pathN: return True
        if x == 0:
            if GetCasePathIntList(colonne,ligne,MAP)[x+1][y] == pathN: return True
        if x == ligne-1:
            if GetCasePathIntList(colonne,ligne,MAP)[x-1][y] == pathN: return True
        else:
            if GetCasePathIntList(colonne,ligne,MAP)[x+1][y] == pathN: return True
            if GetCasePathIntList(colonne,ligne,MAP)[x-1][y] == pathN: return True
    if y > 0 and y != colonne-1:
        if GetCasePathIntList(colonne,ligne,MAP)[x][y-1] == pathN: return True
        if GetCasePathIntList(colonne,ligne,MAP)[x][y+1] == pathN: return True
        if x == ligne-1:
            if GetCasePathIntList(colonne,ligne,MAP)[x-1][y] == pathN: return True
        if x > 0 and x != ligne-1:
            if GetCasePathIntList(colonne,ligne,MAP)[x-1][y] == pathN: return True
            if GetCasePathIntList(colonne,ligne,MAP)[x+1][y] == pathN: return True
        if x == 0:
            if GetCasePathIntList(colonne,ligne,MAP)[x+1][y] == pathN: return True
    if y == 0:
        if GetCasePathIntList(colonne,ligne,MAP)[x][y+1] == pathN: return True
        if x == ligne-1:
            if GetCasePathIntList(colonne,ligne,MAP)[x-1][y] == pathN: return True
        if x > 0 and x != ligne-1:
            if GetCasePathIntList(colonne,ligne,MAP)[x-1][y] == pathN: return True
            if GetCasePathIntList(colonne,ligne,MAP)[x+1][y] == pathN: return True
        if x == 0:
            if GetCasePathIntList(colonne,ligne,MAP)[x+1][y] == pathN: return True
    return False

#Permet de modifier le chemin
def setPath(event,MAP,colonne,ligne,pathN):
    if event.type == 5 and event.button == 1:

        cursor = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        test = cursor.collidelist(GetCaseRectList(colonne,ligne,MAP))
        if test != -1:
            currCase = GetCaseRectList(colonne,ligne,MAP)[test]
            if checkPathBuild(colonne,ligne,MAP,int(test/colonne),test-colonne*int(test/colonne),pathN):
                if test < colonne:
                    pathN = MAP[0][test].AddToPath(pathN)
                else:
                    pathN = MAP[int(test/colonne)][test-colonne*int(test/colonne)].AddToPath(pathN)

    return pathN


# [A VIRER DANS MENU]
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
# [A VIRER DANS MENU]
#Draw le GUI comme l'argent , le niveau ect
def DrawGUI(window,PlayingState,X,Y,money,score,level,grid):

    if PlayingState:
        pygame.draw.rect(window,(120,120,120),(0,0,1/6*X,Y))
        pygame.draw.rect(window,(34,139,34),(grid.x,grid.y,4/6*X,5/6*Y))
        IntDif = text(20,str(money)+" $",(255,255,255),(176,224,230),7/10*X,20,window)
        IntDif = text(20,str(score)+" pts",(255,255,255),(176,224,230),8/10*X,20,window)
        IntDif = text(20,"lvl "+str(level),(255,255,255),(176,224,230),9/10*X,20,window)