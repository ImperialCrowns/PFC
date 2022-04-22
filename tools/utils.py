def count_choice(p_liste : list) -> list :

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

def max_liste(liste : list) -> str :

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

def calcul_percent(p_liste : list) -> None :

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
