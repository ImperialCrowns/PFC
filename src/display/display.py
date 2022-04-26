import os
from src.ascii.ascii_hands import ascii_hands


def pfc_combo(pl : str, ai : str) -> str :

    '''
    Entrée : Deux strings qui correspondent au choix du joueur et au choix de l'IA
    Sortie : Une String des ascii hands
    Fonction : Affichage des ascii hands
    '''

    res = ascii_hands[pl].split('\n')
    for i, line in enumerate(ascii_hands[ai].split('\n')):
        res[i] += " " * 10 + line[::-1].replace("(", ")").replace(")", "(")
    return '\n'.join(res)

def print_result_round(p_score : int, ia_score : int, p_choice : str, ia_choice : str) -> None:

    '''
    Entrée : 2 entiers et 2 strings qui sont respectivement les scores du joueurs et de l'IA et les choix respectifs
    Sortie : Rien
    Fonction : Affiche les résultats du tour actuel
    '''

    os.system('clear')
    print("                  | %d | %d |" % (p_score, ia_score))
    print(pfc_combo(p_choice, ia_choice))
    print("%s vs. %s" % (p_choice.capitalize(), ia_choice.capitalize()))
    print("\n")

def print_start_round() -> None:

    '''
    Entrée : Rien
    Sortie : Rien
    Fonction : Affiche le début d'un nouveau tour
    '''

    os.system('clear')
    print("                  | 0 | 0 |")
    print(pfc_combo("pierre", "pierre"))
    print("En attente...")
    print("\n")

def print_result_round(p_score : int, ia_score : int, p_choice : str, ia_choice : str) -> None :

    '''
    Entrée : p_score, ia_score, p_choice, ia_choice
    Sortie : Rien
    Fonction : Affiche les résultats du tour actuel
    '''

    os.system('clear')
    print("                  | %d | %d |" % (p_score, ia_score))
    print(pfc_combo(p_choice, ia_choice))
    print("%s vs. %s" % (p_choice.capitalize(), ia_choice.capitalize()))
    print("\n")
