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
    Phase = True
    New_Seuil_Difficulte = 16 + Niveau * 1.5
    return New_Seuil_Difficulte,Phase

Seuil_Difficulte,Mapping_Phase = Initiate_Mapping_Phase(Seuil_Difficulte,Niveau,Mapping_Phase)

def Refresh_Difficulty_Bar(Curr_Difficulte,Seuil_Difficulte,fenetre):
    pygame.draw.rect(fenetre,(105,105,105),(100,20,200,20))
    pygame.draw.rect(fenetre,(255,255,0),(100,20,200*(Curr_Difficulte/Seuil_Difficulte),20))
    IntDif = text(20,str(Curr_Difficulte)+"/"+str(Seuil_Difficulte),(255,255,255),(0,0,0),320,20,fenetre)




