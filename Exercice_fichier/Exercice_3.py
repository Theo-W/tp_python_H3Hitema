"""
Ecrire un programme permettant de déterminer si un fichier est carré ou non. On considère
qu’un fichier est carré à partir du moment où il a autant de lignes que de caractères sur
chacune de ses lignes.
"""

a = open('TP_fichiers_1_1/exo1.txt', 'r')
b = a.readlines()
a.close()

for e in b:
    if len(e) != len(b):
        print('c pas carré')

print('c carre')
        