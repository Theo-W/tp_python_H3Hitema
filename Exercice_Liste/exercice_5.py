"""
Ecrire les instructions permettant de créer une liste à partir de deux autres listes
préalablement construits. Le nouveau tableau sera la somme des éléments des deux listes de
départ.
"""


def exo5(liste1, liste2):
    liste3 = [0] * len(liste1)
    for i in range(len(liste1)):
        liste3[i] = liste1[i] + liste2[i]
    return liste3
