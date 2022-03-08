#!/bin/python3

from itertools import count
import os
import random

from numpy import who

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
    res = ascii_hands[pl].split('\n')
    for i, line in enumerate(ascii_hands[ai].split('\n')):
        res[i] += " " * 10 + line[::-1].replace("(", ")").replace(")", "(")
    return '\n'.join(res)

def choose_first():
    buffer = random.randint(0, 10)
    if buffer >= 5:
        return "feuille"
    elif buffer < 2:
        return "pierre"
    else:
        return "ciseaux"

def choose_defeat(ia_liste, player_liste):
    if len(player_liste) >= 3 :
        if player_liste[-1] == player_liste[-2] == player_liste[-3]:
            if player_liste[-1] == "feuille":
                return "ciseaux"
            elif player_liste[-1] == "pierre":
                return "feuille"
            if player_liste[-1] == "ciseaux":
                return "pierre"
    if ia_liste[-1] == "pierre":
        return "ciseaux"
    elif ia_liste[-1] == "ciseaux":
        return "feuille"
    elif ia_liste[-1] == "feuille":
        return "pierre"

def count_choice(p_liste):
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
    maxi = 0
    for i in range(0, len(liste)) :
        if liste[i][1] > maxi:
            maxi = i
    return liste[i][0]

def choose_win(ia_liste, player_liste):
    if len(player_liste) >= 3 :
        if player_liste[-1] == player_liste[-2] == player_liste[-3]:
            if player_liste[-1] == "feuille":
                return "ciseaux"
            elif player_liste[-1] == "pierre":
                return "feuille"
            if player_liste[-1] == "ciseaux":
                return "pierre"
        if len(player_liste) >= 5 :
            proba = count_choice(player_liste)
            player_confident_choice = max_liste(proba)
            if player_confident_choice == "pierre" :
                return "feuille"
            elif player_confident_choice == "feuille" :
                return "ciseaux"
            elif player_confident_choice == "ciseaux" :
                return "pierre"
    ia_choice = random.randint(0,2)
    if ia_choice == 0 :
        ia_choice = "pierre"
    elif ia_choice == 1:
        ia_choice = "feuille"
    else:
        ia_choice = "ciseaux"
    return ia_choice

def pfc():
    os.system('clear')
    print("                  | 0 | 0 |")
    print(pfc_combo("pierre", "pierre"))
    print("En attente...")
    print("\n")
    ia_score = 0
    p_score = 0
    ia_liste = []
    p_liste = []
    while (p_score < 5 and ia_score < 5) :
        if len(ia_liste) == 0:
            ia_choice = choose_first()
        elif who_win_last == "ia":
            ia_choice = choose_defeat(ia_liste, p_liste)
        elif who_win_last == "player":
            ia_choice = choose_win(ia_liste, p_liste)
        who_win_last = "player"
        p_choice = input("(pierre/feuille/ciseaux): ")
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
        os.system('clear')
        print("                  | %d | %d |" % (p_score, ia_score))
        print(pfc_combo(p_choice, ia_choice))
        print("%s vs. %s" % (p_choice.capitalize(), ia_choice.capitalize()))
        print("\n")
pfc()