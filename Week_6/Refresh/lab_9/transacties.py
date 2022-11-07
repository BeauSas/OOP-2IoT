class Balans:
    def __init__(self,startbedrag):
        self.startbedrag = startbedrag
    
    def __repr__(self):
        return f"Huidig balans: {self.startbedrag}"

class Transactie(Balans):
    def __init__(self):
        pass

    def storting(self,bedrag):
        self.startbedrag += bedrag

    def afname(self,bedrag):
        if(self.startbedrag > bedrag):
            self.startbedrag -= bedrag
        else:
            print("Insufficient Funds.")

b1 = Balans(500)

t = Transactie()

t.afname(250)

print(b1)

t.storting(15)

print(b1)

t.afname(750)

print(b1)