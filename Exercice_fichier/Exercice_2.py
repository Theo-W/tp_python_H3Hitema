'''
Ecrire une fonction permettant d’obtenir le nombre de lignes d’un fichier.
'''

a = open('TP_fichiers_1_1/exo1.txt', 'r')
print(len(a.readlines()))

