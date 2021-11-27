from TP_1.multiple import age_mult_3


def taux(age, dure, credit):
    taux = 1.3
    montant  = credit - 250000

    if age_mult_3(age) == True:
        taux -= 0.1

    if (credit < 250000):
        if age < 27:
            taux += (0.3 * (dure + 1))
        else:
            taux += (0.3 * (dure + 2))

    else:
        if age > 45:
            return ('Nous sommes désoler mais vous êtres trop vieux')
        tranche = montant // 12000
        taux += (tranche * 0.1)
    if taux < 0.8:
        taux = 0.8
    return("Le taux de votre crédit est de : ", taux)


