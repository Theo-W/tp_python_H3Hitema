"""
Ecrire les instructions demandant à l’utilisateur la saisie d’un nombre entier N puis ensuite
créer une liste de N éléments. Vous devrez ensuite demander à l’utilisateur de saisir les N
éléments à insérer dans la liste. Pensez à vérifier que la valeur de N saisie est bien positive et
affichez ensuite la liste créé.
"""

def exo4():
    a = 0
    n = int(input("entrer un bombre entier"))
    liste = [0] * n
    for i in range(n):
        liste[i] = int(input("entrer un valeur à placer dans la liste"))
    return liste