"""
Ecrire une fonction permettant de transformer un nombre entier sous la forme d’une liste
contenant tous les chiffres de ce nombre. Par exemple si l’on appelle la fonction avec la
valeur 12358 cette dernière renverra la liste [1,2,3,5,8] .
"""


def exo6(n):
    return ([int(c) for c in str(n)])
