import pygame


pygame.init()




Curr_Difficulte = 0

Niveau = 1

Seuil_Difficulte = 0

def Initiate_Mapping_Phase(Seuil_Difficulte,Niveau):

    New_Seuil_Difficulte = 10 + Niveau * 1.5
    return New_Seuil_Difficulte

Seuil_Difficulte = Initiate_Mapping_Phase(Seuil_Difficulte,Niveau)

def Refresh_Difficulty_Bar():
    import Main
    Difficulty_Bar = pygame.draw.rect(Main.fenetre,(255,255,255),(50,50,100,20))