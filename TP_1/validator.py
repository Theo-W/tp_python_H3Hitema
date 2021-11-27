def validator(age, dure, credit):
    if(age > 18 or age < 75):
        print("l'age dois etres compris entre 18 ans à 75 ans")
    if(dure > 24 or dure < 96):
        print("le nombre de mois dois etres entre 24 et 96")
    if(credit > 500000):
        print("le crédit à un maximun de 500 000€")
    return (age, dure, credit)