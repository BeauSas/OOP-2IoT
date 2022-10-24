def exercise_seperator(exercisenr):
    print()
    print("OEFENING ",exercisenr)
    print("------------")
    print()


#Oefening 1
exercise_seperator(1)
class Bolletje:
    def __init__(self, smaak):
        self.smaak = smaak

def maak_bolletjes():
    bolletje_1 = Bolletje("Vanille")
    bolletje_2 = Bolletje("Chocolade")
    bolletje_3 = Bolletje("Banaan")

    bolletjes = [bolletje_1.smaak,bolletje_2.smaak,bolletje_3.smaak]

    for items in bolletjes:
        print(items)

maak_bolletjes()

#Oefening 2 + 3 + 4
exercise_seperator(2)

class Hoorntjes:
    maximum_bolletjes = 2
    
    def __init__(self):
        self.bolletjes = []

    def bolletjes_toevoegen(self, *nieuwe_bolletjes):
        if  len(self.bolletjes) <= self.maximum_bolletjes:
            for singleB in nieuwe_bolletjes:
                self.bolletjes.append(singleB)
        else:
            pass
    
    def single_bol_toevoegen(self, nieuwe_bolletjes):
        self.bolletjes.append(nieuwe_bolletjes)

    def __str__(self):
        convertedlist = []
        for bollen in self.bolletjes:
            convertedlist.append(bollen.smaak)
        return "\n".join(convertedlist)

ijsbak1 = Bolletje("Smurf")
ijsbak2 = Bolletje("Pistache")
ijsbak3 = Bolletje("Cookie Dough")
ijsbak4 = Bolletje("Mint")
ijsbak5 = Bolletje("Strawberry")

hoorntje1 = Hoorntjes()
hoorntje1.single_bol_toevoegen(ijsbak1)
print()
print("Eén smaak besteld: ",hoorntje1)
print()
hoorntje1.bolletjes_toevoegen(ijsbak3,ijsbak5)
print()
print("Meerdere smaken besteld:\n",hoorntje1)
print()
hoorntje1.bolletjes_toevoegen(ijsbak4)
print()
print("Meerdere smaken, yet we only add 1:\n",hoorntje1)
print()