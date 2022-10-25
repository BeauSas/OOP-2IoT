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

class Kooi:
    def __init__(self,ID):
        self.ID = ID
        self.dieren = []
        
    def voeg_dier_toe(self,dier):
        self.dieren.append(dier)

    def voeg_dieren_toe(self,*dier):
        for d in dier:
            self.dieren.append(d)
    
    def __repr__(self):
        outp = f"Kooi {self.ID}\n"
        outp += '\n'.join('\t' + str(d) for d in self.dieren)
        return outp

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

print()
print("Kooien")
print("--------")
print()

kooi1 = Kooi(1)
kooi2 = Kooi(2)
kooi3 = Kooi(3)

kooi1.voeg_dier_toe(animal3)
kooi1.voeg_dieren_toe(animal1,animal2) 
print(kooi1)
print()

kooi2.voeg_dier_toe(animal4)
kooi2.voeg_dieren_toe(animal5) 
print(kooi2)
print()

kooi3.voeg_dier_toe(animal6)
print(kooi3)