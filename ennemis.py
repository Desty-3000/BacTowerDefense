import mapping

class types:
    def __init__(self,vitesse,couleur,vie,element,recompense):
        self.vitesse = vitesse
        self.couleur = couleur
        self.vie = vie
        self.element = element
        self.recompense = recompense

def different_ennemis():
    ennemis_normal = ennemis.types(1,(0,0,255),1,'normal',10)
    return ennemis_normal

def spawn_ennemis(type_ennemis,carte,vague):
    for index,liste in enumerate(carte):
        for index2,valeur in enumerate(a):
            if valeur == 98:
                spawn = [index,index2]          #determine l'index du spawn, ce qui va permetre de calculer les coordonné pour draw les ennemis avec spawn[0] = y et spawn[1] = x

def pathfinding(carte)