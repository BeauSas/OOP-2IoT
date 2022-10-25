class Drank:
    def __init__(self,naam,temp=20):
        self.naam = naam
        self.temp = temp
    def __repr__(self):
        drankkaart = f"Naam: {self.naam} \t Temperatuur: {self.temp}"
        return drankkaart

drankje1 = Drank("Nalu",8)
drankje2 = Drank("Water",4)
drankje3 = Drank("Rode wijn",27)
drankje4 = Drank("Wodka",15)
drankje5 = Drank("Cola",12)
drankje6 = Drank("Sprite")

counter = 0

print(drankje1)
print(drankje2)
print(drankje3)
print(drankje4)
print(drankje5)
print(drankje6)