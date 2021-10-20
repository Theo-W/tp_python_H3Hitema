# Ecrire un programme demandant à un utilisateur de saisir un nombre puis affiche les 10
# nombres suivants. Par exemple si l’utilisateur saisit 47, il faudra afficher les nombres de 48
# jusqu’ à 57.

a = int(input('donnez moi un nombre'))
b = a + 10

while a <= b:
    print(a)
    a += 1