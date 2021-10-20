"""
Ecrire un programme demandant à l’utilisateur la saisie de N nombres entiers et affichera
ensuite le résultat de la moyenne de l’ensemble de ces nombres. La valeur de N est
déterminée par l’utilisateur au tout début du programme
"""

N = int(input())
i = 0
somme = 0

while i < N:
    somme += int(input())
    i += 1
print(somme/N)