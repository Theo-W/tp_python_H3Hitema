"""
Même question que l’exercice précédent mais pour récupérer la plus petite valeur
(l’utilisation de la fonction min() est interdite)
"""


def exo2(liste):
    ppv = liste[0]
    a = 0
    for i in range(1,len(liste)):
        a = liste[i]
        if ppv > a:
            ppv = a
    return ppv