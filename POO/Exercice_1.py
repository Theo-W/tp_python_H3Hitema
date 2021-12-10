"""
Écrire un programme Python qui permet de définir une classe Satellite qui permette d’instancier
des objets simulant des satellites artificiels lancés dans l’espace, autour de la terre. Le
constructeur de cette classe initialisera les attributs d’instance suivants, avec les valeurs par
défaut indiquées : masse = 100, vitesse = 0.œ
Créez plusieurs satellites avec des valeurs différentes.
Ajoutez deux méthodes accélérer/ralentir permettant de modifier automatiquement la vitesse
du satellite. LA vitesse maximale du satellite est définit comme étant égale au triple de sa masse.
"""


class Satellite:

    def __init__(self, m=100, v=0):
        self.masse = m
        self.vitesse = v

    def acceleter(self):
        if self.vitesse < self.masse * 3:
            self.vitesse += self.vitesse

    def ralentir(self):
        self.vitesse -= 50




s1 = Satellite()
s2 = Satellite(500, 50)
s2.acceleter()
print(s2.vitesse)

class ManagementSatelite:

    def __int__(self, m, v):
        self.masse = m
        self.vitesse = v


    def eregister(self, galaxie = []):

    def gestion(self):
        i = 0
        galaxie = []
        while i != 4:
            print("Saisir 1 pour ajouter")
            print("Saisir 2 pour enregistrer dans un fichier")
            print("Saisir 3 pour pour charger depuis un fichier")
            print("Saisir 4 pour quitter")
            i = int(input())

        if i == 1:
            m = int(input('Saisir la masse du Satellite'))
            v = int(input('Saisir la vitesse du Satellite'))
            galaxie.append(Satellite(m, v))

        elif i == 2:
            m = int(input('Saisir la masse du Satellite'))
            v = int(input('Saisir la vitesse du Satellite'))
            g = galaxie.append(Satellite(m ,v))

            f = open('satelite.txt', 'w')
            f.write(g)
            f.close()
        elif i == 3:

            m = int(input('Saisir la masse du Satellite'))
            v = int(input('Saisir la vitesse du Satellite'))
            g = galaxie.append(Satellite(m ,v))

            f = open('satelite.txt', 'w')
            f.write(g)
            f.close()

