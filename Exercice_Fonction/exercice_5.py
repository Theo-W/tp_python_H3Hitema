'''
Une adresse IP est composée de 4 chiffres allant de 0 à 255 séparés par un « . » .
Par exemple :
192.168.1.10
10.10.2.25
Sont des adresses IP.
Ecrire un programme permettant de générer (et afficher) l’ensemble des adresses IP possibles
'''

def affIp ():
    for i in range(256):
        for j in range(256):
            for k in range(256):
                for l in range (256):
                    print(i,'.',j,'.',k,'.',l)

print(affIp())