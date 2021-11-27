'''
Ecrire une fonction permettant de calculer le seuil de rentabilité d’une machine déterminé par le
scénario suivant. On considère qu’une machine est achetée à un prix X à une certaine date. On
considère qu’une machine perd 5% de sa valeur chaque année sauf les années bissextiles où elle
perd 15% .
Le seuil de rentabilité de la machine est atteint à partir du moment où sa valeur est inférieure ou
égale à 23% du montant d’achat (X) de la machine.
La fonction recevra en paramètre l’année d’achat et le montant, elle devra retourner le nombre
d’années nécessaires pour atteindre ce seuil de rentabilité.
Remarque : On considère que les années bissextiles sont les années multiples de 200.
'''

montant = int(input("Entrez Le montant: "))
annee = int(input("Entrez l annee a verifier: "))
m = montant
a = annee

while m > ((montant * 23)/100):
    a += 1
    if(annee%4==0 and annee%100!=0 or annee%400==0):
         m = m - ((m * 15)/100)
    else:
        m = m - ((m * 5) /100)
print(a - annee)