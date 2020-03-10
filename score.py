import pygame
import ennemies

class score():
    def __init__(self):
        self.valeur = 0



def temp(phase):
    if phase == 'vivant':
        score_temp = 0
        if pygame.time.get_time()%1000 == 0:
            Score.valeur += 10

def ennemis(score,liste_killcount,liste_valeur_ennemis):
    for position,valeur in enumerate(liste_valeur_ennemis):
        score.valeur += valeur*liste_killcount[position]
    return score_ennemis
