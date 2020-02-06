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
        IntDif = text(20,str(Curr_Difficulte)+"/"+str(Seuil_Difficulte),(255,255,255),(176,224,230),520,20,fenetre)


def DrawMapAndGUI(window,X,Y):
    pygame.draw.rect(window,(120,120,120),(0,0,1/6*X,Y))


