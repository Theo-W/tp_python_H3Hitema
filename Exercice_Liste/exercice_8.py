"""
Ecrire les intructionspermettant de calculer le schtroumpf (rien a voir avec
les petits personnages bleus) de deux tableaux T1 et T2 de  taillesrespectives
 N1 et N2
"""


def exo8(l1, l2):
    resultat = 0
    a = 0
    b = 0
    for i in range(len(l1)):
        a = l1[i]
        for j in range(len(l2)):
            b = l2[j]
            resultat += (a * b)
    return resultat
