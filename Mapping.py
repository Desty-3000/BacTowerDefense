import pygame

pygame.init()

Curr_Difficulte = 8

Niveau = 1


class text:
    def __init__(self,width,text,color1,color2,x,y,fenetre):
        self.font = pygame.font.Font('freesansbold.ttf', width)
        self.playBtn = self.font.render(text, True, color1, color2)
        self.playRect = self.playBtn.get_rect()
        self.playRect.topleft = (x,y)
        fenetre.blit(self.playBtn, self.playRect)





#Phase 0 = Mapping , 1 = Attacking
Mapping_Phase = False

Seuil_Difficulte = 10

def Initiate_Mapping_Phase(Seuil_Difficulte,Niveau,Phase):
    Phase = False
    New_Seuil_Difficulte = 16 + Niveau * 1.5
    return New_Seuil_Difficulte,Phase

Seuil_Difficulte,Mapping_Phase = Initiate_Mapping_Phase(Seuil_Difficulte,Niveau,Mapping_Phase)

def Refresh_Difficulty_Bar(Curr_Difficulte,Seuil_Difficulte,fenetre,Show,X,Y):
    if Show:
        pygame.draw.rect(fenetre,(105,105,105),(2/6*X,20,2/6*X,20))
        pygame.draw.rect(fenetre,(255,255,0),(2/6*X,20,(2/6*X)*(Curr_Difficulte/Seuil_Difficulte),20))
        IntDif = text(20,str(Curr_Difficulte)+"/"+str(Seuil_Difficulte),(255,255,255),(176,224,230),2/7*X,20,fenetre)


def DrawMapAndGUI(window,PlayingState,X,Y,money,score,level):
    if PlayingState:
        pygame.draw.rect(window,(120,120,120),(0,0,1/6*X,Y))
        a = X/2+1/10*X
        b = Y/2
        grid = pygame.Rect(0,0,4/6*X,5/6*Y)
        grid.center = (a,b)
        pygame.draw.rect(window,(34,139,34),(grid.x,grid.y,4/6*X,5/6*Y))
        IntDif = text(20,str(money)+" $",(255,255,255),(176,224,230),7/10*X,20,window)
        IntDif = text(20,str(score)+" pts",(255,255,255),(176,224,230),8/10*X,20,window)
        IntDif = text(20,"lvl "+str(level),(255,255,255),(176,224,230),9/10*X,20,window)
        return [a,b]