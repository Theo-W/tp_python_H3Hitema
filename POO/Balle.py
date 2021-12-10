class Balle:
    def __inti(self, n, a=19):
        self.nom = n
        self.age = a

    def bonjour(self):
        print('Bonjours', self.nom)

    def indentique(self, p):
        if self.nom == p.nom and self.age == p.age:
            return True
        else:
            return False
        