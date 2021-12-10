"""
Définir une classe Rectangle d'attributs:longueur et largeur et nom et les méthodes:
perimetre qui retourne le périmètre du rectangle.
surface qui retourne la surface du rectangle.
afficher qui affiche le périmètre et la surface d'un rectangle ainsi leurs dimensions en longueur et
largeur.

 Définir une classe Carre héritant de Rectangle et qui surcharge l’attribut d’instance : nom =
"carré".
"""


class Rectangle:

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "Rectangle"

    def perimetreRectagle(self):
        return  (self.largeur * 2) + (self.longueur * 2)


    def aireRetangle(self):
        return self.longueur * self.largeur

    def afficher(self):
        print(self.nom,": Longeur", self.longueur, "Largeur", self.largeur, "Le périmètre du restangle est", self.perimetreRectagle(), "L'aire du rectangle est", self.aireRetangle())

r = Rectangle(3,5)
r.afficher()

class Carre(Rectangle):

    def __init__(self, cote):
        self.largeur = cote
        self.longueur = cote
        self.nom = "Carré"

c = Carre(4)
c.afficher()