from TP_1.calcul import taux
from TP_1.multiple import age_mult_3
from TP_1.validator import validator

age = int(input("Saisir l'age: "))
dure = int(input("Saisir la duré; "))
credit = int(input("Saisir votre crédit"))

validator(age, dure, credit)
age_mult_3(age)
taux(age, dure, credit)