class Osoba:
    def __init__(self,imie:str,wiek:int,waga:float,wzrost:float)->None:
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczy = "brązowe"
        self.info()
        
    def __repr__(self):
        return (f"Dane osoby ->\n"
                f"imię: {self.imie}\n"
                f"wiek: {self.wiek} lat\n"
                f"waga: {self.waga} kg\n"
                f"wzrost: {self.wzrost} cm")
        
        
    def info(self)->None:
        print("Tworzenie nowej instancji klasy Osoba -> obiekt Osoba")
        
    def wiek_za_n_lat(self,n):
        return self.wiek + n
    
    def czypracownik(self):
        return False
    
    
        
