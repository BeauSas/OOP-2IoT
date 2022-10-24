class Dier:
    def __init__(self,aantal_poten,kleur):
        self.soort = self.__class__.__name__
        self.aantal_poten = aantal_poten
        self.kleur = kleur

    def __repr__(self):
        return f"{self.soort}, {self.aantal_poten} poten, kleur: {self.kleur}"

class Wolf(Dier):
    def __init__(self,kleur):
        super(Wolf,self).__init__(4,kleur)

class Schaap(Dier):
    def __init__(self,kleur):
        super(Schaap,self).__init__(4,kleur)

class Slang(Dier):
    def __init__(self,kleur):
        super(Slang,self).__init__(0,kleur)

class Papegaai(Dier):
    def __init__(self,kleur):
        super(Papegaai,self).__init__(2,kleur)

animal1 = Wolf("Grijs")
animal2 = Wolf("Paars")

animal3 = Schaap("Wit")
animal4 = Schaap("Zwart")

animal5 = Slang("Groen")
animal6 = Slang("Bruin")

animal7 = Papegaai("Rood")
animal8 = Papegaai("Blauw")

print(animal1)
print(animal2)
print(animal3)
print(animal4)
print(animal5)
print(animal6)
print(animal7)
print(animal8)