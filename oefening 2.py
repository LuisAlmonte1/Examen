naam = "claptrap"
taak = "koken"
class Robot:
    def __init__(self, naam, taak):
        self.naam = naam
        self.taak = taak
    def statusbot(self):
       if taak == "koken":
        print(naam, "begint met", taak)
       else:
        print(naam, "stopt met", taak)

p1= Robot("claptrap", "koken")
p1.statusbot()
