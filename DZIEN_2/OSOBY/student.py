from pracownik import Pracownik

class Student(Pracownik):
    def __init__(self, imie, wiek, waga, wzrost, nr_studenta, kierunek, rok,
                 firma = None, stanowisko = None, latapracy= None, wynagrodzenie = None,
                 dyscyplina = None, lataupr = None, bestwynik = None):
        super().__init__(imie, wiek, waga, wzrost, firma, stanowisko, latapracy, wynagrodzenie, dyscyplina, lataupr,
                         bestwynik)
        self.nr_studenta = nr_studenta
        self.kierunek = kierunek
        self.rok = rok

    def infostudent(self):
        print(f'student nr indeksu: {self.nr_studenta}, kierunek: {self.kierunek}, rok studiów: {self.rok}')

    def print_student(self):
        if self.Firma is not None & self.dyscyplina is not None:
            self.infostudent()
            self.infopracownik()
            self.infosport()
        elif self.Firma is not None:
            self.infostudent()
            self.infopracownik()
        elif self.dyscyplina is not None:
            self.infostudent()
            self.infosport()
        else:
            self.infostudent()

    def czypracownik(self) -> bool:
        return self.firma is not None
            
    
