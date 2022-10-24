class Bolletje:
    def __init__(self, smaak):
        self.smaak = smaak

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

    def __repr__(self):
        return '\n'.join(s.smaak for s in self.bolletjes)

class Reuzenhoorntje(Hoorntjes):
    maximum_bolletjes=5

ijsbak1 = Bolletje("Smurf")
ijsbak2 = Bolletje("Pistache")
ijsbak3 = Bolletje("Cookie Dough")
ijsbak4 = Bolletje("Mint")
ijsbak5 = Bolletje("Strawberry")
   
ijsRH1 = Reuzenhoorntje()
ijsRH1.bolletjes_toevoegen(ijsbak1,ijsbak2)
ijsRH1.bolletjes_toevoegen(ijsbak3,ijsbak4)
ijsRH1.bolletjes_toevoegen(ijsbak5)

print(ijsRH1)