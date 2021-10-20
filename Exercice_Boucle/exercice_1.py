# Ecrire un programme demandant à l’utilisateur la saisie de deux nombres et doit indiquer si
# le résultat du produit (multiplication) de ces deux nombres est positif ou négatif. Le
# programme ne doit à aucun moment calculer le produit des deux nombres (l’utilisation de
# l’opérateur de multiplication est interdit);

a = int(input('votre premier nombre'))
b = int(input('votre deuxieme nombre'))

if a > 0 and b > 0 or a < 0 and b < 0:
    print('possitif')
else:
    print('Negatof')