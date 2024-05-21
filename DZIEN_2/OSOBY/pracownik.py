from osoba import Osoba
from sport import Sport,Ekstra

class Pracownik(Osoba,Sport,Ekstra):
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie,
                 dyscyplina=None,lataupr=None,bestwynik=None):
        Osoba.__init__(self,imie,wiek,waga,wzrost)
        Sport.__init__(self,dyscyplina,lataupr,bestwynik)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie
        
    def infopracownik(self):
        print(f"pracownik firmy {self.firma}, stanowisko: {self.stanowisko}, "
              f"lata pracy:{self.latapracy}, wyngrodzenie: {self.wynagrodzenie} zł")
        
    def print_pracownik(self):
        if self.dyscyplina is not None:
            self.infopracownik()
            self.infosport()
        else:
            self.infopracownik()

    def czypracownik(self):
        return True
    
    
            
    
