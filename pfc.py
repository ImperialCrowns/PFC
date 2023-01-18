#!/bin/python3

from src.display import display
from src.choice import choice
from src.tools import utils as tools

def pfc() -> None:

    '''
    Entrée : Rien
    Sortie : Rien
    Fonction : Boucle Principal, affichage, récupère les choix du joueur et de l'IA
    '''

    # Ouverture du fichier data

    file_read = open("data.txt", "r")
    file_read.close()

    # Affichage

    display.print_start_round()

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
            ia_choice = choice.choose_first()
        elif who_win_last == "ia":
            ia_choice, does_rep = choice.choose_defeat(ia_liste, p_liste, does_rep)
        elif who_win_last == "player":
            ia_choice, does_rep = choice.choose_win(p_liste, does_rep)
        who_win_last = "player"

        # Choix du joueur

        p_choice = choice.get_user_choice();
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

        display.print_result_round(p_score, ia_score, p_choice, ia_choice)

    # Gestion des données

    tools.calcul_percent(p_liste)
    tools.format_data()


# Fonction main, début du programme

if __name__ == "__main__":
    pfc()
