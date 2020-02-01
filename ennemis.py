import mapping

class types:
    def __init__(self,vitesse,couleur,vie,element,recompense):
        self.vitesse = vitesse
        self.couleur = couleur
        self.vie = vie
        self.element = element
        self.recompense = recompense

def differents_ennemis():
    ennemis_normal = types(1,(0,0,255),1,'normal',10)
    return ennemis_normal

def spawn_ennemis(type_ennemis,carte,fenetre):
    for index,liste in enumerate(carte):
        for index2,valeur in enumerate(a):
            if valeur == 98:
                spawn = [index,index2]          #determine l'index du spawn, ce qui va permetre de calculer les coordonné pour draw les ennemis avec spawn[0] = y et spawn[1] = x
    ennemis = pygame.draw.rect(fenetre,type_ennemis.couleur,(spawn[1]*50,spawn[0]*50,10,10))    #les coordonnés sont temporaire
    ennemis_vivant = []
    ennemis_vivant.append(ennmis)
    ennemis_vie = []
    ennemis_vie.append(type_ennemis.vie)
    return spawn,ennemis_vie,ennemis_vivant

def déplacement(carte,emplacement_spawn):

