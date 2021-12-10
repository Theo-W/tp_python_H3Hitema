constructeur: une methode obligatoire dans chacune des classes. Son rôles de est de permettre la création d'instances de la classe. Son nom est `__init__`

`self`: mot cle représentant l'instance que l'on est entrain de manipuler. Il s'utilise que dans les classes

ex: 
```python
class Personnage:
    def __init__(self):
        self.nom = "Michel"
        self.age = 45
```

utilisation: 
```python
p1 = Personnage()
print(p1.age) # 19

p1.age = 22
print(p1.age) # 22
```

création d'un construteur avec parametre: 
```python
def __init__(self, age = 19):
    self.non = "Michel"
    self.age = age
```