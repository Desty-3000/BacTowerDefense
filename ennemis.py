import pygame
import Mapping

#initialisation des different ennemis a spawn sous la forme [lvl1,lvl2,lvl3,lvl4]
WaveEnnemieList = []
EnnemisSpawned = []

class types:
    def __init__(self,vitesse,couleur,vie,recompense):
        self.vitesse = vitesse
        self.couleur = couleur
        self.vie = vie
        self.recompense = recompense
        self.Index = Mapping.Spawn
        self.rectangle = pygame.rect(mapping.startCoordIndex[0]*mapping.c,mapping.startCoordIndex[1]*Mapping.d,mapping.c/5,mapping.d/5)
        self.case_a_suivre = 1
    def Draw(self,window):
        pygame.rect.draw(window,self.couleur,self.rectangle)
#TEMP
#lvl1 = types(2,(222,44,44),5,20)
#lvl2 = types(4,(255,236,0),3,30)
#lvl3 = types(2,(155,35,35),10,50)
#lvl4 = types(1,(141,12,198),100,200)
inittime = 0

def spawn_ennemis(temp,inittemp,liste_ennemis,WaveActuel,WaveEnnemies):
    wave = DefineWave(WaveActuel,WaveEnnemies)
    if inittemp == 0:
        inittemp = temp
    elif temp == inittemp+1:
        for numberEnnemis in wave:
            if numberEnnemis.index() == 0:
                for ennemis in range(numberEnnemis):
                    liste_ennemis.append(lvl1)
                    inittemp = temp
            if numberEnnemis.index() == 1:
                for ennemis in range(numberEnnemis):
                    liste_ennemis.append(lvl2)
                    inittemp = temp
            if numberEnnemis.index() == 2:
                for ennemis in range(numberEnnemis):
                    liste_ennemis.append(lvl3)
                    inittemp = temp
            if numberEnnemis.index() == 3:
                for ennemis in range(numberEnnemis):
                    liste_ennemis.append(lvl4)
                    inittemp = temp
    return liste_ennemis




def déplacement(joueur,carte,liste_ennemis,X_case,Y_case):     #X_case et Y_case en pixel
    for ennemis in liste_ennemis:
        X = ennemis.Index[0]
        Y = ennemis.Index[1]
        avancement = 0
        if carte[Y][X+1] == ennemis.case_a_suivre or carte[Y][X+1] == 97:
            ennemis.rectangle = ennemis.rectangle.move(ennemis.vitesse,0)
            avancement += 1
            if avancement == X_case:
                case_a_suivre += 1
                avancement = 0
        if carte[Y][X+1] == 97 and avancement == X_case:
            joueur.vie -= 1
            liste_ennemis.remove(ennemis)
        if carte[Y+1][X] == ennemis.case_a_suivre or carte[Y+1][X] == 97:
            rectangle_temp = ennemis.rectangle
            ennemis.rectangle = rectangle_temp.move(0,-ennemis.vitesse)
            avancement += 1
            if avancement == Y_case:
                ennemis.case_a_suivre += 1
                avancement = 0
        if carte[Y+1][X] == 97 and avancement == Y_case:
            joueur.vie -= 1
            liste_ennemis.remove(ennemis)
        if carte[Y][X-1] == ennemis.case_a_suivre or carte[Y][X-1] == 97:
            rectangle_temp = ennemis.rectangle
            ennemis.rectangle = rectangle_temp.move(-ennemis.vitesse,0)
            avancement += 1
            if avancement == X_case:
                ennemis.case_a_suivre += 1
                avancement = 0
            if carte[Y][X-1] == 97 and avancement == X_case:
                joueur.vie -= 1
                liste_ennemis.remove(ennemis)
        if carte[Y-1][X] == ennemis.case_a_suivre or carte[Y-1][X] == 97:
            rectangle_temp = ennemis.rectangle
            ennemis.rectangle = rectangle_temp.move(0,ennemis.vitesse)
            avancement += 1
            if avancement == Y_case:
                ennemis.case_a_suivre += 1
                avancement = 0
            if carte[Y-1][X] == 97 and avancement == Y_case:
                joueur.vie -= 1
                liste_ennemis.remove(ennemis)
    return liste_ennemis

def CheckEnnemieHealth(liste_ennemis):
    for ennemis in liste_ennemis:
        if ennemis.vie <= 0:
            liste_ennemis.remove(ennemis)
    return liste_ennemis

def DefineWave(wave,WaveEnnemies):
    if wave == 1:
        WaveEnnemies = [20,0,0,0]
    elif wave == 2:
        WaveEnnemies = [20,20,0,0]
    elif wave == 3:
        WaveEnnemies = [0,20,20,0]
    elif wave == 4:
        WaveEnnemies = [10,30,25,0]
    elif wave == 5:
        WaveEnnemies = [20,40,35,0]
    elif wave == 6:
        WaveEnnemies = [0,0,0,1]
    return WaveEnnemies




