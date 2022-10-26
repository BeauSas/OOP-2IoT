class Persoon:
    population = 0
    def __init__(self,naam="John Doe"):
        self.__class__.population += 1
        self.naam = naam

    def __del__(self):
        self.__class__.population -= 1
    
    def __repr__(self):
        return f"Totale populatie: {str(self.__class__.population)}"

p1 = Persoon("Eric")
p2 = Persoon("Mar")
p3 = Persoon("Dude")
p4 = Persoon("Dudette")
p5 = Persoon()

print()
print(p3)
print()
del p2
print(p5)