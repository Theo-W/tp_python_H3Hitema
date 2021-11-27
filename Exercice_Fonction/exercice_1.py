'''
Ecrire une fonction permettant d’afficher la table de multiplication de la valeur transmise en
paramètre (on affichera uniquement les 20 premiers termes).
'''


def table(num):
    for i in range(1, 21):
        t = num * i
        print(num, 'x', i, '=', t)
        i += 1
