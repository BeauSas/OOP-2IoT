from turtle import title


class Boek:
    def __init__(self,titel,auteur,prijs,dikte):
        self.titel = titel
        self.auteur = auteur
        self.prijs = prijs
        self.dikte = dikte

class Kast(Boek):
    def __init__(self,ruimte):
        self.plank = []
        self.ruimte = ruimte

    def voeg_boek_toe(self,*boek):
        for b in boek:
            if(self.ruimte > boek.dikte):
                self.plank.append(b)
                self.ruimte -= boek.dikte
            else:
                print("Onvoldoende ruimte.")

    def totaal_prijs(self):
        waarde = sum(boek.prijs for boek in self.plank)
        return waarde

    def bevat_boek(self,titel):
        for x in len(self.plank):
            if(x == titel):
                return True
            else:
                return False

    def __repr__(self):
        boeklijst = "Boek: "
        boeklijst += '\t'.join(str(b) for b in self.plank)
        return boeklijst

kast1 = Kast(20)
boek1 = Boek("Python V1","Kristof",15,4)
boek2 = Boek("Moby Dick","Mr. Krabs",35,8)
boek3 = Boek("Maan, vis, roos","Junior",5,2)
boek4 = Boek("College For Dummies","Beau",19,4)
boek5 = Boek("Forbidden Book","X",125,10)


kast1.voeg_boek_toe(boek1,boek2,boek3,boek4)
kast1.voeg_boek_toe(boek5)
print(kast1.totaal_prijs())

print(kast1)
