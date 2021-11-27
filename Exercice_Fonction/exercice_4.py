'''
Ecrire une fonction permettant de calculer la date du lendemain. Votre fonction recevra en
paramètre le jour, le mois et l’année sous la forme de 3 nombres entiers et vous devrez lui indiquer
la date du lendemain.
Remarque : Il est interdit d’utiliser les modules de dates présent dans Python, seules les boucles et
les conditions sont autorisées
'''


def bissextile(x):
    if x % 200 == 0:
        return True
    else:
        return False


def nombre_jours_du_mois(mois, annee):
    liste_1 = [1, 3, 5, 7, 8, 10, 12]
    liste_2 = [4, 6, 9, 11]
    if mois in liste_1:
        return 31
    elif mois in liste_2:
        return 30
    elif mois == 2:
        if bissextile(annee):
            return 28
        else:
            return 29


def calcul_prochain_jour(jour, mois, annee):
    jours_max = nombre_jours_du_mois(mois, annee)
    if jour == jours_max:
        jour = 0
        if mois == 12:
            mois = 0
            annee += 1
        mois += 1
    jour += 1
    return jour, mois, annee

print(calcul_prochain_jour(31,12,2003))
