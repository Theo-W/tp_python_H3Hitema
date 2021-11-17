"""
Ecrire une fonction recevant en paramètre deux listes, cette fonction devra renvoyer le
nouvelle liste. La nouvelle liste sera construite en alternant les valeurs des deux listes. Dans
le cas où les deux listes auraient des tailles différentes, on se contentera d’ajouter les
éléments supplémentaires à la fin de la liste.
"""


def exo7(liste1, liste2):
    if len(liste1) < len(liste2):
        petite_liste = len(liste1)
        gra = 2
        reste = len(liste2) - len(liste1)
    elif len(liste2) < len(liste1):
        petite_liste = len(liste2)
        gra = 1
        reste = len(liste1) - len(liste2)
    else:
        petite_liste = len(liste1)
        gra = 0
        reste = 0
    liste3 = [0] * (len(liste1)+len(liste2))
    j = 0
    for i in range(petite_liste):
        liste3[j] = liste1[i]
        liste3[j+1] = liste2[i]
        j += 2
        print("liste1 = ", liste1)
        print("liste2 = ", liste2)
        print("liste3 = ", liste3)
        print("j =", j)
    print("petite liste =", petite_liste)
    k = 2*petite_liste
    if gra == 2:
        for l in range(reste):
            liste3[k] = liste2[petite_liste]
            petite_liste += 1
    elif gra == 1:
        for l in range(reste):
            liste3[k] = liste1[petite_liste]
            petite_liste += 1
    return liste3

print(exo7([5,4,9,7], [1,4]))