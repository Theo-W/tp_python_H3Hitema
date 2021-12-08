"""
Ecrire un programme permettant d’inverser le contenu d’un fichier mot à mot.
Exemple de modification :
Avant : Le soleil est bleu
Apres : bleu est soleil Le
"""

a = "Le soleil est bleu"
c = a.split()
c.reverse()
g = ' '.join(c)

f = open('TP_fichiers_1_1/exo4.txt', 'w')
f.write(g)
f.close()