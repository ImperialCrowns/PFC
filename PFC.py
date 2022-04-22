#!/bin/python3

from display import print_result_round, print_start_round
from choice import choose_defeat, choose_first, choose_win, get_user_choice
from tools import utils

def pfc() -> None:

    '''
    Entrée : Rien
    Sortie : Rien
    Fonction : Boucle Principal, affichage, récupère les choix du joueur et de l'IA
    '''

    file_read = open("data.txt", "r")
    file_read.close()

    # Affichage

    print_start_round()

    # Init variable

    ia_score = 0
    p_score = 0
    ia_liste = []
    p_liste = []
    does_rep = 0

    # Début de la Boucle principale

    while (p_score < 5 and ia_score < 5) :

        # Choix de l'IA

        if len(ia_liste) == 0:
            ia_choice = choose_first()
        elif who_win_last == "ia":
            ia_choice, does_rep = choose_defeat(ia_liste, p_liste, does_rep)
        elif who_win_last == "player":
            ia_choice, does_rep = choose_win(p_liste, does_rep)
        who_win_last = "player"

        # Choix du joueur

        p_choice = get_user_choice();
        if p_choice == "continue":
            continue

        # Win / Draw / Defeat

        if (p_choice == ia_choice) :
            p_liste.append(p_choice)
            ia_liste.append(ia_choice)
        elif p_choice == "pierre" and ia_choice == "ciseaux" :
            p_score += 1
            p_liste.append(p_choice)
            ia_liste.append(ia_choice)
        elif p_choice == "feuille" and ia_choice == "pierre" :
            p_score += 1
            p_liste.append(p_choice)
            ia_liste.append(ia_choice)
        elif p_choice == "ciseaux" and ia_choice == "feuille" :
            p_score += 1
            p_liste.append(p_choice)
            ia_liste.append(ia_choice)
        elif p_choice != "ciseaux" and p_choice != "pierre" and p_choice != "feuille" :
            continue
        else:
            ia_score += 1
            who_win_last = "ia"
            p_liste.append(p_choice)
            ia_liste.append(ia_choice)

        # Affichage

        print_result_round(p_score, ia_score, p_choice, ia_choice)

    utils.calcul_percent(p_liste)


# Fonction main, début du programme

if __name__ == "__main__":
    pfc()
