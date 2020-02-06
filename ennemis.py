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

def differents_ennemis():
    ennemis_normal = types(1,(0,0,255),1,'normal',10)
    return ennemis_normal

def init_spawn(carte):
    for index,liste in enumerate(carte):
        for index2,valeur in enumerate(a):
            if valeur == 98:
                spawn = [index,index2]          #determine l'index du spawn, ce qui va permetre de calculer les coordonné pour draw les ennemis avec spawn[0] = y et spawn[1] = x
    return spawn

def spawn_ennemis(type_ennemis,fenetre,spawn):
    ennemis = pygame.draw.rect(fenetre,type_ennemis.couleur,(spawn[1]*50,spawn[0]*50,10,10))    #les coordonnés sont temporaire
    ennemis_vivant.append(ennemis)
    ennemis_vie.append(type_ennemis.vie)
    position.append(spawn)
    return spawn,ennemis_vie,ennemis_vivant

def déplacement(carte,position_ennemis,liste_ennemis,fenetre):
    for index,valeur in enumerate(liste_ennemis):
        y = position_ennemis[index][0]
        x = position_ennemis[index][1]
        if carte[y+1][x] == 99:
            for i in range(50):
                valeur = pygame.move(0,1)
                nouvelle_ennemis = pygame.draw.rect(fenetre,(0,0,255),valeur)
                liste_ennemis[index] = nouvelle_ennemis

        elif carte[y-1][x] == 99:
            for i in range(50):
                valeur = pygame.move(0,-1)
                nouvelle_ennemis = pygame.draw.rect(fenetre,(0,0,255),valeur)
                liste_ennemis[index] = nouvelle_ennemis
        elif carte[y][x+1] == 99:
            for i in range(50):
                valeur = pygame.move(1,0)
                nouvelle_ennemis = pygame.draw.rect(fenetre,(0,0,255),valeur)
                liste_ennemis[index] = nouvelle_ennemis
        elif carte[y][x-1] == 99:
            for i in range(50):
                valeur = pygame.move(-1,0)
                nouvelle_ennemis = pygame.draw.rect(fenetre,(0,0,255),valeur)
                liste_ennemis[index] = nouvelle_ennemis




