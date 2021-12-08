"""
On souhaite créer un mini-dictionnaire de traduction entre deux langues. On choisira une
langue de référence à laquelle on fera correspondre pour chaque mot une traduction sous la
forme « mot : traduction » . On souhaite ranger toutes ces informations dans un fichier en y
indiquant un mot (et sa traduction) par ligne.

a. Ecrire une fonction traduire(mot) qui prend en paramètre un mot et retourne sa
traduction issue du dictionnaire. Si le mot n’est pas présent dans le dictionnaire la
fonction devra retourner la valeur vide (None).

b. Ecrire une fonction ajoute(mot,traduction) qui prend en paramètre un mot et sa
traduction et ajoute cette nouvelle référence dans le dictionnaire. On veillera à
s’assurer que le mot n’est pas déjà présent dans le dictionnaire.

c. Ecrire une fonction supprime(mot) qui prend en paramètre un mot et supprime
celui-ci ainsi que sa traduction du dictionnaire.
"""


#A)
def traduire(mot):
    d = open('TP_fichiers_1_1/exo5.txt', 'r')
    r = d.readlines()
    d.close()

    for i in r:
        p = i.split(':')
        if p[0] == mot:
            return p[1]
    return None
#print(traduire('moche'))

#B)
def addtraduire(mot, traduire):
    if traduire(mot) is None:
        d = open('TP_fichiers_1_1/exo5.txt', 'a')
        t = [mot, ':', traduire]
        w = "".join(t)
        d.write(w + '\n')
        d.close()
#print(addtraduire('toi', 'you'))

#C)
def deletetraduire(mot):
    d = open('TP_fichiers_1_1/exo5.txt', 'r')
    r = d.readlines()
    d.close()
    idx = 0

    while idx < len(r):
        if r[idx].split(':')[0] == mot:
            r.pop(idx)
        idx += 1

    f = open('TP_fichiers_1_1/exo5.txt', 'w')
    f.writelines(r)
    f.close()

#print(deletetraduire('coucou'))

