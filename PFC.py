#!/bin/python3

import os
import random

ascii_hands = {}
ascii_hands["pierre"] = '''
    _______       
---'   ____)      
      (_____)     
      (_____)     
      (____)      
---.__(___)       
'''
ascii_hands["feuille"] = '''
    _______       
---'   ____)____  
          ______) 
          _______)
         _______) 
---.__________)   
'''
ascii_hands["ciseaux"] = '''
    _______       
---'   ____)____  
          ______) 
       __________)
      (____)      
---.__(___)       
'''

def pfc_combo(pl, ai):

    '''
    Entrée : Deux strings qui correspondent au choix du joueur et au choix de l'IA
    Sortie : Une String des ascii hands
    Fonction : Affichage des ascii hands
    '''

    res = ascii_hands[pl].split('\n')
    for i, line in enumerate(ascii_hands[ai].split('\n')):
        res[i] += " " * 10 + line[::-1].replace("(", ")").replace(")", "(")
    return '\n'.join(res)

def choose_first():

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

def count_choice(p_liste):

    '''
    Entrée : Une liste qui contient tous les coups du joueur
    Sortie : Une liste de liste qui contient le nombre de fois que le joueur a joué tel coup
    Fonction : Compte le nombre de fois que le joueur a joué chaque coup : Pierre / Feuille / Ciseaux
    '''

    pierre = 0
    feuille = 0
    ciseaux = 0
    for i in p_liste:
        if i == "pierre" :
            pierre += 1
        elif i == "feuille" :
            feuille += 1
        elif "ciseaux" :
            ciseaux += 1
    return [["pierre", pierre], ["feuille", feuille], ["ciseaux", ciseaux]]

def max_liste(liste):

    '''
    Entrée : Une liste qui contient le nombre de fois que le joueur a effectué un coup et son pourcentage
    Sortie : Une string qui correspond au nom du coup que le joueur joue le plus souvent
    Fonction : Détermine le choix que le joueur fait le plus
    '''

    maxi = 0
    for i in range(0, len(liste)) :
        if liste[i][1] > maxi:
            maxi = i
    return liste[i][0]

def choose_defeat(ia_liste, player_liste, does_rep):

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

def choose_win(player_liste, does_rep):

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
            proba = count_choice(player_liste)
            player_confident_choice = max_liste(proba)
            if player_confident_choice == "pierre" :
                return "feuille", 0
            elif player_confident_choice == "feuille" :
                return "ciseaux", 0
            elif player_confident_choice == "ciseaux" :
                return "pierre", 0
    
    # Sinon, si l'on a pas assez de données, on choisit un coup random

    ia_choice = random.randint(0,2)
    if ia_choice == 0 :
        ia_choice = "pierre", 0
    elif ia_choice == 1:
        ia_choice = "feuille", 0
    else:
        ia_choice = "ciseaux", 0
    return ia_choice

def calcul_percent(p_liste) :

    '''
    Entrée : Une liste qui contient tous les anciens choix du joueur
    Sortie : Rien
    Fonction : Écrit dans un fichier le nombre de coup du joueur pour chaque choix avec son pourcentage d'être choisi
    '''

    pierre = 0
    feuille = 0
    ciseaux = 0
    for i in p_liste:
        if i == "pierre":
            pierre += 1
        if i == "feuille":
            feuille += 1
        if i =="ciseaux":
            ciseaux += 1
    liste = []
    liste.append(["pierre: ", pierre, pierre // len(p_liste)])
    liste.append(["feuille: ", feuille, feuille // len(p_liste)])
    liste.append(["ciseaux: ", ciseaux, ciseaux // len(p_liste)])
    file_write = open("data.txt", 'a')
    file_write.write("Pierre : " + str(pierre) + " " + str(pierre / len(p_liste) * 100) + "\n" + "Feuille : " + str(feuille) + " " + str(feuille / len(p_liste) * 100) + "\n" + "Ciseaux : " + str(ciseaux) + " " + str(ciseaux / len(p_liste) * 100) + "\n\n")
    file_write.close()


def pfc():

    '''
    Entrée : Rien
    Sortie : Rien
    Fonction : Boucle Principal, affichage, récupère les choix du joueur et de l'IA
    '''

    file_read = open("data.txt", "r")
    file_read.close()

    # Affichage

    os.system('clear')
    print("                  | 0 | 0 |")
    print(pfc_combo("pierre", "pierre"))
    print("En attente...")
    print("\n")

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

        p_choice = input("(pierre/feuille/ciseaux): ")
        if (not p_choice):
            continue
        if p_choice[0] == "p":
            p_choice = "pierre"
        elif p_choice[0] == "c":
            p_choice = "ciseaux"
        elif p_choice[0] == "f":
            p_choice = "feuille"

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
        
        os.system('clear')
        print("                  | %d | %d |" % (p_score, ia_score))
        print(pfc_combo(p_choice, ia_choice))
        print("%s vs. %s" % (p_choice.capitalize(), ia_choice.capitalize()))
        print("\n")

    calcul_percent(p_liste)


pfc()