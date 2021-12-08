"""
6) L’exercice se base sur le fichier « exo 6 .csv » permettant de mettre en place un début de
manipulation autour de fichiers csv. Le contenu de ce fichier csv est composé d’auteurs, de
citations et de titres. (Pensez à regarder le contenu du fichier pour mieux comprendre ce qui
est demandé)
a. Créez une fonction entete qui prend comme paramètre une chaine de caractères se
trouvant dans l'entête du fichier ( "Auteur", "Citation", ou "Titre"), et qui renvoie le
numéro
de
la
colonne
correspondante.
EXEMPLE : "Citation" =>2Votre fonction devra se baser sur la première ligne du fichier et donc ne pas contenir
de valeur « en dur » dans votre code. On consédérera la première colonne comme la
colonne n°1

b. En utilisant la fonction enteteprécédement créée, créez une fonction titres qui a
comme paramètre le nom d'un auteur et qui affiche les titres référencés pour cet
auteur.
EXEMPLE : "ShafiqueKeshabjee" => "Le roi, le sage et le bouffon"

c. En utilisant la fonction enteteprécédement créée, créez une fonction citations qui a
comme paramètre un titre et qui affiche toutes les citations référencées pour ce titre
et
l'auteur
correspondant.
EXEMPLE : "No et moi" => "Et si c'était ça le bonheur, pas même un rêve, pas même
une promesse, juste l'instant."

d. En utilisant la fonction enteteprécédement créée,créez une fonction ecrire qui a
comme paramètres trois chaines de caractères ( un nom d'auteur, une citation et un
titre ) et qui rajoute une ligne correspondant à ces données dans le fichier.
"""
import tarfile

#A)
def entete(intitule):
    f = open('TP_fichiers_1_1/exo6.csv', 'r')
    ligne = f.readlines()
    f.close()

    return ligne.split(';').index(intitule) + 1
#print(entete('Citation'))

#B)
def titres(auteur):
    f = open('TP_fichiers_1_1/exo6.csv', 'r')
    content = f.readlines()
    f.close()

    for e in content:
        if e.split(';')[entete("Auteur") - 1] == auteur:
            print(e.split(";")[entete('Titre') - 1])

#C)
def citation(titre):
    f = open('TP_fichiers_1_1/exo6.csv', 'r')
    content = f.readlines()
    f.close()

    for e in content:
        if e.split(';')[entete("Citation") - 1] == citation:
            print(e.split(";")[entete('Auteur') - 1], e.split(';')[entete('Titre') - 1])

#d)
def ajouter(auteur, titre, citation):
    ligne = ["", "", ""]
    ligne[entete("Auteur") - 1] = auteur
    ligne[entete("Titre") - 1] = titre
    ligne[entete("Citation") - 1] = citation
    l = ";".join('ligne') + "\n"
    fa = open("TP_fichiers_1_1/exo6.csv", 'a')
    fa.write(l)
    fa.close()

#print(ajouter('', '', ''))