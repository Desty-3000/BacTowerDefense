import pygame
import mapping

ennemis_vivant = []
ennemis_vie = []
position = []

class types:
    def __init__(self,vitesse,couleur,vie,element,recompense):
        self.vitesse = vitesse
        self.couleur = couleur
        self.vie = vie
        self.element = element
        self.recompense = recompense
        self.Index = mapping.startCoordIndex
        self.rectangle = pygame.rect(mapping.startCoordIndex[0]*mapping.c,mapping.startCoordIndex[1]*mapping.d,mapping.c/5,mapping.d/5)

def init_spawn(carte):
    for index,liste in enumerate(carte):
        for index2,valeur in enumerate(a):
            if valeur == 98:
                spawn = [index,index2]          #determine l'index du spawn, ce qui va permetre de calculer les coordonné pour draw les ennemis avec spawn[0] = y et spawn[1] = x
    return spawn

def spawn_ennemis(type_ennemis,fenetre):
    if pygame.time.get_tick()%1000 == 0:
        pygame.draw.rect(fenetre,type_ennemis.couleur,type_ennemis.rectangle)    #les coordonnés sont temporaire
        ennemis_vivant.append(type_ennemis)
    return ennemis_vivant



def déplacement(carte,liste_ennemis,fenetre):
    for ennemis in liste_ennemis:
        X = ennemis.Index[0]
        Y = ennemis.Index[1]
        if carte[Y][X+1] ==







