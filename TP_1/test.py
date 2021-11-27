def age_mult_3(age):
    if age % 3 == 0:
        return True
    else:
        return False

def taux_credit():
    taux = 1.3
    age = int(input("Veuillez saisir votre âge"))
    montant = int(input("Veuillez saisir le montant de votre crédit"))
    duree = int(input("Veuillez saisir le nombre d'années de votre crédit"))
    prix_ccul = montant - 250000
    print("age = ", age)
    print("duree= ", duree)
    print("montant ", montant)
    if age < 17 or age > 76:
        return("Vous n'avez pas l'age requis pour effectuer votre demande")
    if montant > 500001:
        return("Le montant est trop important pour effctuer votre demande")
    if 0 > duree or duree > 5:
        return("La durée du crédit n'est pas bonne pour effectuer votre demande")
    if age_mult_3(age) == True:
        taux -= 0.1
    if montant < 250000:
        if age < 27:
            taux += (0.3*(duree+1))
        else:
            taux += (0.3*(duree+2))
    else:
        if age > 45:
            return("Vous être trop vieux pour demander un crédit de plus de 2 ans")
        tranches = prix_ccul // 12000
        taux += (tranches * 0.1)
    if taux < 0.8:
        taux = 0.8
    return("Le taux de votre crédit est de : ", taux)