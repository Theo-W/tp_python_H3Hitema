print('Montant du credit')
montant = int(input())
print('Durée (en année)')
duree = int(input())
print('Age du client')
age = int(input())
taux = 1.3

if 1 <= duree <= 4 and 18 <= age <= 75 and montant < 500000:
    if(age // 10 + age%10)%3:
        taux -= 0.1
    if montant < 250000:
        if age < 27:
            taux += 0.3 * (duree - 1)
        elif age > 35:
            taux += 0.3 * (duree + 2)
        else:
             taux += 0.3 * duree
    else:
        if age > 45 and duree > 2:
            print("Crédit refuser")
        else:
            reste = montant - 250000
            tranches = reste // 12000

    if taux < 0.8:
        taux = 0.8

    print('Taux:', taux)

else :
    print('Crédit refuser')

print('saisir le montant:')
montant = int(input())
print('saisir la durée (en année)')
duree = int(input())
print('saisir le taux')
taux = int(input())

mt_total = montant + (taux/100)*montant
mensualité = mt_total / (duree*12)
mois = 0

while mt_total > 0:
    mt_total -= mensualité
    print("mois: ", mois, "montant: ",mensualité, "reste à payer", mt_total)
    mois+=1