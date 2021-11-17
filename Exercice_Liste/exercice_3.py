"""
Ecrire une fonction permettant de calculer la moyenne d’une liste de nombres passé en
paramètres
"""

def moyenne(liste):
    tot = 0
    a = 0
    for i in range(len(liste)):
        a = liste[i]
        tot += a
    return (tot/len(liste))