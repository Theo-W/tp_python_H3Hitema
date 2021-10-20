# Ecrire un programme permettant d’obtenir le résultat du calcul de la somme de tous les
# nombres entiers de 1 à 100 :
# 1 + 2 + ⋯ + 98 + 99 + 100 = ?

nombre = 1
resultat = 0

for i in range(100):
    resultat += nombre
    nombre += 1
print(resultat)