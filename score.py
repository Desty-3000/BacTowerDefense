import pygame
import ennemies

def temp():
    while vivant:
        pygame.time.wait(1000)
        score_temp += 10
    return score_temp

def ennemis(liste_killcount,liste_valeur_ennemis):
    score_ennemis = 0
    for position,valeur in enumerate(liste_valeur_ennemis):
        score_ennemis += valeur*liste_killcount[position]
    return score_ennemis
