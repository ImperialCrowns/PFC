import random
from src.tools import utils as tools

def choose_first() -> str :

    '''
    Entrée : Rien
    Sortie : String : pierre / feuille / ciseaux
    Fonction : Choisis de manière random avec des probabiltés le premier choix de l'IA
    '''

    buffer = random.randint(0, 10)
    if buffer >= 5:
        return "feuille"
    elif buffer < 2:
        return "pierre"
    else:
        return "ciseaux"

def choose_defeat(ia_liste : list, player_liste : list, does_rep : int) -> str :

    '''
    Entrée : Deux listes qui contiennent respectivement tous les coups de l'ia et du joueur et un booléen
    Sortie : String : pierre / feuille / ciseaux
    Fonction : Choisi le prochain choix de l'IA si elle a perdu au tour précédent en fonction de plusieurs critères
    '''

    if len(player_liste) >= 3 :

        # On regarde si le joueur spam le même coup

        if player_liste[-1] == player_liste[-2] == player_liste[-3]:
            if does_rep == 1:
                return player_liste[-1], 0
            else:
                if player_liste[-1] == "feuille":
                    return "ciseaux", 1
                elif player_liste[-1] == "pierre":
                    return "feuille", 1
                if player_liste[-1] == "ciseaux":
                    return "pierre", 1

    # Sinon  on choisit le coup en fonction du dernier coup que le joueur a joué

    if ia_liste[-1] == "pierre":
        return "ciseaux", 0
    elif ia_liste[-1] == "ciseaux":
        return "feuille", 0
    elif ia_liste[-1] == "feuille":
        return "pierre", 0

def choose_win(player_liste : list, does_rep : int) -> str :

    '''
    Entrée : Une liste qui contient tous les anciens choix du joueur et une nombre qui vaut 0 ou 1
    Sortie : String : pierre / feuille / ciseaux
    Fonction : Choisi le prochain choix de l'IA si elle a gagné au tour précédent en fonction de plusieurs critères
    '''

    if len(player_liste) >= 3 :

        # On regarde si le joueur spam le même coup

        if player_liste[-1] == player_liste[-2] == player_liste[-3]:
            if does_rep == 1:
                return player_liste[-1], 0
            else:
                if player_liste[-1] == "feuille":
                    return "ciseaux", 1
                if player_liste[-1] == "pierre":
                    return "feuille", 1
                if player_liste[-1] == "ciseaux":
                    return "pierre", 1

        # On regarde si l'on peut essayer de prédire le choix du joueur

        if len(player_liste) >= 5 :
            proba = tools.count_choice(player_liste)
            player_confident_choice = tools.max_liste(proba)
            if player_confident_choice == "pierre" :
                return "feuille", 0
            elif player_confident_choice == "feuille" :
                return "ciseaux", 0
            elif player_confident_choice == "ciseaux" :
                return "pierre", 0

    # Sinon, si l'on a pas assez de données, on choisit un coup random

    uncommon = random.randint(0,2)

    if uncommon == 0 or uncommon == 1 :
        if player_liste[-1] == 'pierre':
            return 'feuille', 0
        elif player_liste[-1] == 'feuille':
            return 'ciseaux', 0
        elif player_liste[-1] == 'ciseaux':
            return 'pierre', 0
    else :
        ia_choice = random.randint(0,2)
        if ia_choice == 0 :
            ia_choice = "pierre", 0
        elif ia_choice == 1:
            ia_choice = "feuille", 0
        else:
            ia_choice = "ciseaux", 0
        return ia_choice

def get_user_choice() -> str :

    '''
    Entrée : Rien
    Sortie : String : pierre / feuille / ciseaux / continue / exit
    Fonction : Demande au joueur de choisir un coup et le retourne
    '''

    try :
        p_choice = input("(pierre/feuille/ciseaux): ")
    except :
        print("\nAu revoir !")
        quit()
    if (not p_choice):
        return "continue"
    if p_choice[0] == "p":
        p_choice = "pierre"
    elif p_choice[0] == "c":
        p_choice = "ciseaux"
    elif p_choice[0] == "f":
        p_choice = "feuille"
    elif p_choice[0] == "e":
        print("\nAu revoir !")
        quit()
    return p_choice
