import pygame
import mapping

ennemis_vivant = []
ennemis_vie = []
position = []

class joueur:
    def __init__(self):
        self.vie = 5

class types:
    def __init__(self,vitesse,couleur,vie,element,recompense):
        self.vitesse = vitesse
        self.couleur = couleur
        self.vie = vie
        self.element = element
        self.recompense = recompense
        self.Index = mapping.startCoordIndex
        self.rectangle = pygame.rect(mapping.startCoordIndex[0]*mapping.c,mapping.startCoordIndex[1]*mapping.d,mapping.c/5,mapping.d/5)
        self.case_a_suivre = 1

def spawn_ennemis(type_ennemis,fenetre):
    if pygame.time.get_tick()%1000 == 0:
        pygame.draw.rect(fenetre,type_ennemis.couleur,type_ennemis.rectangle)
        ennemis_vivant.append(type_ennemis)
    return ennemis_vivant



def déplacement(carte,liste_ennemis,fenetre,X_case,Y_case,phase):     #X_case et Y_case en pixel
    if phase == 'vivant':
        for ennemis in liste_ennemis:
            X = ennemis.Index[0]
            Y = ennemis.Index[1]
            avancement = 0
            if carte[Y][X+1] == ennemis.case_a_suivre or carte[Y][X+1] == 97:
                ennemis.rectangle = ennemis.rectangle.move(1,0)
                pygame.draw.rect(fenetre,ennemis.couleur,ennemis.rectangle)
                avancement += 1
                if avancement == X_case:
                    ennemis.case_a_suivre += 1
                    avancement = 0
                if carte[Y][X+1] == 97 and avancement == X_case:
                    joueur.vie -= 1
                    liste_ennemis.remove(ennemis)
            if carte[Y+1][X] == ennemis.case_a_suivre or carte[Y+1][X] == 97:
                rectangle_temp = ennemis.rectangle
                ennemis.rectangle = rectangle_temp.move(0,-1)
                pygame.draw.rect(fenetre,ennemis.couleur,ennemis.rectangle)
                avancement += 1
                if avancement == Y_case:
                    ennemis.case_a_suivre += 1
                    avancement = 0
                if carte[Y+1][X] == 97 and avancement == Y_case:
                    joueur.vie -= 1
                    liste_ennemis.remove(ennemis)
            if carte[Y][X-1] == ennemis.case_a_suivre or carte[Y][X-1] == 97:
                rectangle_temp = ennemis.rectangle
                ennemis.rectangle = rectangle_temp.move(-1,0)
                pygame.draw.rect(fenetre,ennemis.couleur,ennemis.rectangle)
                avancement += 1
                if avancement == X_case:
                    ennemis.case_a_suivre += 1
                    avancement = 0
                if carte[Y][X-1] == 97 and avancement == X_case:
                    joueur.vie -= 1
                    liste_ennemis.remove(ennemis)
            if carte[Y-1][X] == ennemis.case_a_suivre or carte[Y-1][X] == 97:
                rectangle_temp = ennemis.rectangle
                ennemis.rectangle = rectangle_temp.move(0,1)
                pygame.draw.rect(fenetre,ennemis.couleur,ennemis.rectangle)
                avancement += 1
                if avancement == Y_case:
                    ennemis.case_a_suivre += 1
                    avancement = 0
                if carte[Y-1][X] == 97 and avancement == Y_case:
                    joueur.vie -= 1
                    liste_ennemis.remove(ennemis)








