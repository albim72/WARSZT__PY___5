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

    def get_kolor_oczu(self):
        return self.kolor_oczy

    def set_kolor_oczu(self,nowykolor):
        self.kolor_oczy = nowykolor

    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opisbmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <= 25:
            return "waga normalna"
        elif self.bmi() <= 30:
            return "nadwaga"
        elif self.bmi() <= 35:
            return "otyłość I stopnia"
        elif self.bmi() <= 40:
            return "otyłość II stopnia"
        else:
            return "otyłość III stopnia"
        
    #zapotrzebowanie energetyczne
        
    def policz_ppm(self,plec):
        if plec == "k":
            return 655.1 + 9.563*self.waga + 1.85*self.wzrost - 4.676*self.wiek
        elif plec == "m":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wiek
        else:
            return "zły wybór"



